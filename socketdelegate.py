import socket

class SocketConnection:

	connection = None

	def __init__(self, address, port):
		self.connection = socket.socket()
		self.connection.connect((address, port));

	def read(self):
		return self.connection.recv(1024)

	def send(self, data):
		self.connection.send(data)

	def close(self):
		self.connection.close()
