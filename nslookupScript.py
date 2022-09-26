import socket
from turtle import forward

#takes a column of ips, like extracted from a csv and pasted to a text file, and finds and returns the PTR record for that IP.
def nslookup(ips):
    ips = open(ips,"r")
    results = []

    for line in ips:
        i=0
        results.append(line.rstrip('\n'))

    results = set(results)
    for ip in results:
        try:
            forwardDNS = open("forwardDNS.txt","a")
            forwardDNS.write(socket.gethostbyaddr(ip))
            forwardDNS.close()
        except:
            None,None,None

ips=input("Please enter filename of ips to resolve: ")
nslookup(ips)
