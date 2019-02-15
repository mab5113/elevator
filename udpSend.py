http://www.ironpython.info/index.php?title=Sending_Udp_Packets

from System.Net import IPAddress
from System.Net.Sockets import UdpClient
from System.Text import Encoding


class UdpSender(object):
    def __init__(self, port, ipAddress):
        self.client = UdpClient(0)
 
        # Only set this if you want to be able to listen
        # on the same machine
        self.client.MulticastLoopback = True

        # No *need* to parse - you can pass in a string
        addr = IPAddress.Parse(ipAddress)

        # Connecting means that you don't have to specify
        # The IP address when we call send.
        # For Udp, connecting isn't a requirement though
        self.client.Connect(addr, port)


    def send(self, message):
        bytearr = Encoding.UTF8.GetBytes(message)
        self.client.Send(bytearr, bytearr.Length)

port = 5555
group = "230.29.35.5"

udpSender = UdpSender(port, group)
udpSender.send("Some text")