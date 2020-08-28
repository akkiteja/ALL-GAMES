from pandac.PandaModules import Point3, VBase4
from direct.fsm.FSM import FSM
from direct.interval.IntervalGlobal import Sequence, Parallel, ActorInterval, Func, Wait, ParticleInterval, Track, LerpColorScaleInterval, LerpScaleInterval, LerpHprInterval
from direct.task.Task import Task
from toontown.battle import BattleParticles
from toontown.battle import MovieUtil
from toontown.minigame.MazeSuit import MazeSuit
from CogdoMazeGameObjects import CogdoMazeSplattable
import CogdoMazeGameGlobals as Globals
import random


class CogdoMazeSuit(MazeSuit, FSM, CogdoMazeSplattable):
    GagHitEventName = 'CogdoMazeSuit_GagHit'
    DeathEventName = 'CogdoMazeSuit_Death'
    ThinkEventName = 'CogdoMazeSuit_Think'

    def __init__(self,
                 serialNum,
                 maze,
                 randomNumGen,
                 difficulty,
                 startTile,
                 cogdoSuitType,
                 walkAnimName=None):
        data = Globals.SuitData[cogdoSuitType]
        MazeSuit.__init__(
            self,
            serialNum,
            maze,
            randomNumGen,
            data['cellWalkPeriod'],
            difficulty,
            data['dnaName'],
            startTile=startTile,
            walkSameDirectionProb=Globals.SuitWalkSameDirectionProb,
            walkTurnAroundProb=Globals.SuitWalkTurnAroundProb,
            uniqueRandomNumGen=False,
            walkAnimName=walkAnimName)
        FSM.__init__(self, 'CogdoMazeSuit')
        CogdoMazeSplattable.__init__(
            self, self.suit,
            '%s-%i' % (Globals.SuitCollisionName, self.serialNum), 1.5)
        if 'scale' in data:
            self.suit.setScale(data['scale'])

        self.hp = data['hp']
        self.type = cogdoSuitType
        self.memos = data['memos']
        self.deathSuit = self.suit.getLoseActor()
        self.deathSuit.pose('lose', 0)
        BattleParticles.loadParticles()
        self._initSfx()

    def _initSfx(self):
        audioMgr = base.cogdoGameAudioMgr
        self._deathSoundIval = Sequence(
            audioMgr.createSfxIval(
                'cogSpin',
                duration=1.6000000000000001,
                startTime=0.59999999999999998,
                volume=0.80000000000000004,
                source=self.deathSuit),
            audioMgr.createSfxIval(
                'cogDeath', volume=0.32000000000000001, source=self.deathSuit))

    def _destroySfx(self):
        if self._deathSoundIval.isPlaying():
            self._deathSoundIval.finish()

        del self._deathSoundIval

    def destroy(self):
        BattleParticles.unloadParticles()
        self.ignoreAll()
        self._destroySfx()
        CogdoMazeSplattable.destroy(self)
        MazeSuit.destroy(self)

    def handleEnterSphere(self, collEntry):
        messenger.send(self.COLLISION_EVENT_NAME, [self.type, self.serialNum])

    def gameStart(self, gameStartTime):
        MazeSuit.gameStart(self, gameStartTime)
        self.accept(
            Globals.GagCollisionName + '-into-' + self.gagCollisionName,
            self.handleGagHit)
        messenger.send(self.ThinkEventName, [self, self.TX, self.TY])

    def initCollisions(self):
        MazeSuit.initCollisions(self)
        self.collNodePath.setScale(0.75)
        self.accept(
            self.uniqueName('again' + self.COLL_SPHERE_NAME),
            self.handleEnterSphere)

    def think(self, curTic, curT, unwalkables):
        MazeSuit.think(self, curTic, curT, unwalkables)
        messenger.send(self.ThinkEventName, [self, self.TX, self.TY])

    def handleGagHit(self, collEntry):
        gagNodePath = collEntry.getFromNodePath().getParent()
        messenger.send(self.GagHitEventName,
                       [self.type, self.serialNum, gagNodePath])

    def _getSuitAnimationIval(self,
                              animName,
                              startFrame=0,
                              duration=1,
                              partName=None,
                              nextState=None):
        totalFrames = self.suit.getNumFrames(animName)
        frames = totalFrames - 1 - startFrame
        frameRate = self.suit.getFrameRate(animName)
        newRate = frames / duration
        playRate = newRate / frameRate
        ival = Sequence(
            ActorInterval(
                self.suit,
                animName,
                startTime=startFrame / newRate,
                endTime=totalFrames / newRate,
                playRate=playRate,
                partName=partName))
        if nextState is not None:

            def done():
                self.request(nextState)

            ival.append(Func(done))

        return ival

    def hitByGag(self):
        self.hp = self.hp - 1
        self.doSplat()
        if self.hp <= 0:
            self.explode()

    def explode(self):
        self.doDeathTrack()
        messenger.send(self.DeathEventName, [self.type, self.serialNum])

    def doDeathTrack(self):
        def removeDeathSuit(suit, deathSuit):
            if not deathSuit.isEmpty():
                deathSuit.detachNode()
                suit.cleanupLoseActor()

        self.deathSuit.reparentTo(self.suit.getParent())
        self.deathSuit.setScale(self.suit.getScale())
        self.deathSuit.setPos(render, self.suit.getPos(render))
        self.deathSuit.setHpr(render, self.suit.getHpr(render))
        self.suit.hide()
        self.collNodePath.reparentTo(self.deathSuit)
        gearPoint = Point3(0, 0, self.suit.height / 2.0 + 2.0)
        smallGears = BattleParticles.createParticleEffect(
            file='gearExplosionSmall')
        singleGear = BattleParticles.createParticleEffect(
            'GearExplosion', numParticles=1)
        smallGearExplosion = BattleParticles.createParticleEffect(
            'GearExplosion', numParticles=10)
        bigGearExplosion = BattleParticles.createParticleEffect(
            'BigGearExplosion', numParticles=30)
        smallGears.setPos(gearPoint)
        singleGear.setPos(gearPoint)
        smallGearExplosion.setPos(gearPoint)
        bigGearExplosion.setPos(gearPoint)
        smallGears.setDepthWrite(False)
        singleGear.setDepthWrite(False)
        smallGearExplosion.setDepthWrite(False)
        bigGearExplosion.setDepthWrite(False)
        suitTrack = Sequence(
            Func(self.collNodePath.stash),
            ActorInterval(self.deathSuit, 'lose', startFrame=80, endFrame=140),
            Func(
                removeDeathSuit,
                self.suit,
                self.deathSuit,
                name='remove-death-suit'))
        explosionTrack = Sequence(
            Wait(1.5),
            MovieUtil.createKapowExplosionTrack(
                self.deathSuit, explosionPoint=gearPoint))
        gears1Track = Sequence(
            ParticleInterval(
                smallGears,
                self.deathSuit,
                worldRelative=0,
                duration=4.2999999999999998,
                cleanup=True),
            name='gears1Track')
        gears2MTrack = Track((0.0, explosionTrack),
                             (0.69999999999999996,
                              ParticleInterval(
                                  singleGear,
                                  self.deathSuit,
                                  worldRelative=0,
                                  duration=5.7000000000000002,
                                  cleanup=True)), (5.2000000000000002,
                                                   ParticleInterval(
                                                       smallGearExplosion,
                                                       self.deathSuit,
                                                       worldRelative=0,
                                                       duration=1.2,
                                                       cleanup=True)),
                             (5.4000000000000004,
                              ParticleInterval(
                                  bigGearExplosion,
                                  self.deathSuit,
                                  worldRelative=0,
                                  duration=1.0,
                                  cleanup=True)),
                             name='gears2MTrack')

        def removeParticle(particle):
            if particle and hasattr(particle, 'renderParent'):
                particle.cleanup()
                del particle

        removeParticles = Sequence(
            Func(removeParticle, smallGears), Func(removeParticle, singleGear),
            Func(removeParticle, smallGearExplosion),
            Func(removeParticle, bigGearExplosion))
        self.deathTrack = Sequence(
            Parallel(suitTrack, gears2MTrack, gears1Track,
                     self._deathSoundIval), removeParticles)
        self.deathTrack.start()


