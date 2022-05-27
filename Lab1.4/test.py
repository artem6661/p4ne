class Subnet:
    def __init__(self, n='0.0.0.0',p='/0'):
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
n3=Subnet()

L = [n1,n2]

print(L)

print(n1)
