import socket
from _thread import *
from player import Player
import sys
import pickle
from lobby import Lobby
import helper

#server and port
# ONLINE SERVER:
# (leave as empty string)
# LOCAL SERVER FOR DEBUGGING:
# 128.226.250.52
server = "128.226.250.52"
port = 5555

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the server and port to the socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# s.listen(2) means after the queue of joinees exceeds 2, clients attempting to join are kicked
# 5 is fine and should never change. Server should be able to process clients fast enough to never back up past 5
s.listen(5)
print("Waiting for a connection, server started")

# on server side data
lobbies = []            # list of all active lobbies
lobby_ID_list = []            # list of all active lobby IDs
num_of_players = 0

#creates new thread for a client (one thread for each client always running)
next_id = 0

def threadedClient(conn, player_ID):
    global lobbies, lobby_ID_list, num_of_players
    global next_id
    player = Player(player_ID)
    num_of_players += 1
    # get the information for this client when thread is created
    conn.send(pickle.dumps(player))
    print("connected player ID " + str(player.getID()))
    while True:
        try:

            # receive data from the client
            # CURRENT DATA BREAKDOWN:
            # data[0] = player object to be updated in server
            # data[1] = decision value
            #           refer to helper constants
            # data[2] = join code
            #           for use ONLY when decision value == helper.JOIN_LOBBY
            data = pickle.loads(conn.recv(4096))          # 4096 is size of data being passed in, the larger this is, the longer the server takes
            player_received = data[0]
            decision_value = data[1]
            join_code = data[2]

            lobby_ID_index = -1

            # find which lobby player is in, if any
            if player_received.getLobby() != "":
                lobby_ID = player_received.getLobby()
                for x in range(len(lobby_ID_list)):
                    if lobby_ID_list[x] == lobby_ID:
                        lobby_ID_index = x

            # use data[0] (a player object) to update the server side player data
            # reset player index every loop because as other players disconnect and reconnect, this index can change
            # find the players index by finding it's ID In the system, a unique value that cannot change
            if lobby_ID_index != -1:
                for x in range(len(lobbies[lobby_ID_index].players)):
                    if lobbies[lobby_ID_index].players[x].getID() == player.getID():
                        player_index = x
                        lobbies[lobby_ID_index].players[player_index] = player_received
                        break
            
            # use data[1] to make decision
            # create lobby
            if decision_value == helper.CREATE_LOBBY:
                new_lobby = Lobby(lobby_ID_list, player_received)
                lobbies.append(new_lobby)
                lobby_ID_list.append(new_lobby.ID)
                print(lobby_ID_list)
            # attempt to join lobby
            elif decision_value == helper.JOIN_LOBBY:
                print("player " + str(player_received.ID) + " attempting to join: ")
                print(join_code)
                print("")
                lobby_found = ""
                lobby_found_index = -1
                for x in range(len(lobby_ID_list)):
                    if join_code == lobby_ID_list[x]:
                        lobby_found = lobbies[x]
                        lobby_found_index = x
                        lobby_ID_index = x
                if lobby_found == "":
                    print("lobby not found")
                else:
                    print("lobby found, adding player")
                    lobbies[lobby_found_index].addPlayer(player_received)
                    #player_received.lobbyID = join_code
            # leave lobby
            elif decision_value == helper.LEAVE_LOBBY:
                lobbies[lobby_ID_index].removePlayer(player_received)
                player_received.lobbyID = ""
                # if there's no more players in the lobby, delete it
                if len(lobbies[lobby_ID_index].players) == 0:
                    print("removing lobby " + str(lobbies[lobby_ID_index].ID))
                    lobbies.pop(lobby_ID_index)
                    lobby_ID_list.pop(lobby_ID_index)

            # create reply to client
            reply = []
            if not player_received:
                print("Disconnected")
                break
            else:
                # reply is player data being sent back to client
                if player_received.lobbyID != "":
                    reply = lobbies[lobby_ID_index].players
                else:
                    reply = [player_received]
                #print("Received: ", data)
                #print("Sending: ", reply)
            

            # send out data to client from server
            # current data:
            # data[0]: list of players in server including client
            # data[1]: number of clients in server
            conn.sendall(pickle.dumps((reply, num_of_players)))
        except:
            break
    print("Lost connection with player ID: " + str(player.getID()))

    # remove disconnected client from any lobby it was in
    if player_received.getLobby() != "":
        lobbies[lobby_ID_index].removePlayer(player_received)
        # if there's no more players in the lobby, delete it
        if len(lobbies[lobby_ID_index].players) == 0:
            print("removing lobby " + str(lobbies[lobby_ID_index].ID))
            lobbies.pop(lobby_ID_index)
            lobby_ID_list.pop(lobby_ID_index)

    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threadedClient, (conn, next_id))
    next_id += 1