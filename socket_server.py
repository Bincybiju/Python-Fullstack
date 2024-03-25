import socket
s=socket.socket()
s.bind(('localhost',9999))
s.listen()
print("Waiting for connection...")
while True:
    c,address=s.accept()
    name=c.recv(100).decode()
    print(name)
    print("connected with",address)
    c.send("Thankyou for connecting".encode())