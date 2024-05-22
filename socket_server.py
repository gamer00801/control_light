import socket
from model1 import *
from machine import I2S, Pin



wifi_connect("FLAG", "0233110330")

led = Pin(3, Pin.OUT)  # 假設使用 GPIO3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

print('Server Listening')

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    if '/on' in request:
        led.value(1)
    elif '/off' in request:
        led.value(0)
    response = 'HTTP/1.1 200 OK\n\n'
    conn.send(response)
    conn.close()