class CogdoMazeSlowMinionSuit(CogdoMazeSuit):
    def __init__(self,
                 serialNum,
                 maze,
                 randomNumGen,
                 difficulty,
                 startTile=None):
        CogdoMazeSuit.__init__(self, serialNum, maze, randomNumGen, difficulty,
                               startTile, Globals.SuitTypes.SlowMinion)
        self.defaultTransitions = {
            'Off': ['Normal'],
            'Normal': ['Attack', 'Off'],
            'Attack': ['Normal']
        }

    def gameStart(self, gameStartTime):
        CogdoMazeSuit.gameStart(self, gameStartTime)
        self.request('Normal')

    def enterNormal(self):
        self.startWalkAnim()

    def exitNormal(self):
        pass

    def enterAttack(self, elapsedTime):
        self._attackIval = self._getSuitAnimationIval(
            'finger-wag', duration=2.0, nextState='Normal')
        self._attackIval.start(elapsedTime)

    def filterAttack(self, request, args):
        if request == 'Attack':
            return None
        else:
            return self.defaultFilter(request, args)

    def exitAttack(self):
        self._attackIval.pause()
        del self._attackIval


class CogdoMazeFastMinionSuit(CogdoMazeSuit):
    def __init__(self,
                 serialNum,
                 maze,
                 randomNumGen,
                 difficulty,
                 startTile=None):
        CogdoMazeSuit.__init__(self, serialNum, maze, randomNumGen, difficulty,
                               startTile, Globals.SuitTypes.FastMinion)


