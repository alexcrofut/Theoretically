import socket
import pickle
from _thread import *
from player import Player
from game import Game
import sys

server = "10.0.0.45"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(connection, player, game_id):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if game_id in games:
                game = games[game_id]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_went()
                    elif data != "get":
                        game.play_move(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost connection!")
    print("Closing Game ", game_id)
    try:
        del games[game_id]
    except:
        print("Couldn't close Game ", game_id)
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating new game ... ", gameId)
    else:
        games[gameId].ready = True
        p = 1
        print("Joining game ... ", gameId)

    start_new_thread(threaded_client, (conn, p, gameId))
