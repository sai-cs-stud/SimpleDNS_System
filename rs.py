import socket
def root_server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # List for dns data(in tuple format)
    dnsrs = []
    # Read in data from txt file
    with open("/PROJI-DNSRS.txt") as txtdata:
        for line in txtdata:
            linetup = tuple(map(str, line.split(' ')))
            dnsrs.append(linetup)
    
    # recieve client msg
    data_from_client=csockid.recv(100)
    msg2 = "{}".format(data_from_client.decode('utf-8'))
    print("[S]: Data received from client: " + msg2)
    # send a intro message and reversed client msg to client  
    msg = "Welcome to CS 352!"
    #msg2 = reverse(msg2)
    csockid.send(msg.encode('utf-8'))
    #csockid.send(msg2.encode('utf-8'))
    # Close the server socket
    ss.close()
    exit()
    