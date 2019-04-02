
import socket, select
import random
import json
from utils.utils import *

class Server:

	player_list = []
	player_count = 2

	yama = []
	idx = 0
	lastIdx = 0
	doras = []
	uradoras = []

	def initialize(self):
		self.yama.clear()
		for i in range(136):
			self.yama.append(i)
		for i in self.yama:
			print(get34Str(i), end=" ")
		print("")
		random.shuffle(self.yama)	 
		for i in self.yama:
			print(get34Str(i), end=" ")
		print("")
		self.idx = 0
		self.lastIdx = 122
		self.doras.append(self.yama[self.lastIdx + 8])
		

	def distribute(self, oya):
		for i in range(self.player_count):
			curPlayer = (i + oya) % self.player_count
			ar = []
			for _ in range(13):
				ar.append(self.yama[self.idx])
				self.idx = self.idx + 1
			dat = json.dumps({"key" : "distribute", "tiles" : ar, "oya" : oya, "dora" : get34Str(getNextTile(self.doras[0]))})
			print(dat)
			self.player_list[curPlayer][0].send(dat.encode())
			txt = self.player_list[curPlayer][0].recv(4096).decode()
			print(txt)

	def giveTileTo(self, player, tile):
		dat = json.dumps({"key" : "getTile", "tile" : tile})
		print("send    " + dat)
		self.player_list[player][0].send(dat.encode())

	def startround(self, oya):
		curPlayer = oya
		while True:
			self.giveTileTo(curPlayer, self.yama[self.idx])
			print("give " + get34Str(self.yama[self.idx]) + " to " + str(curPlayer))
			res = json.loads(self.player_list[curPlayer][0].recv(4096).decode())
			print(", who choose to discard " + str(res["tile"]))
			self.idx = self.idx + 1
			curPlayer = (curPlayer + 1) % self.player_count
			if self.idx == self.lastIdx:
				break


	def main(self):
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind(("0.0.0.0", 5000))
		server_socket.listen(10)

		print("waiting for players.....")

		while len(self.player_list) < self.player_count:
			read_sockets, write_sockets, error_sockets = select.select([server_socket], [], [])
			sockfd, addr = server_socket.accept()
			print("player (%s, %s) connected" % addr)
			name = sockfd.recv(4096).decode()
			if name:
				print("name : %s" % name)
			self.player_list.append([sockfd, addr, name])

		GAME_COUNT = 1
		BANBA = 0
		OYA = random.randint(0, self.player_count - 1)

		self.initialize()
		self.distribute(OYA)

		self.startround(OYA)

if __name__ == "__main__":
	a = Server()
	a.main()
