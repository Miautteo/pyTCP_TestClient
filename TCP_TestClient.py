import socket as S

##Establish Socket
socket = S.socket(S.AF_INET, S.SOCK_STREAM)
socket.connect(('localhost', 11000))

##Define Data
Msg = "Hallo ü"
encoding = "utf-8"

##Send Data
SendData = bytes(Msg, encoding)
socket.send(SendData)

##Listen for response
recvData = socket.recv(1024)
recvMsg = recvData.decode(encoding)
print(recvMsg)

##close Connection
socket.close()