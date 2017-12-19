import socket
import argparse
import threading

global target_host 
global target_port
target_ports = []

parser = argparse.ArgumentParser(usage = '-Host <TARGET-HOST> -ports <TARGET-PORT>')
parser.add_argument("-H", "--Host", help = 'Give Target Host!', default = "")
parser.add_argument("-p", "--ports", nargs = '+', help = 'Give Target Port!', default = "")
args = parser.parse_args()
if ((str(args.Host) == "") or (str(args.ports) == "")):
    print(parser.usage)
    exit(0)
else:
    target_host = args.Host
    target_ports = args.ports


def Connect(target_host, target_port):
    try:
        cursock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cursock.connect((target_host, target_port))
        print("Socket Connected to "+target_host+" on Port "+str(target_port))
        cursock.send(b'Hello\r\n') #Payload
        feedback = cursock.recv(100)
        print(str(feedback))
        cursock.close()
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
        t1 = Thread(target = Connect(), args = (target_host, int(curport)))
        t1.start()

def main():
    print("")
    Port_Scan(target_host, target_ports)
main()