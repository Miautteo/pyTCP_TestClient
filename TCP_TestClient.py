import socket as S

##Establish variables:
Address = "2a02:908:f10:b440:"
Port = 11000
encoding = "utf-8"


try:
    ##Establish Socket
    socket = S.socket(S.AF_INET6, S.SOCK_STREAM, 0)
    socket.connect((Address, Port, 0, 0))

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

except Exception as e:
    print(f'Fehler beim verbinden: {e}')