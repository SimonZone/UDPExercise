from socket import *
import random
import json
from time import sleep
    
serverName = '255.255.255.255'
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

sender = "SS Speedtrap"
while True:
    speed = random.randint(53, 80)

    speedInfo = {"sensorName": sender, "speed": speed}
    speedInfoJson = json.dumps(speedInfo)

    clientSocket.sendto(speedInfoJson.encode(), (serverName, serverPort))
    print("send file")
    print(speed)
    sleep(random.randint(3, 10))
    
