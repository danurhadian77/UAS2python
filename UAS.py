import socket


def server_program():
	# get the hostname
	host = socket.gethostname()
	port = 5000 # initiate port no above 1024

	server_socket = socket.socket() # get instance
	# look slosely. The bind() function takes tuple as argument
	server_socket.bind((host, port)) # bind host address and port together

	#configure how many client the server can listen simultaneosly
	server_socket.listen(10)
	conn, address = server_socket.accept() # accept new connection
	print("connection from: "+ str(address))
	while True:
		#recive data stream. it won't accept data packet reater than 1024 bytes
		data = conn.recv(1024).decode()
		if not data:
			# if data is not recived break
			break
		print("from connected user: " + str(data))
		data = input(' -> ')
		conn.send(data.encode()) # send data to the client

	conn.close() #close the connection


if __name__ =='__main__':
	server_program()