class CogdoMazeBossSuit(CogdoMazeSuit):
    BlinkTaskName = 'CogdoMazeBossBlinkTask'
    ShakeTaskName = 'CogdoMazeBossShakeTask'
    StartWalkTaskName = 'CogdoMazeBossStartWalkTask'
    ShakeEventName = 'CogdoMazeSuitShake'

    def __init__(self,
                 serialNum,
                 maze,
                 randomNumGen,
                 difficulty,
                 startTile=None):
        CogdoMazeSuit.__init__(
            self,
            serialNum,
            maze,
            randomNumGen,
            difficulty,
            startTile,
            Globals.SuitTypes.Boss,
            walkAnimName='stomp')
        self.dropTimer = 0
        self._walkSpeed = (
            float(self.maze.cellWidth) / self.cellWalkDuration) * 0.5

    def _initSfx(self):
        CogdoMazeSuit._initSfx(self)
        audioMgr = base.cogdoGameAudioMgr
        self._stompSfxIval = audioMgr.createSfxIval(
            'cogStomp',
            source=self.suit,
            cutoff=Globals.BossStompSfxCutoff,
            volume=0.29999999999999999)
        self._hitSfx = audioMgr.createSfx('bossCogAngry', self.suit)

    def _destroySfx(self):
        del self._hitSfx
        if self._stompSfxIval.isPlaying():
            self._stompSfxIval.finish()

        del self._stompSfxIval
        CogdoMazeSuit._destroySfx(self)

    def spin(self):
        part = self.suit
        time = Globals.BossSpinTime
        degrees = 360 * Globals.BossSpinCount
        spinIval = LerpHprInterval(
            part,
            time, (self.suit.getH() + degrees, 0, 0),
            blendType='easeOut')
        spinIval.start()

    def hitByGag(self):
        if self.hp >= 2:
            self._hitSfx.play()
            self.spin()
            self.suit.setColorScale(Globals.BlinkColor)
            self._CogdoMazeBossSuit__startBlinkTask()
        elif self.hp == 1:
            self._CogdoMazeBossSuit__stopBlinkTask()

        CogdoMazeSuit.hitByGag(self)

    def gameStart(self, gameStartTime):
        CogdoMazeSuit.gameStart(self, gameStartTime)

    def startWalkAnim(self):
        self.suit.loop(self._walkAnimName, fromFrame=43, toFrame=81)
        self.suit.setPlayRate(
            self._walkSpeed * Globals.BossCogStompAnimationPlayrateFactor,
            self._walkAnimName)
        self._CogdoMazeBossSuit__startShakeTask()

    def destroy(self):
        CogdoMazeSuit.destroy(self)
        self._CogdoMazeBossSuit__stopShakeTask()
        self._CogdoMazeBossSuit__stopBlinkTask()

    def pickRandomValidSpot(self, r=5):
        validSpots = []
        for x in range(self.TX - r, self.TX + r):
            for y in range(self.TY - r, self.TY + r):
                if self.maze.isWalkable(x, y):
                    validSpots.append([x, y])
                    continue

        return self.rng.choice(validSpots)

    def _CogdoMazeBossSuit__startShakeTask(self):
        self._CogdoMazeBossSuit__stopShakeTask()
        taskMgr.doMethodLater(Globals.BossShakeTime,
                              self._CogdoMazeBossSuit__shake,
                              self.uniqueName(CogdoMazeBossSuit.ShakeTaskName))
        self.bossShakeLastTime = 0

    def _CogdoMazeBossSuit__stopShakeTask(self):
        taskMgr.remove(self.uniqueName(CogdoMazeBossSuit.ShakeTaskName))

    def _CogdoMazeBossSuit__shake(self, task):
        if task.time - self.bossShakeLastTime > Globals.BossShakeTime:
            self.suit.setPlayRate(
                self._walkSpeed * Globals.BossCogStompAnimationPlayrateFactor,
                self._walkAnimName)
            self._stompSfxIval.start()
            messenger.send(self.ShakeEventName,
                           [self, Globals.BossShakeStrength])
            self.bossShakeLastTime = task.time

        return task.cont

    def _CogdoMazeBossSuit__startBlinkTask(self):
        self._CogdoMazeBossSuit__stopBlinkTask()
        taskMgr.doMethodLater(Globals.BlinkFrequency,
                              self._CogdoMazeBossSuit__blink,
                              CogdoMazeBossSuit.BlinkTaskName)

    def _CogdoMazeBossSuit__stopBlinkTask(self):
        taskMgr.remove(CogdoMazeBossSuit.BlinkTaskName)

    def _CogdoMazeBossSuit__blink(self, task):
        blink = Sequence(
            LerpColorScaleInterval(self.suit, Globals.BlinkSpeed,
                                   VBase4(1.0, 1.0, 1.0, 1.0)),
            LerpColorScaleInterval(self.suit, Globals.BlinkSpeed,
                                   Globals.BlinkColor))
        blink.start()
        return Task.again