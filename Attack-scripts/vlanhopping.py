from scapy.all import *

packet = Ether(dst="ff:ff:ff:ff:ff:ff")/\
        IP(src="192.168.40.1",dst="172.16.50.1")/\
        Dot1Q(vlan=30)/\
        Dot1Q(vlan=40)/\
        Dot1Q(vlan=40)/\
        ICMP()

packet.show()
sendp(packet)
