This project, as the name suggests, is a basic network packet sniffer designed to capture connections made 
on a specified network interface.

You can also speceifes filters like TCP to capture only the tcp connection.

HOW IT WORKS :

  .First, I imported the scapy laibrary.
(Scapy is a powerful interactive packet manipulation library written in Python.)

  .Then, I created a function to store and print the connection detailes.(Packet_callback)

  .After that, Another function  is defined to start sniffing when the script is executed. This function 
     prints a start message, defines the network interface and filter (if specified), and then calls 
     the packet_callback function to print the connection details.

How to run it:
  .command# python3 excute.py (Some times it will ask you for root permission, solution use "sudo")  
