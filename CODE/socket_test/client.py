from socket import *
import time
import os

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(("", 8888))

# 先向服务器发送请求
def ask_file(server):
    file_name = input("请输入文件名:")
    udpSocket.sendto(file_name.encode(), server)
    recvData = udpSocket.recvfrom(1024)
    data = recvData[0]

    if data == b"%notFile%":  # 判断是否存在该文件
        print("文件不存在")
    else:
        # 写入文件
        file_path = "Recv/" + file_name  # 写进Recv文件夹下
        start = time.time()
        while True:
            if data == b"$hyk$":
                break  # 退出循环
            with open(file_path, "ab") as f:
                f.write(data)
            udpSocket.sendto("stop".encode(), server)

            # 接收新的一轮数据
            data = udpSocket.recvfrom(1024)[0]
        end = time.time()
        print("文件已经存进Recv文件夹下,耗时%.2f" % (end-start))

if __name__ == '__main__':
    if not os.path.exists("Recv"):
        os.mkdir("Recv")
    server = ("192.168.2.183", 5925)   # 服务器的ip和端口
    ask_file(server)
