from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    string = input("请输入语句：")

    udpSocket.sendto(string.encode("utf-8"), ("192.168.43.133", 7892))

