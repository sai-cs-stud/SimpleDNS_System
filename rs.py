import socket
def convertList(lis):
    str = ' '.join(lis)
    return str
def root_server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[RS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[RS]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[RS]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[RS]: Got a connection request from a client at {}".format(addr))
    while True:
        # List for dns data(in list format)
        dnsrs = []
        # Read in data from txt file
        with open("PROJI-DNSRS.txt") as txtdata:
            for line in txtdata:
                lineList = line.split()
                dnsrs.append(lineList)
    
        # recieve client msg
        data_from_client=csockid.recv(200)
        hnsreq = "{}".format(data_from_client.decode('UTF-8'))
        if str.strip(hnsreq) == 'disconnect':
            break
        print("[RS]: Processing request from client " + hnsreq)
    
        # Check if in dns (caps insensitive search)
        boolean = 0
        ns_str = ''
        for lineList in dnsrs:
            if lineList[2] == 'NS':
                ns_str = convertList(lineList)
            if lineList[0].lower() == str.strip(hnsreq.lower()):
                csockid.send(convertList(lineList).encode('UTF-8'))
                #print("[RS]: Data sent to client")
                boolean = 1
                break
        if boolean == 0:
            csockid.send(ns_str.encode('UTF-8'))
            #print("[RS]: Data sent to client")
    # Close the server socket
    ss.close()
    exit()
    
