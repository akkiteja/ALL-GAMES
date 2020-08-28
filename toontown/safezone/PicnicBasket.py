from pandac.PandaModules import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.fsm import StateData
from toontown.toontowngui import TTDialog
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil


class PicnicBasket(StateData.StateData):
    def __init__(self, safeZone, parentFSM, doneEvent, tableNumber,
                 seatNumber):
        StateData.StateData.__init__(self, doneEvent)
        self.tableNumber = tableNumber
        self.seatNumber = seatNumber
        self.fsm = ClassicFSM.ClassicFSM('PicnicBasket', [
            State.State('start', self.enterStart, self.exitStart,
                        ['requestBoard', 'trolleyHFA', 'trolleyTFA']),
            State.State('trolleyHFA', self.enterTrolleyHFA,
                        self.exitTrolleyHFA, ['final']),
            State.State('trolleyTFA', self.enterTrolleyTFA,
                        self.exitTrolleyTFA, ['final']),
            State.State('requestBoard', self.enterRequestBoard,
                        self.exitRequestBoard, ['boarding']),
            State.State('boarding', self.enterBoarding, self.exitBoarding,
                        ['boarded']),
            State.State('boarded', self.enterBoarded, self.exitBoarded,
                        ['requestExit', 'trolleyLeaving', 'final', 'exiting']),
            State.State('requestExit', self.enterRequestExit,
                        self.exitRequestExit, ['exiting', 'trolleyLeaving']),
            State.State('trolleyLeaving', self.enterTrolleyLeaving,
                        self.exitTrolleyLeaving, ['final']),
            State.State('exiting', self.enterExiting, self.exitExiting,
                        ['final']),
            State.State('final', self.enterFinal, self.exitFinal, ['start'])
        ], 'start', 'final')
        self.parentFSM = parentFSM

    def load(self):
        self.parentFSM.getStateNamed('picnicBasketBlock').addChild(self.fsm)
        self.buttonModels = loader.loadModel(
            'phase_3.5/models/gui/inventory_gui')
        self.upButton = self.buttonModels.find('**//InventoryButtonUp')
        self.downButton = self.buttonModels.find('**/InventoryButtonDown')
        self.rolloverButton = self.buttonModels.find(
            '**/InventoryButtonRollover')

    def unload(self):
        self.parentFSM.getStateNamed('trolley').removeChild(self.fsm)
        del self.fsm
        del self.parentFSM
        self.buttonModels.removeNode()
        del self.buttonModels
        del self.upButton
        del self.downButton
        del self.rolloverButton

    def enter(self):
        self.fsm.enterInitialState()
        if base.localAvatar.hp > 0:
            messenger.send('enterPicnicTableOK_%d_%d' % (self.tableNumber,
                                                         self.seatNumber))
            self.fsm.request('requestBoard')
        else:
            self.fsm.request('trolleyHFA')

    def exit(self):
        self.ignoreAll()

    def enterStart(self):
        pass

    def exitStart(self):
        pass

    def enterTrolleyHFA(self):
        self.noTrolleyBox = TTDialog.TTGlobalDialog(
            message=TTLocalizer.TrolleyHFAMessage,
            doneEvent='noTrolleyAck',
            style=TTDialog.Acknowledge)
        self.noTrolleyBox.show()
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('noTrolleyAck', self._PicnicBasket__handleNoTrolleyAck)

    def exitTrolleyHFA(self):
        self.ignore('noTrolleyAck')
        self.noTrolleyBox.cleanup()
        del self.noTrolleyBox

    def enterTrolleyTFA(self):
        self.noTrolleyBox = TTDialog.TTGlobalDialog(
            message=TTLocalizer.TrolleyTFAMessage,
            doneEvent='noTrolleyAck',
            style=TTDialog.Acknowledge)
        self.noTrolleyBox.show()
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('noTrolleyAck', self._PicnicBasket__handleNoTrolleyAck)

    def exitTrolleyTFA(self):
        self.ignore('noTrolleyAck')
        self.noTrolleyBox.cleanup()
        del self.noTrolleyBox

    def _PicnicBasket__handleNoTrolleyAck(self):
        ntbDoneStatus = self.noTrolleyBox.doneStatus
        if ntbDoneStatus == 'ok':
            doneStatus = {}
            doneStatus['mode'] = 'reject'
            messenger.send(self.doneEvent, [doneStatus])
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(ntbDoneStatus))

    def enterRequestBoard(self):
        pass

    def handleRejectBoard(self):
        doneStatus = {}
        doneStatus['mode'] = 'reject'
        messenger.send(self.doneEvent, [doneStatus])

    def exitRequestBoard(self):
        pass

    def enterBoarding(self, nodePath, side):
        camera.wrtReparentTo(nodePath)
        heading = PythonUtil.fitDestAngle2Src(camera.getH(nodePath), 90 * side)
        self.cameraBoardTrack = LerpPosHprInterval(
            camera, 1.5, Point3(14.4072 * side, 0, 3.8666999999999998),
            Point3(heading, -15, 0))
        self.cameraBoardTrack.start()

    def exitBoarding(self):
        self.ignore('boardedTrolley')

    def enterBoarded(self):
        self.enableExitButton()

    def exitBoarded(self):
        self.cameraBoardTrack.finish()
        self.disableExitButton()

    def enableExitButton(self):
        self.exitButton = DirectButton(
            relief=None,
            text=TTLocalizer.TrolleyHopOff,
            text_fg=(1, 1, 0.65000000000000002, 1),
            text_pos=(0, -0.23000000000000001),
            text_scale=0.80000000000000004,
            image=(self.upButton, self.downButton, self.rolloverButton),
            image_color=(1, 0, 0, 1),
            image_scale=(20, 1, 11),
            pos=(0, 0, 0.80000000000000004),
            scale=0.14999999999999999,
            command=lambda self=self: self.fsm.request('requestExit'))

    def disableExitButton(self):
        self.exitButton.destroy()

    def enterRequestExit(self):
        messenger.send('trolleyExitButton')

    def exitRequestExit(self):
        pass

    def enterTrolleyLeaving(self):
        self.acceptOnce('playMinigame', self.handlePlayMinigame)
        self.acceptOnce('picnicDone', self.handlePicnicDone)

    def handlePlayMinigame(self, zoneId, minigameId):
        base.localAvatar.b_setParent(ToontownGlobals.SPHidden)
        doneStatus = {}
        doneStatus['mode'] = 'minigame'
        doneStatus['zoneId'] = zoneId
        doneStatus['minigameId'] = minigameId
        messenger.send(self.doneEvent, [doneStatus])

    def handlePicnicDone(self):
        doneStatus = {}
        doneStatus['mode'] = 'exit'
        messenger.send(self.doneEvent, [doneStatus])

    def exitTrolleyLeaving(self):
        self.ignore('playMinigame')
        taskMgr.remove('leavingCamera')
        return self.notify.debug('handling golf kart  done event')

    def enterExiting(self):
        pass

    def handleOffTrolley(self):
        doneStatus = {}
        doneStatus['mode'] = 'exit'
        messenger.send(self.doneEvent, [doneStatus])

    def exitExiting(self):
        pass

    def enterFinal(self):
        pass

    def exitFinal(self):
        pass
