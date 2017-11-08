import socket
import tdl
import threading
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set rendered font
tdl.setFont('assets/arial_16x16.png')

# Create console window
window = tdl.init(50, 30, "Network Client")

def listener():
	global window
	recvSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	recvSock.bind(("127.0.0.1", 5006))
	recvSock.setblocking(0)
	while (1):
		dataIn = None
		try:
			dataIn = recvSock.recv(10000).decode('utf-8')
		except:
			pass
			
		if dataIn != None:
			window.clear()
			data = json.loads(dataIn)
			for entity in data["entities"]:
				window.drawChar(entity["x"], entity["y"], entity["char"])
			tdl.flush()

t = threading.Thread(target=listener)
t.start()

while (1):
	for event in tdl.event.get():
		if event.type == 'KEYDOWN':
			if event.keychar != 'TEXT':
				msgBytes = "{0}~{1}".format("KEYDOWN", event.keychar).encode('utf-8')
				sock.sendto(msgBytes, (UDP_IP, UDP_PORT))
		elif event.type == 'KEYUP':
			if event.keychar != 'TEXT':
				msgBytes = "{0}~{1}".format("KEYUP", event.keychar).encode('utf-8')
				sock.sendto(msgBytes, (UDP_IP, UDP_PORT))

