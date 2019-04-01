
import socket, select
import random
import json

player_list = []
recv_buffer = 4096
port = 5000

yama = []
idx = 0
lastIndex = 0
doras = []
uradoras = []

def initialize():
	yama.clear()
	for i in range(136):
		yama.append(i)
	random.shuffle(yama)	 
	idx = 0
	lastIndex = 122
	

def distribute(oya):
	for i in range(4):
		curPlayer = (i + oya) % 4
		ar = []
		for _ in range(13):
			ar.append(yama[idx])
			idx = idx + 1
		json.dumps({"key" : "distribute", "tiles" : ar, "oya" : oya, })
		player_list[curPlayer][0].send("")
		txt = player_list[curPlayer][0].recv(recv_buffer)
		print(txt)


if __name__ == "__main__":
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # this has no effect, why ?
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("0.0.0.0", port))
	server_socket.listen(10)

	print("waiting for players.....")

	while len(player_list) < 4:
		read_sockets, write_sockets, error_sockets = select.select([server_socket], [], [])
		sockfd, addr = server_socket.accept()
		player_list.append([sockfd, addr])
		print("player (%s, %s) connected" % addr)
		name = sockfd.recv(recv_buffer)
		if name:
			print("name : %s" % name)

	GAME_COUNT = 1
	BANBA = 0
	OYA = random.randint(0, 3)

	initialize()
	distribute()
