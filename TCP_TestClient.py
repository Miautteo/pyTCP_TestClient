import socket as S

##Establish variables:
#Address = "192.168.178.58"
Address = ""
Port = 11000
encoding = "utf-8"

##Establish Socket
socket = S.socket(S.AF_INET6, S.SOCK_STREAM)
socket.connect((Address, Port))

##Define Data
Msg = "Hallo ü"

##Send Data
SendData = bytes(Msg, encoding)
socket.send(SendData)

##Listen for response
recvData = socket.recv(1024)
recvMsg = recvData.decode(encoding)
print(recvMsg)

##close Connection
socket.close()