import socket

class SocketConnection:

	self.connection = None

	def __init__(self, address, port):
		self.connection = socket.socket()
		self.socket.connect((address, port));

	def readData(self):
		self.connection.recv(1024)

	def send(self, data):
		self.connection.send(data)

	def close(self):
		self.connection.close()
