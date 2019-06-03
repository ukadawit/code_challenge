'''
  There should be an http request listner that accepts requests from clients and 
  responds with the location of the object in blender.
  the current location of the object is held by variable  'currentLocation' which 
  gets the location vector from 'bpy' object
'''
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class BlenderLocationRequestListner(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')

        self.send_header("Access-Control-Allow-Origin", "*")

        self.end_headers()
 
       # Current location of the cube from bpy 
        currentLocation = bpy.data.scenes['Scene'].objects['Cube'].location
        #  foramated location in to json
        formatedLocation = '{"x" : '+str(currentLocation[0])+', "y" : '+str(currentLocation[1])+', "z" : '+str(currentLocation[2])+'} '  
       
        self.wfile.write(bytes(formatedLocation, "utf8"))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  server_address = ('localhost', 12000)
  httpd = HTTPServer(server_address, BlenderLocationRequestListner)
  print('running server...')
  httpd.serve_forever()
 
 
run()