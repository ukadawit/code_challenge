'''
    There should be a script that listens to requests from clients and retrun
    the current location of the object
'''
# socket is needed to listen for http requests
from socket import *
import sys

sock = socket(AF_INET, SOCK_STREAM)
server_address = ('localhost', 12000)

sock.bind(server_address)
# Listen for incoming http requests
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        # Current location of the cube from bpy 
        currentLocation = bpy.data.scenes['Scene'].objects['Cube'].location
        #  foramated location in to json
        formatedLocation = '{x : '+currentLocation[0]+', y : '+currentLocation[1]+', z : '+currentLocation[2]+'} '  
        # send back the location information
        connection.sendall(formatedLocation.encode('utf-8'))
       
    finally:
        # Clean up the connection
        connection.close()
