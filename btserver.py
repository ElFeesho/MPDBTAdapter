#!/usr/bin/python

from bluetooth import *

class BTClient:
	client_sock = None
	def __init__(self, client_sock):
		self.client_sock = client_sock

	def read(self):
		buffer = ""
		try:
			while True:
				data = self.client_sock.recv(1024)
				if len(data) == 0:
					break
				buffer = buffer + data
		except IOError:
			print("Client disconnection?")
			# Client disconnected?
		return buffer

	def send(data):
		self.client_sock.send(data)

class BTServer:
	server_sock = None
	channel = None

	def __init__(self):
		self.server_sock = BluetoothSocket( RFCOMM )
		self.server_sock.bind(("",PORT_ANY))
		self.channel = self.server_sock.getsockname()[1]
	
	def listen(self):
		self.server_sock.listen(1)
		print("Listening for bluetooth connections")

	def advertiseServices(self):
		uuid = "00001101-0000-1000-8000-00805F9B34FB"
		advertise_service(self.server_sock, "MPDBTAdapter",
         service_id = uuid,
         service_classes = [ uuid, SERIAL_PORT_CLASS ],
         profiles = [ SERIAL_PORT_PROFILE ])
		print("Advertising services")

	def acceptClient(self):
		client_sock, client_info = self.server_sock.accept()

		print("Accepted connection from ", client_info)
		return BTClient(client_sock)
