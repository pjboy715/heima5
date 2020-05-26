import socket

if __name__ == '__main__':
    # 1.创建tcp客户端套接字
    # AF_INET：ipv4地址类型
    # SOCK_STREAM：tcp传输协议
    tcp_client_sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.和服务段套接字建立连接
    tcp_client_sockt.connect(('192.168.1.218', 9090))

    # 3.发送数据到服务端
    send_content = '你好，我是客户端小白！！'
    # 对字符串进程编码位二进制数据
    send_data = send_content.encode('gbk')

    # 3.发送数据到服务端
    tcp_client_sockt.send(send_data)

    # 4.接收服务端的数据
    # 1024:表示每次接收的最大字节数
    recv_data = tcp_client_sockt.recv(1024)
    # 对二进制数据进行解码
    recv_content = recv_data.decode('gbk')
    print('接收数据为：', recv_content)

    # 5.关闭套接字
    tcp_client_sockt.close()
