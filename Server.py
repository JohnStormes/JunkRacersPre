import socket
from _thread import *
from Player import Player
import sys
import pickle

#server and port
server = "128.226.250.52"
port = 5555

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the server and port to the socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# s.listen(2) means 2 people can connect to this server
s.listen(5)
print("Waiting for a connection, server started")

# client data stored on server side
players = []

#creates new thread for a client (one thread for each client always running)
next_id = 0
def threadedClient(conn, player_ID):
    global players
    player = Player(player_ID)
    players.append(player)
    # get the information for this client when thread is created
    conn.send(pickle.dumps(players[players.index(player)]))
    print("connected player ID " + str(player.getID()))
    while True:
        try:

            # receive data from the client
            data = pickle.loads(conn.recv(4096))          # 2048 is size of data being passed in, the larger this is, the longer the server takes

            # use the data (a player object) to update the player data
            # reset player index every loop because as other players disconnect and reconnect, this index can change
            # find the players index by finding it's ID In the system, a unique value that cannot change
            for x in range(len(players)):
                if players[x].getID() == player.getID():
                    player_index = x
                    players[player_index] = data
                    break
            reply = []
            
            if not data:
                print("Disconnected")
                break
            else:
                # send other players data back to this client (or this players data if this is the only player on the server)
                if len(players) == 1:
                    reply.append(players[0])
                else:
                    reply = players.copy()
                    reply.pop(player_index)
                #print("Received: ", data)
                #print("Sending: ", reply)
            
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost connection with player ID: " + str(player.getID()))

    # remove disconnected player from player list
    for x in range(len(players)):
        if players[x].getID() == player.getID():
            print("removing player " + str(player.getID()) + " from index " + str(x))
            players.pop(x)
            break
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threadedClient, (conn, next_id))
    next_id += 1