from socket import *
import os

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(("", 9000))

def send_info(client, file_name):
    f = open(file_name, "rb")
    data = f.read()
    f.close()
    udpSocket.sendto(data, client)

def send_info_plus(client, file_name):
    f = open(file_name, "rb")
    data = f.read()
    f.close()

    #-------------------------#
    #测试代码
    a = b''
    b = data
    #-------------------------#

    while len(data) > 1000:
        temp_data = data[:1000]
        data = data[1000:]
        temp_data = "$parFile$".encode() + temp_data
        #---------------------------#
        #测试代码
        a = a + temp_data[9:]
        #---------------------------#
        udpSocket.sendto(temp_data, client) # 发送部分数据
        # 接收客户端的信号
        udpSocket.recvfrom(1024)

    data = "$endFile$".encode() + data
    #-----------------------------#
    a = a + data[9:]
    print(a == b)
    #-----------------------------#
    udpSocket.sendto(data, client)
    udpSocket.recvfrom(1024)

if __name__ == '__main__':
    while True:
        recvData = udpSocket.recvfrom(1024)
        # 更新当前文件夹下的文件
        file_list = os.listdir(os.path.dirname(__file__))
        # 获取发送者的ip和端口
        adress = recvData[1]

        # 判断文件是否存在
        if recvData[0].decode("utf-8") in file_list:
            send_info_plus(adress, recvData[0].decode("utf-8"))
        else:
            # 文件不存在
            udpSocket.sendto("%notFile%".encode(), adress)
