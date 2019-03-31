
import socket, select, string, sys

if __name__ == "__main__":

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	try:
		s.connect(("localhost", 5000))
	except:
		print "connection fail"
		sys.exit()

	print "connected!!"
	s.send("saki")
