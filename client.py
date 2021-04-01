import threading
import time
import random
import socket
#import rs
#from rs import root_server
#from ts import top_server
import sys

lsHostname = sys.argv[1]
lsListenPort = int(sys.argv[2])
#tsListenPort = int(sys.argv[3])


def client():
    try:
        cli_lss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client RS socket created")
        #cli_tss = None
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
    # List for request data
    hostreqs = []
    # Read in data from txt file
    with open("PROJ2-HNS.txt") as txtdata:
        for line in txtdata:
            hostreqs.append(line)
    
    # Define port for rs socket
    port1 = lsListenPort
    #localhost_addr1 = socket.gethostbyname(socket.gethostname())

    # connect to servers on local(for now)
    server_binding1 = (lsHostname,port1)
    cli_lss.connect(server_binding1)
    # Open resolved and clear
    f = open("RESOLVED.txt", "r+")
    f.seek(0)
    f.truncate()

    while True:
        # Send and recieve here
        for req in hostreqs:
            cli_lss.send(req.encode('UTF-8'))
            #print("[C]: Requesting " + req)
            data_from_ls = "{}".format(cli_lss.recv(200).decode('UTF-8'))
            print("[C]: Recieved\n" + data_from_ls)
            dataline = data_from_ls.split()
            f.write(data_from_ls+"\n")
        break

    f.close()
    # Close client sockets
    cli_lss.send('disconnect'.encode('UTF-8'))
    cli_lss.close()
    exit()

if __name__ == "__main__":
    client()
    print("Done.")
