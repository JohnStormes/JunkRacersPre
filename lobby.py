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
    def printPlayerInfo(self):
        for x in range(len(self.players)):
            print (self.players[x].getID())

    # print team hierarchy
    def printTeamHierarchy(self):
        for x in range(len(self.team_list)):
            for y in range(len(self.team_list[x])):
                print("team " + str(x) + ", player ID: " + str(self.team_list[x][y].ID))

    # initialize
    def __init__(self, ID_list, host):
        self.players = [host]
        self.ID = createID(ID_list)
        self.host = host.ID
        self.players[0].setLobby(self.ID)
        self.team_list = [[host], [], [], [], []]
        self.team_count = 1

    # add a given player
    def addPlayer(self, player):
        if len(self.players) < 10:
            player.lobbyID = self.ID
            self.players.append(player)
            found_slot = False
            for x in range(len(self.team_list)):
                if len(self.team_list[x]) != 2:
                    open_slot = x
                    self.team_list[open_slot].append(player)
                    found_slot = True
                    break
            if not found_slot:
                print("lobby full!")
        #self.printPlayerInfo()
        self.printTeamHierarchy()

    # remove a given player
    def removePlayer(self, player):
        #self.printPlayerInfo()
        print("player " + str(player.ID) + " leaving lobby " + str(self.ID))

        # find player in lobby
        found_ID_index = -1
        for x in range(len(self.players)):
            if self.players[x].ID == player.ID:
                found_ID_index = x

        # if player attempting to remove is in the lobby
        if found_ID_index != -1:
            self.players.pop(found_ID_index)
            # find player ID in team list and remove
            team_x = -1
            team_y = -1
            for x in range(len(self.team_list)):
                for y in range(len(self.team_list[x])):
                    if self.team_list[x][y].ID == player.ID:
                        team_x = x
                        team_y = y
            
            if team_x != -1 and team_y != -1:
                self.team_list[team_x].pop(team_y)

            # update host
            if player.ID == self.host and len(self.players) != 0:
                self.host = self.players[0].ID
        self.printTeamHierarchy()

    # player attempt to change teams
    def changeTeam(self, player, team):
        # find player ID in team list
        team_x = -1
        team_y = -1
        for x in range(len(self.team_list)):
            for y in range(len(self.team_list[x])):
                if self.team_list[x][y].ID == player.ID:
                    team_x = x
                    team_y = y

        if len(self.team_list[team]) < 2:
            self.team_list[team_x].pop(team_y)
            self.team_list[team].append(player)
            return True
        else:
            return False
    