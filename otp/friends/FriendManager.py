from pandac.PandaModules import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPGlobals


class FriendManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendManager')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self._FriendManager__available = 0
        self.gameSpecificFunction = None

    def setAvailable(self, available):
        self._FriendManager__available = available
        if self._FriendManager__available and self.gameSpecificFunction:
            self.gameSpecificFunction()

    def getAvailable(self):
        return self._FriendManager__available

    def setGameSpecificFunction(self, function):
        self.gameSpecificFunction = function

    def executeGameSpecificFunction(self):
        if self._FriendManager__available and self.gameSpecificFunction:
            self.gameSpecificFunction()

    def generate(self):
        if base.cr.friendManager is not None:
            base.cr.friendManager.delete()

        base.cr.friendManager = self
        DistributedObject.DistributedObject.generate(self)

    def disable(self):
        base.cr.friendManager = None
        DistributedObject.DistributedObject.disable(self)

    def delete(self):
        self.gameSpecificFunction = None
        base.cr.friendManager = None
        DistributedObject.DistributedObject.delete(self)

    def up_friendQuery(self, inviteeId):
        self.sendUpdate('friendQuery', [inviteeId])
        self.notify.debug('Client: friendQuery(%d)' % inviteeId)

    def up_cancelFriendQuery(self, context):
        self.sendUpdate('cancelFriendQuery', [context])
        self.notify.debug('Client: cancelFriendQuery(%d)' % context)

    def up_inviteeFriendConsidering(self, yesNo, context):
        self.sendUpdate('inviteeFriendConsidering', [yesNo, context])
        self.notify.debug(
            'Client: inviteeFriendConsidering(%d, %d)' % (yesNo, context))

    def up_inviteeFriendResponse(self, yesNoMaybe, context):
        self.sendUpdate('inviteeFriendResponse', [yesNoMaybe, context])
        self.notify.debug(
            'Client: inviteeFriendResponse(%d, %d)' % (yesNoMaybe, context))

    def up_inviteeAcknowledgeCancel(self, context):
        self.sendUpdate('inviteeAcknowledgeCancel', [context])
        self.notify.debug('Client: inviteeAcknowledgeCancel(%d)' % context)

    def friendConsidering(self, yesNoAlready, context):
        self.notify.info('Roger Client: friendConsidering(%d, %d)' %
                         (yesNoAlready, context))
        messenger.send('friendConsidering', [yesNoAlready, context])

    def friendResponse(self, yesNoMaybe, context):
        self.notify.debug(
            'Client: friendResponse(%d, %d)' % (yesNoMaybe, context))
        messenger.send('friendResponse', [yesNoMaybe, context])

    def inviteeFriendQuery(self, inviterId, inviterName, inviterDna, context):
        self.notify.debug('Client: inviteeFriendQuery(%d, %s, dna, %d)' %
                          (inviterId, inviterName, context))
        if not hasattr(base, 'localAvatar'):
            self.up_inviteeFriendConsidering(0, context)
            return None

        if inviterId in base.localAvatar.ignoreList:
            self.up_inviteeFriendConsidering(4, context)
            return None

        if not base.localAvatar.acceptingNewFriends:
            self.up_inviteeFriendConsidering(6, context)
            return None

        self.up_inviteeFriendConsidering(self._FriendManager__available,
                                         context)
        if self._FriendManager__available:
            messenger.send('friendInvitation',
                           [inviterId, inviterName, inviterDna, context])

    def inviteeCancelFriendQuery(self, context):
        self.notify.debug('Client: inviteeCancelFriendQuery(%d)' % context)
        messenger.send('cancelFriendInvitation', [context])
        self.up_inviteeAcknowledgeCancel(context)

    def up_requestSecret(self):
        self.notify.warning('Sending Request')
        self.sendUpdate('requestSecret', [])

    def requestSecretResponse(self, result, secret):
        messenger.send('requestSecretResponse', [result, secret])

    def up_submitSecret(self, secret):
        self.sendUpdate('submitSecret', [secret])

    def submitSecretResponse(self, result, avId):
        messenger.send('submitSecretResponse', [result, avId])