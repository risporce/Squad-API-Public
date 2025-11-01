from Packets.Client.ClientHelloMessage import ClientHelloMessage
from Packets.Server.ServerHelloMessage import ServerHelloMessage
from Packets.Client.LoginMessage import LoginMessage
from Packets.Server.LoginOkMessage import LoginOkMessage
from Packets.Server.LoginFailedMessage import LoginFailedMessage
from Packets.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Packets.Client.AskPlayerProfileMessage import AskPlayerProfileMessage
from Packets.Client.AskForLeaderboardDataMessage import AskForLeaderboardDataMessage
from Packets.Client.AskForLocalLeaderboardDataMessage import AskForLocalLeaderboardDataMessage
from Packets.Server.PlayerProfileMessage import PlayerProfileMessage
from Packets.Server.LeaderboardDataMessage import LeaderboardDataMessage
from Packets.Server.LocalLeaderboardDataMessage import LocalLeaderboardDataMessage
from Packets.Server.KeepAliveServerMessage import KeepAliveServerMessage
from Packets.Client.KeepAliveMessage import KeepAliveMessage
from Packets.PacketsEnum import LogicSquadPackets

class LogicSquadMessageFactory:
    messagesList = {
        LogicSquadPackets.CLIENT_HELLO_MESSAGE.value: ClientHelloMessage,
        LogicSquadPackets.ASK_PLAYER_PROFILE_MESSAGE.value: AskPlayerProfileMessage,
        LogicSquadPackets.SERVER_HELLO_MESSAGE.value: ServerHelloMessage,
        LogicSquadPackets.LOGIN_MESSAGE.value: LoginMessage,
        LogicSquadPackets.LOGIN_OK_MESSAGE.value: LoginOkMessage,
        LogicSquadPackets.LOGIN_FAILED_MESSAGE.value: LoginFailedMessage,
        LogicSquadPackets.PLAYER_PROFILE_MESSAGE.value: PlayerProfileMessage,
        LogicSquadPackets.ASK_LEADERBOARD_DATA_MESSAGE.value : AskForLeaderboardDataMessage,
        LogicSquadPackets.ASK_LOCAL_LEADERBOARD_DATA_MESSAGE.value : AskForLocalLeaderboardDataMessage,
        LogicSquadPackets.LEADERBOARD_DATA_MESSAGE.value : LeaderboardDataMessage,
        LogicSquadPackets.LOCAL_LEADERBOARD_DATA_MESSAGE.value : LocalLeaderboardDataMessage,
        LogicSquadPackets.OWN_HOME_DATA_MESSAGE.value: OwnHomeDataMessage,
        LogicSquadPackets.KEEP_ALIVE_MESSAGE.value : KeepAliveMessage,
        LogicSquadPackets.KEEP_ALIVE_SERVER_MESSAGE.value : KeepAliveServerMessage,
    }


    def getMessageName(messageType):
            try:
                message = LogicSquadMessageFactory.messagesList[messageType]
            except KeyError:
                message = str(messageType)
            if type(message) == str:
                return message
            else:
                return message.__name__

    def messageExist(messageType):
        return (messageType in LogicSquadMessageFactory.messagesList.keys())

    def createMessageByType(messageType, messagePayload, logicData):
        messagesList = LogicSquadMessageFactory.messagesList
        if LogicSquadMessageFactory.messageExist(messageType):
            if type(messagesList[messageType]) == str:
                pass
                #print(LogicSquadMessageFactory.getMessageName(messageType), "skipped")
            else:
                #print(LogicSquadMessageFactory.getMessageName(messageType), "created")
                return messagesList[messageType](messagePayload, logicData)
        else:
            return None