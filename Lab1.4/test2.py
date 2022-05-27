from ipaddress import IPv4Network
import random

class IPv4RN(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(p_start, p_end)),strict=False)

    def regular(self):
        return self.is_global and not \
                (self.is_multicast or self.is_link_local or \
                 self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)

net=random.randint(0x0b00000,0xdf00000)
print(net)


