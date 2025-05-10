import socket                                              #to communicate with other machines using TCP & UDP protocols
import termcolor

def scan(target, ports):
    for port in range(1,ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()  # initiating socket object which helps to connect with internet using TCP or UDP
        sock.connect((ipaddress, port))
        print("[+] PORT OPENED :) " + str(port))
        sock.close()

    except:
        print("[-] PORT CLOSED :( " + str(port))

targets = input("[*] Enter Targets To Scan(split them by , ): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)

else:
    scan(targets, ports)

