import socket
def convertList(lis):
    str = ' '.join(lis)
    return str
def top_server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[TS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', 12345)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[TS]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[TS]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[TS]: Got a connection request from a client at {}".format(addr))

    while True:
        # List for dns data(in list format)
        dnsts = []
        # Read in data from txt file
        with open("PROJI-DNSTS.txt") as txtdata:
            for line in txtdata:
                lineList = line.split()
                dnsts.append(lineList)
    
        # recieve client msg
        data_from_client=csockid.recv(200)
        hnsreq = "{}".format(data_from_client.decode('UTF-8'))
        if str.strip(hnsreq) == 'disconnect':
            break
        print("[TS]: Processing request from client " + hnsreq)
    
        # Check if in dns (caps insensitive search)
        boolean = 0
        for lineList in dnsts:
            if lineList[0].lower() == str.strip(hnsreq.lower()):
                csockid.send(convertList(lineList).encode('UTF-8'))
                boolean = 1
        if boolean == 0:
            csockid.send(hnsreq + "- ERROR: HOST NOT FOUND".encode('UTF-8'))
        break
    # Close the server socket
    ss.close()
    exit()
    