from socket import *
import requests
import json

serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    speedTrap, clientAddress = serverSocket.recvfrom(2048)
    print(speedTrap)
    speedTrapDecoded = speedTrap.decode()
    print("Received message:" + speedTrapDecoded)
    speedTrapDe = json.loads(speedTrapDecoded)

    
    api_url = "https://speedtrapapi20230411142537.azurewebsites.net/api/SpeedTraps"
    request = requests.post(api_url, json=speedTrapDe)