import socket
port = 8081
host=input("Enter Server to connect: ")
#to=input("enter ip to connect: ")
name=input("Your handler name: ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost",8082))

while True:
    msg=input("Say something to server::  ")
    msg=bytes(name+" says:: "+msg,("UTF-8"))   #cannot send data directly thats why convert to byte
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.sendto(msg,(host, port))
    data,addr=s.recvfrom(1024)
    print (data,"from" ,addr)
    
    
    
    
    
