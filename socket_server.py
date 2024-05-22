import socket
from machine import I2S, Pin
import network
import time

def wifi_connect(SSID, PASSWORD):
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        station.disconnect()
        while station.isconnected():
            pass
    print("WiFi 連線中...")
    station.active(True)
    station.connect(SSID, PASSWORD)
    while not station.isconnected():
        pass
    connected_ssid = station.config('essid')
    print(f"WiFi: {connected_ssid} 已連線")
    print('Network Config:', station.ifconfig())
    time.sleep(1)

wifi_connect("Wifi Name", "Wifi PassWord")

led = Pin(3, Pin.OUT)  # 選擇與燈泡連接的腳位

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

