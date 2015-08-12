#!/usr/bin/python

from socketdelegate import SocketConnection

if __name__ == "__main__":
	connection = SocketConnection("0.0.0.0", 6600)
	print(connection.read())
	connection.close()
	pass	
