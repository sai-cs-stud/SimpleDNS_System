import socket
import sys

tsListenPort = int(sys.argv[1])
def convertList(lis):
    str = ' '.join(lis)
    return str
def top_server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[TS2]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', tsListenPort)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[TS2]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[TS2]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[TS2]: Got a connection request at {}".format(addr))

    while True:
        # List for dns data(in list format)
        dnsts = []
        # Read in data from txt file
        with open("PROJ2-DNSTS2.txt") as txtdata:
            for line in txtdata:
                lineList = line.split()
                dnsts.append(lineList)
    
        # recieve LS msg
        data_from_LS=csockid.recv(200)
        while data_from_LS:
            hnsreq = "{}".format(data_from_LS.decode('UTF-8'))
            if str.strip(hnsreq) == 'disconnect':
                break
            print("[TS2]: Processing request from LS-" + str.strip(hnsreq))
            #print(dnsts)
            # Check if in dns (caps insensitive search)

            for lineList in dnsts:
                if lineList[0].lower() == str.strip(hnsreq.lower()):
                    csockid.send(convertList(lineList).encode('UTF-8'))
            data_from_LS=csockid.recv(200)
        break
    # Close the server socket
    ss.close()
    exit()
if __name__ == "__main__":
    top_server()