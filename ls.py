import socket
import sys

lsListenPort = int(sys.argv[1])
ts1HostName = sys.argv[2]
ts1ListenPort = int(sys.argv[3])
ts2HostName = sys.argv[4]
ts2ListenPort = int(sys.argv[5])

def convertList(lis):
    str = ' '.join(lis)
    return str
def root_server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[LS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', lsListenPort)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[LS]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[LS]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[LS]: Got a connection request from a client at {}".format(addr))

    while True:
        # recieve client msg
        data_from_client=csockid.recv(200)
        hnsreq = "{}".format(data_from_client.decode('UTF-8'))
        print("\n[LS]: Processing request from client-" + str.strip(hnsreq))
        if str.strip(hnsreq) == 'disconnect':
            #do more stuff then break!!!
            break

        # Connect to TS Servers
        try:
            ls_ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ls_ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Define port for ts sockets
            port1 = ts1ListenPort
            localhost_addr1 = socket.gethostbyname(socket.gethostname())
            port2 = ts1ListenPort
            localhost_addr2 = socket.gethostbyname(socket.gethostname())
            # connect to ts on local
            server_binding_ts1 = (ts1HostName, port1)
            ls_ts1.connect(server_binding_ts1)
            server_binding_ts2 = (ts2HostName, port2)
            ls_ts2.connect(server_binding_ts2)
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()

        # forward message to TS1 and TS2
        ls_ts1.send(data_from_client)
        ls_ts2.send(data_from_client)
        print("[LS]: Data forwarded to TS1 and TS2")
        
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
if __name__ == "__main__":
    root_server()