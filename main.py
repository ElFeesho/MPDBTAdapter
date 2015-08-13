#!/usr/bin/python

from socketdelegate import SocketConnection
from btserver import BTServer
from btserver import BTClient

if __name__ == "__main__":
	connection = SocketConnection("0.0.0.0", 6600)
	print(connection.read())

	btserver = BTServer()
	btserver.listen()

	btserver.advertiseServices()

	while True:
		btclient = btserver.acceptClient()

		while True:
			readData = btclient.read()
			print("Read from bluetooth %s" % readData)
			connection.send(readData)
			response = connection.read()
			print("Read from network: %s" % response)
			btclient.send(response)

