#Use the programme as
#python myclient.py ip_Address_of_Server_in_xx.xx.xx.xx_format

import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#create a socket
ip_address = "192.168.1.10"  #sys.argv[1]
port_number = 7
s.connect((ip_address,port_number))
#Go to an infinite loop
while 1:
    try:
        #Ask the user to enter some message through keyboard
        message = input("Client:")
        if message == 'quit':
            break
        #If the user enters "quit", quit the programme,
        #otherwise send the data entered by the user to 
        #the client
        with open('lena_gray.raw', 'rb') as f:
            imgData = bytearray(f.read())
        #print("File Size",len(imgData))
        sentSize=0
        s.sendall(imgData)#.encode()
        print("Sent image data")
        recvDataSize=0
        f = open('lena_nagative.raw','wb')
        while recvDataSize < 512*512:
            recvData = s.recv(8192)
            recvDataSize += len(recvData)
            #print("Total Data received",len(recvData))            
            f.write(recvData)
        f.close()
        #Print the received data on the screen
        print("Processed image received")

    except Exception as e: #If any exception happens during send the data
        print(e)
        s.close() #the programme
        print("Error Connection lost")
        break