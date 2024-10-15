# Johnathan Stormes
import random

# create a unique lobby ID
def createID(ID_list):
    ID = ""
    for x in range(5):
        letter = random.randrange(1, 27)
        ID = ID + chr(64 + letter)
    for x in range(len(ID_list)):
        if ID == ID_list[x]:
            createID(ID_list)
    return ID
    


# lobby class for server data
class Lobby:

    # print all player IDs
    def printPlayerIDs(self):
        for x in range(len(self.players)):
            print (self.players[x].getID())

    # initialize
    def __init__(self, ID_list, host):
        self.players = [host]
        self.ID = createID(ID_list)
        self.host = host
        host.host = True
        self.host.setLobby(self.ID)

    # add a given player
    def addPlayer(self, player):
        if len(self.players) < 10:
            player.lobbyID = self.ID
            self.players.append(player)
        self.printPlayerIDs()

    # remove a given player
    def removePlayer(self, player):
        print("player " + str(player.getID()) + " leaving lobby " + str(self.ID))
        for x in range(len(self.players)):
            if self.players[x].getID() == player.getID():
                self.players[x].host = False
                self.players.pop(x)
                if len(self.players) != 0:
                    self.host = self.players[0]
                    self.host.host = True
                break
        self.printPlayerIDs()
    