import socket

if __name__ == '__main__':
    # 1.创建服务端端套接字对象
    # AF_INET：ipv4地址类型
    # SOCK_STREAM：tcp传输协议
    tcp_server_sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用,服务端程序退出后端口号立即释放
    # SOCK_STREAM：表示当前套接字
    # SO_REUSEADDR：表示复用端口号的选项
    tcp_server_sockt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2.绑定端口号
    # bind第一个参数表示IP，通常不指定，即为本机任意IP；第二个参数为端口号
    tcp_server_sockt.bind(('', 19099))

    # 3.设置监听
    # 128:表示最大等待建立连接数量
    tcp_server_sockt.listen(128)

    # 4.等待接受客户端的连接请求
    # 注意点：每次当客户端和服务端建立连接成功都会返回一个新的套接字
    # tcp_server_sockt只负责等待接收客户端的连接请求，收发消息不使用该套接字
    new_client, ip_port = tcp_server_sockt.accept()
    print('客户端IP与端口号为：', ip_port)

    # 5.接收数据
    recv_data = new_client.recv(1024)
    print('接受的数据长度是：', len(recv_data))
    recv_data.decode('gbk')
    print('接受客户端的数据为：', recv_data)

    # 6.发送数据
    send_content = '问题正在处理中'
    # 对字符串编码
    send_data = send_content.encode('gbk')
    new_client.send(send_data)
    # 关闭客户端套接字，表示和客户端终止通信
    new_client.close()

    # 7.关闭服务端套接字，表示服务端以后不再等待接收客户端连接请求
    tcp_server_sockt.close()
