#!/usr/bin/python3
#Simple Python Netcat Client
import threading
import socket
import pty
import sys

def recv_data(s):
    while True:
        print(s.recv(1024).decode('utf-8').rstrip(), end='')

def connect_to_host(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.settimeout(0.6)
    s.connect((str(host), int(port)))
    result = s.recv(1024).decode('utf-8')
    if "Windows PowerShell" in result:
        s.settimeout(None)
        print(result, end='')
        receiver = threading.Thread(target=recv_data, args=[s])
        receiver.daemon = True
        receiver.start()
        while True:
            s.send((input('')).encode('ascii'))

if __name__ == "__main__":
    connect_to_host(sys.argv[1], sys.argv[2])
