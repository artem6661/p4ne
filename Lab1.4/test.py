class Subnet:
    def __init__(self, n,p):
        self.network=n
        self.prefix=p
    def __str__(self):
        return self.network + self.prefix
    def __repr__(self):
        return self.network + self.prefix
    def getnet(self):
        return self.network
    def getprefix(self):
        return self.prefix

n1=Subnet('192.168.1.0','/24')
n2=Subnet('172.16.0.0','/16')

L = [n1,n2]


class A_P_E(Subnet):
    def __init__(self, n, p, gw):
        Subnet. __init__(self,n,p)
        self.gateway=gw
    def getgw(self):
        return self.gateway

ap = A_P_E('192.168.5.0', '/24', "192.168.1.1")
print(ap)