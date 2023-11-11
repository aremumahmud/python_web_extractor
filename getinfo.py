import socket

def readPage(page:str) :
    myreadSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try :
        myreadSocket.connect((page,80))
    except :
        print("could not connect to server or incorrect uri")
        exit()

    cmd = "GET http://"+page+"/ HTTP/1.0\n\n"
    cmd = cmd.encode()

    myreadSocket.send(cmd)

    pageData = ''

    while True :
        data = myreadSocket.recv(512)
        if len(data) < 1 : 
            break

        received = data.decode()
        pageData = pageData + received
    
    myreadSocket.close()

    return pageData



    
