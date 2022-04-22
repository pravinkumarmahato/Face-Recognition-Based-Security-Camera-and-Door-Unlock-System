import time
import socket
import threading
#import RPi.GPIO as GPIO

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9090
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at", socket_address)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)

def show_client():
    try:
        client_socket, addr = server_socket.accept()
        print('CLIENT {} CONNECTED!'.format(addr))
        if client_socket:  # if a client socket exists
            data = client_socket.recv(1024)
            print(data)
            if data.decode("utf-8") == '1':
                print('value is equal to 1')
                #GPIO.output(3, True)
                #time.sleep(5)
                #GPIO.output(3, False)
            else:
                print('value is not equal to 1')
    except Exception as e:
        print(f"CLINET {addr} DISCONNECTED")
        pass


while True:
    show_client()
