import socket
def convertTuple(tup):
    str = ' '.join(tup)
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

    # List for dns data(in tuple format)
    dnsrs = []
    # Read in data from txt file
    with open("PROJI-DNSRS.txt") as txtdata:
        for line in txtdata:
            linetup = tuple(map(str, line.split(' ')))
            dnsrs.append(linetup)
    
    # recieve client msg
    data_from_client=csockid.recv(200)
    hnsreq = "{}".format(data_from_client.decode('UTF-8'))
    print("[RS]: Data received from client: " + hnsreq)
    
    # Check if in dns (caps insensitive search)
    boolean = 0
    ns_tup = {}
    for linetup in dnsrs:
        if linetup[2] == 'NS':
            ns_tup = linetup
        if linetup[0].lower() == hnsreq.lower():
            csockid.send(convertTuple(linetup).encode('UTF-8'))
            boolean = 1
    if boolean == 0:
        csockid.send(convertTuple(ns_tup).encode('UTF-8'))
    
    # Close the server socket
    ss.close()
    exit()
    
