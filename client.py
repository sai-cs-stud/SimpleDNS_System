import threading
import time
import random
import socket
import rs
from rs import root_server
def client():
    try:
        cli_rss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client RS socket created")
        cli_tss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client TS socket created")
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
    port1 = 50007
    localhost_addr1 = socket.gethostbyname(socket.gethostname())

    # Define port for ts socket
    port2 = 50008
    localhost_addr2 = socket.gethostbyname(socket.gethostname())

    # connect to servers on local(for now)
    server_binding1 = (localhost_addr1,port1)
    cli_rss.connect(server_binding1)

    server_binding2 = (localhost_addr2, port2)
    #cli_tss.connect(server_binding2)

    # Send and recieve here
    for req in hostreqs:

        cli_rss.send(req.encode('UTF-8'))
        print("[C]: Requesting " + req + "from [RS]")
        data_from_rs = cli_rss.recv(200)
        print("[RS]: {}".format(data_from_rs.decode('UTF-8')))


    # Close client sockets
    cli_rss.close()
    #cli_tss.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='rs', target=root_server)
    t1.start()

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")
