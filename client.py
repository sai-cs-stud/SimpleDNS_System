import threading
import time
import random
import socket
import rs
from rs import root_server
from ts import top_server

def client():
    try:
        cli_rss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client RS socket created")
        cli_tss = None
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
    # List for request data
    hostreqs = []
    # Read in data from txt file
    with open("PROJI-HNS.txt") as txtdata:
        for line in txtdata:
            hostreqs.append(line)

    # Define port for rs socket
    port1 = 65000
    localhost_addr1 = socket.gethostbyname(socket.gethostname())

    # connect to servers on local(for now)
    server_binding1 = (localhost_addr1,port1)
    cli_rss.connect(server_binding1)

    while True:
        # Send and recieve here
        for req in hostreqs:
            cli_rss.send(req.encode('UTF-8'))
            #print("[C]: Requesting " + req)
            data_from_rs = "{}".format(cli_rss.recv(200).decode('UTF-8'))
            print("[C]: Recieved\n" + data_from_rs)
            dataline = data_from_rs.split()
            if dataline[2] == 'NS':
                try:
                    if cli_tss is None:
                        cli_tss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        print("[C]: Client TS socket created")
                         # Define port for ts socket
                        port2 = 12345
                        localhost_addr2 = socket.gethostbyname(socket.gethostname())

                        # connect to ts on local(for now)
                        server_binding2 = (localhost_addr2, port2)
                        cli_tss.connect(server_binding2)
                except socket.error as err:
                    print('socket open error: {} \n'.format(err))
                    exit()
                cli_tss.send(req.encode('UTF-8'))
                #print("[C]: Requesting " + req)
                data_from_ts = "{}".format(cli_tss.recv(200).decode('UTF-8'))
                print("[C]: Recieved\n" + data_from_ts)
        break
    # Close client sockets
    cli_tss.send('disconnect'.encode('UTF-8'))
    cli_tss.close()

    cli_rss.send('disconnect'.encode('UTF-8'))
    cli_rss.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='rs', target=root_server)
    t1.start()

    time.sleep(random.random() * 5)
    t3 = threading.Thread(name='ts', target=top_server)
    t3.start()

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    

    time.sleep(30)
    print("Done.")
