
import socket, select, string, sys
import random, time

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

data = s.recv(4096)
print(data.decode())
s.send(("hahaha    " + name).encode())
