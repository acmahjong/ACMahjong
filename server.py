
import socket, select


if __name__ == "__main__":
	
	player_list = []
	recv_buffer = 4096
	port = 5000

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # this has no effect, why ?
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("0.0.0.0", port))
	server_socket.listen(10)

	print "waiting for players....."

	while len(player_list) < 4:
		read_sockets, write_sockets, error_sockets = select.select([server_socket], [], [])
		sockfd, addr = server_socket.accept()
		player_list.append([sockfd, addr])
		print "player (%s, %s) connected" % addr
		name = sockfd.recv(recv_buffer)
		if name:
			print "name : %s" % name


	initialization()

