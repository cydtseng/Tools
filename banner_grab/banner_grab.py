import socket

start_port = int(input("[*] Define starting port range:"))
end_port = int(input("[*] Define end port range:"))
ip = input('[*] Input ip address to scan:')

for i in range(start_port, end_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, i))
        print("[*] PORT {} is available. ".format(i), end="")
        msg = s.recv(2048).decode()
        sock.close()
    except:
        print("[*] PORT {} is invalid or unavailable.".format(i))
        pass
