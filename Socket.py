import os  
import http.server       #to install python additional packages
import socketserver     #to include additional sockets packages

port = 4000;

#Creating a server
Server = http.server.SimpleHTTPRequestHandler   #i am creating a server handler

#creating a sockert server
requests = socketserver.TCPSever(("",port), Server)

#printing a welcome a  message
print("Server up runnig forever: ", port);


requests.serve_forever()
