import scapy.all as  scapy

def packet_callback(packet):
	if packet.haslayer(scapy.IP): #Check if the packet has Ip  Layer
	    ip_src= packet[scapy.IP].src
	    ip_dst = packet[scapy.IP].dst
	    protocol = packet[scapy.IP].proto
	    print(f"[*]{ip_src} -> {ip_dst} | Protocol: {protocol}") 

def sniff_network(interface, filter=None):
	print(f"[*] sniffing started on interface {interface}")
	scapy.sniff(iface=interface, filter=filter, prn=packet_callback)



interface = "eth0"

filter = None

sniff_network(interface, filter)
