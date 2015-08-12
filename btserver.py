#!/usr/bin/python

from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service(server_sock, "MPDBTAdapter",
                  service_id = uuid,
                  service_classes = [ uuid, SERIAL_PORT_CLASS ],
                  profiles = [ SERIAL_PORT_PROFILE ])
