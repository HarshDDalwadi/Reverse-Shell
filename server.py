import socket
import sys

# Create socket
def socket_create():
	try:
		global host #IPAddress
		global port #Port
		global s
		host = ''
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print("Socket creation error " + str(msg))


# Bind socket to port and wait for connection from client

def socket_bind():
	try:
		global host #IPAddress
		global port #Port
		global s
		print("Binding socket to port : " + str(port))
		s.bind((host, port))
		s.listen(5) # Number of backlogs, people in the queue
	except socket.error as msg:
		print("Socket binding error : " + str(msg) + "\n" + "Retrying...")
		socket_bind()

#Extablish a connection with client

def socket_accept():
	conn, address = s.accept() # Accepts a new connection
	print(address, conn)
	print("Connection has been established | " + "IP " + address[0] + "| Port " + str(address[1]))
	send_commands(conn)
	conn.close()


#Send commands

def send_commands(conn):
	while True:
		cmd = input()
		if(cmd == 'quit'):
			conn.close()
			s.close()
			sys.exit()
		if(len(str.encode(cmd)) > 0): #encode : converts string to bytes
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end = "")


def main():
	socket_create()
	socket_bind()
	socket_accept()

main()