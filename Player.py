#Johnathan Stormes 2024

class Player:
    def __init__(self, ID):
        self.ID = ID
        self.lobbyID = ""
        self.team = -1
    
    # mutators
    def setLobby(self, lobbyID):
        self.lobbyID = lobbyID
    def setTeam(self, team):
        self.team = team

    # accessors
    def getLobby(self):
        return self.lobbyID
    def getTeam(self):
        return self.team
    def getID(self):
        return self.ID