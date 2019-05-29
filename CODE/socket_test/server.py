from socket import *
import os
import datetime

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(("", 5925))

def send_file_plus(client, file_name):
    f = open("Repository/"+file_name, "rb")
    data = f.read()
    f.close()
    while len(data) > 1000:
        temp_data = data[:1000]
        data = data[1000:]
        udpSocket.sendto(temp_data, client) # 发送部分数据
        # 接收客户端的信号
        udpSocket.recvfrom(1024)
    udpSocket.sendto(data, client)
    udpSocket.recvfrom(1024)
    udpSocket.sendto("$hyk$".encode(), client)

def main():
    while True:
        recvData = udpSocket.recvfrom(1024)

        # 更新当前文件夹下的文件
        # file_list = os.listdir(os.path.dirname(__file__) + "/Repository")
        # 在终端运行时使用这个
        file_list = os.listdir(os.path.dirname(__file__) + "Repository")

        # 获取发送者的ip和端口
        adress = recvData[1]

        # 日志
        now = datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')
        print_log = "一个客户端已经连接,时间为%s,地址为(%s),请求文件为:%s" % (now, str(adress[0])+":"+str(adress[1]), recvData[0].decode())
        print(print_log)
        log = now+"|"+str(adress[0])+":"+str(adress[1])+"|"+recvData[0].decode()+"\n"
        with open("log.txt", "a") as f:
            f.write(log)

        # 判断文件是否存在
        if recvData[0].decode() in file_list:
            send_file_plus(adress, recvData[0].decode("utf-8"))
        else:
            # 文件不存在
            udpSocket.sendto("%notFile%".encode(), adress)

if __name__ == '__main__':
    main()
