import threading
import time
import random
import socket

def client():
    try:
        cli_rss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client RS socket created")
        cli_tss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client TS socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
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
    cli_tss.connect(server_binding2)

    # Send and recieve here


    # Close client sockets
    cli_rss.close()
    cli_tss.close()
    exit()

if __name__ == "__main__":

    print("Done.")
