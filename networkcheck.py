print("网站IP地址查看器")
print("Made by KevinXu")
print("")

slark = (1)
while(slark):
    print("本地网络检测，请选择检测内容：")
    print("1.本机主机名")
    print("2.本地IP地址")
    print("3.常用端口对应服务")
    print("4.查找主机名对应IP地址")
    print("5.查找IP对应的主机名")
    choice = input("请输入序号：")
    print("")
#用户选择

    import socket
    a = socket.gethostname()
    b = socket.gethostbyname(a)
    if choice == "1":
        print(a)
        print("")

    elif choice == "2":
        print(b)
        print("")

    elif choice == "3":
        while True:
            try:
                port = input("请输入端口号：")
                print(socket.getservbyport(int(port)))
                print("")
            except:
                print("此端口无对应服务")
                print("")

    elif choice == "4":
        while True:
            try:
                x = input("请输入您要查询域名：")
                y = socket.gethostbyname(x)
                print(y)
                print("")
            except:
                print("域名输入有误，请重新输入")
                print("")

    elif choice == "5":
        while True:
            try:
                ip = input("请输入IP地址：")
                print(socket.gethostbyaddr(str(ip)))
            except:
                print("无法找到此IP对应的主机名")
                print("")

    else:
        print("输入错误，请重新输入")
        print("")
