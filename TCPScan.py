import socket
import argparse
import threading
import ftplib
import random

mailfront = ["Zofia", "Test", "Jack", "Alehandro", "Vladimir", "Boston", "Loquisha", "Mahogany", "Ferrari"]
mailback = ["gmail.com", "yahoo.com", "hotmail.com"]

global target_host 
global target_Ports
target_ports = []


parser = argparse.ArgumentParser(usage = 'Host (-H) [TARGET-HOST], -ports (-p) [TARGET-PORTS (ex. 21 125 80)], -Anonymous FTP Query (-a), Must use -p with args or -a')
parser.add_argument("-H", "--Host", help = 'Give Target Host!', default = "", required = True)
parser.add_argument("-p", "--ports", nargs = '+', help = 'Give Target Port!', default = "")
parser.add_argument("-a", "--Anon", action = 'store_true', help = 'Sets Anonymous FTP Query Mode')
args = parser.parse_args()
if (str(args.ports) == "") and ((args.Anon) == False): #Must use one of these
    print(parser.usage)
    exit(0)
else:
    target_host = args.Host
    target_Ports = args.ports


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
        return
    #for file in list:
    #    name = file.lower()
    #    if ('.php' or '.html' or '.htm' or '.asp') in name:
    #       print("Appending "+name)
    #       backlist.append(name)
    return backlist


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
        t1 = threading.Thread(target = Connect(target_host, int(curport)))
        t1.start()

def main():
    print("")
    if ((target_Ports) != ""):
        Port_Scan(target_host, target_Ports)
    if (args.Anon == True):
        query_Login(target_host)
    print("All Done")
main()
