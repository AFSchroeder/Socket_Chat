import socket, sys, os
"""
This application uses low level socket connections to pass messages between
two terminals. It is a very simple applicaiton meant more for testing and
training, than for commercial use.

Developed by: B. Schroeder
Origin Date: 22 Mar 2016
Last Updated: 22 Mar 2016
"""

def server(port):
    """
    This is the server side of the chat application. It accepts only one
    parameter, port, and sets up a socket that accepts one connection. The
    server will 'listen' indefinitely for a connecction once it is initiated.
    """
    #This is representative of all availavle interfaces
    HOST = ''
    try:
        #This opens up a socket and binds it to the host and port specified
        #then waits for and accepts one connection
        sock_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_serv.bind((HOST, port))
        sock_serv.listen(1)
        print 'Waiting for connection on', port

    #All error handlers function in the same way throughout this application
    #the error is caught using socket.error and the error number and text
    #is printed on screen and the applicaiton is restarted.
    except socket.error as msg:
        print 'Error', msg[0], ':' + msg[1]
        reset()

    try:
        #Accepts the connection and prints the host name and address of client
        con, addr = sock_serv.accept()
        print 'Connected by', addr

    except socket.error as msg:
        print 'Error', msg[0], ':' + msg[1]
        reset()

    #This is an infinite loop to keep the connection open until an empty string
    #is sent or recieved
    while True:
        try:
            #This waits to recv a message from the client
            data = con.recv(1024)
            if data < 1: break
            print '<><<', data

        except socket.error as msg:
            print 'Error', msg[0], ':' + msg[1]
            reset()

        try:
            #This prompts the user to type a message and sends it to the client
            message = raw_input('<>>>')
            if message == "": break
            con.sendall(message)

        except socket.error as msg:
            print 'Error', msg[0], ':' + msg[1]
            reset()

    con.close()
    print 'Connection closed.'

def client(host, port):
    """
    This is the client side of the chat application. It accepts two parameters,
    host and port, then apptempts to connect to an already running server.
    """
    try:
        my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_sock.connect((host, port))
        print 'Connection successful.'

    except socket.error as msg:
        print 'Error', msg[0], ':' + msg[1]
        reset()

    #This is an infinite loop to keep the connection open until an empty string
    #sent or recieved.
    while True:
        try:
            #This prompts the user to type a message to send to the server
            message = raw_input('<>>>')
            if message == "": break
            my_sock.sendall(message)

        except socket.errror as msg:
            print 'Error', msg[0], ':' + msg[1]
            reset()

        try:
            #This waits to recv the incoming message from the server
            data = my_sock.recv(1024)
            if data < 1: break
            print '<><<', data
        except socket.error as msg:
            print 'Error', msg[0], ':' + msg[1]
            reset()

    my_sock.close()
    print 'Connection closed.'

def app_start():
    """
    This function is essentially the splash screen and runs only on the initial
    start up or the application.
    """

    os.system('cls')
    print """
Welcome to Socket Chat!

    """
    reset()

def reset():
    """
    This function gets all necessary parameters from the user. The user must
    enter the parameters exactly right or errors will result. The user must
    select either server or client mode, the enter the host (for client side)
    and an available port.
    """

    mode = raw_input('Choose server ("s") or client ("c") mode: ')
    host = raw_input('Enter hostname or IP: ')
    port = raw_input('Enter port number: ')

    if mode == 's':
        server(int(port))
    elif mode == 'c':
        client(host, int(port))
    else:
        pass

#Starts the application initially
app_start()
