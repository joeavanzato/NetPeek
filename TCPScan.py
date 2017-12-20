import socket
import argparse
import threading
import ftplib
import random
import time
import sys

mailfront = ["Zofia", "Test", "Jack", "Alehandro", "Vladimir", "Boston", "Loquisha", "Mahogany", "Ferrari"]
mailback = ["gmail.com", "yahoo.com", "hotmail.com"]

global flood_time
global target_host 
global target_Ports
target_host = ""
target_Ports = []
flood_time = 0
target_Ports.append("")

parser = argparse.ArgumentParser(usage = 'Host (-H) [TARGET-HOST], Ports for Scanning (-p) [TARGET-PORTS (ex. 21 125 80)], Anonymous FTP Login Query (-a) (No Args), UDP Flooding Enabled (-u 200) where 200 is total msgs sent')
parser.add_argument("-H", "--Host", help = 'Give Target Host!', required = True)
parser.add_argument("-p", "--ports", nargs = '+', help = 'Give Target Port!')
parser.add_argument("-a", "--Anon", action = 'store_true', help = 'Sets Anonymous FTP Query Mode')
parser.add_argument("-u", "--flood", nargs = 1, help = 'Flood Host with random UDP Datagrams')
args = parser.parse_args()

if (((target_Ports[0]) == "") and ((args.Anon) == False) and ((args.flood) == "")): #Must use at least one of these
    print("Missing Parameters!  Must use -u with some ports")
    print(parser.usage)
    exit(0)
elif ((target_Ports[0]) == "") and ((args.flood) == True):
    print("Must Select Ports for UDP Flooding with -p!")
    print(parser.usage)
    exit(0)
else:
    target_host = args.Host
    target_Ports = args.ports
    flood_time = args.flood

def flood_host(host, portlist, flood_time):
    count = 0
    for port in portlist:
        count = count + 1
        tname = 't-'+str(count)
        tname = threading.Thread(target = flood_port(host, port, flood_time))
        tname.start()

def flood_port(host, port, flood_time):
    current_count = 0
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    random_data = bytes(random._urandom(512))
    stop_time = int(time.time()) + flood_time
    while True:
        if ((stop_time) < (time.time())) or (current_count > 30): #Artificial Break
            break
        else:
            pass
        print("Datagram Sent")
        temp_socket.sendto(random_data, (host, port))
        current_count = current_count + 1

def query_Login(host):
    try:
        tmpftp = ftplib.FTP(host)
        tmpmail = random.choice(mailfront)+"@"+random.choice(mailback)
        print(tmpmail)
        tmpftp.login('anonymous', tmpmail)
        print(str(host)+" Succeeded Connecting via FTP")
        crawl(tmpftp)
        tmpftp.quit()
    except:
        print(str(host)+" Failed Connecting Via FTP")


def crawl(connection):
    backlist = []
    list = []
    try:
        list = connection.dir()
    except:
        print("Failed Retrieiving Default Directory Contents")
        pass
    #for file in list:
    #    name = file.lower()
    #    if ('.php' or '.html' or '.htm' or '.asp') in name:
    #       print("Appending "+name)
    #       backlist.append(name)
    return backlist


def Connect(target_host, target_port):
    try:
        current_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        current_socket.connect((target_host, target_port))
        print("Socket Connected to "+target_host+" on Port "+str(target_port))
        current_socket.send(b'Hello\r\n') #Payload
        feedback = current_socket.recv(100)
        print(str(feedback))
        current_socket.close()
    except socket.error:
        print("Error Connecting on Port "+str(target_port))

def Port_Scan(target_host, target_Ports):
    try:
        target_IP = gethostbyname(target_host)
    except:
        print("Error Resolving FQDN to IP!")
    try:
        target_Name = gethostbyaddr(target_IP)
        print(target_Name)
    except:
        print("Error Resolving Host name from IP!")
    lenport = len(target_Ports)
    x = 0
    for x in range(lenport):
        curport = target_Ports[x]
        print(curport)
        x = x + 1
        print("Scanning Port "+str(curport))
        tconnect = threading.Thread(target = Connect(target_host, int(curport)))
        tconnect.start()

def main():
    print("")
    if ((flood_time) != 0):
        tflood = threading.Thread(target = flood_host(target_host, target_Ports, flood_time))
        tflood.start()
    else:
        pass
    if (args.Anon == True):
        tlogin = threading.Thread(target = query_Login(target_host))
        tlogin = t3.start()
    else:
        pass
    if ((target_Ports) != ""):
        tscan = threading.Thread(target = Port_Scan(target_host, target_Ports))
        tscan.start()
    else:
        pass
    print("All Done")
main()
