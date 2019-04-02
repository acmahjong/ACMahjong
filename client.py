
import socket, select, string, sys
import random, time
import json

if __name__ == "__main__":

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(2000)
	name = "saki " + str(random.randint(1,10000))

	try:
		s.connect(("localhost", 5000))
	except:
		print("connection fail")
		sys.exit()

	print("connected!! as " + name)
	s.send(name.encode())
	
"""
	while True:
		socket_list = [s]

		# Get the list sockets which are readable
		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

		for sock in read_sockets:
			data = sock.recv(4096)
			print data
			time.sleep(2)
			sock.send("2333" + name)
"""

data = s.recv(4096).decode()
print(data)

ar = json.loads(data)
global hand
hand = ar["tiles"]
print(hand)

s.send(("hahaha    " + name).encode())

while True:
	data = s.recv(4096).decode()
	print("~~~~~~~~~~~~ " + data)
	dic = json.loads(data)
	hand.append(dic["tile"])
	tileToDiscard = random.randint(0, len(hand) - 1)
	print(hand, tileToDiscard)
	s.send(json.dumps({"key" : "discard", "tile" : hand[tileToDiscard]}).encode())
	del(hand[tileToDiscard])
	time.sleep(1)
	

