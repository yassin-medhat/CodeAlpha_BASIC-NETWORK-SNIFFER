This project, as the name suggests, is a basic network packet sniffer designed to capture connections made 
on a specified network interface.


You can also specify filters like TCP to capture only the TCP connections.

HOW IT WORKS:

First, I imported the Scapy library. (Scapy is a powerful interactive packet manipulation library written in Python.)

Then, I created a function to store and print the connection details (packet_callback).

After that, another function is defined to start sniffing when the script is executed. This function prints a start message, 
defines the network interface and filter (if specified), and then calls the packet_callback function to print the connection details.

How to Run It:

Command: python3 execute.py (Sometimes it will ask you for root permission; in that case, use sudo).
