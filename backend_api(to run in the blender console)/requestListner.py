'''
    There should be a script that listens to requests from clients and retrun
    the current location of the object
'''
# socket is needed to listen for http requests
from socket import *

server_address = ('localhost', 12000)

socket.bind(server_address)

# Listen for incoming http requests
socket.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        while True:
            # Current location of the cube
            currentLocation = bpy.data.scenes['Scene'].objects['Cube'].location
            # foramated location in to json
            formatedLocation = {'x': currentLocation[0], 'y': currentLocation[1], 'z': currentLocation[2]}
            
            connection.sendall(formatedLocation)

    finally:
        # Clean up the connection
        connection.close()
