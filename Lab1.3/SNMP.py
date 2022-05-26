from pysnmp.hlapi import *

snmp_engine = SnmpEngine()
UsmUserData = UsmUserData(userName="monRO", authKey="ROmonVW!", authProtocol="md5", mpModel=3)
transport = UdpTransportTarget(("10.26.44.95", 161))
context_data = ContextData()

snmp_system = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
snmp_interfaces = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")

result = getCmd(snmp_engine, UsmUserData, transport, context_data, ObjectType(snmp_system))

type(result)
"class>" "generator"
for i in result:
    for j in i[3]:
        print(j)
