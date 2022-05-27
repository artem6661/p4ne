from pysnmp.hlapi import *
from pysnmp.hlapi import UsmUserData

snmp_engine = SnmpEngine()
UsmUserData = UsmUserData(userName="monRO", authKey="ROmonVW!")
transport = UdpTransportTarget(("10.26.44.95", 161))
context_data = ContextData()

snmp_system = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
snmp_interfaces = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")

#достаем snmp_system getCmd и snmp_interfaces nextCmd (чтобы глубоко не рыть при nextCmd - докидываем lexicographicMode=False)
result = getCmd(snmp_engine, UsmUserData, transport, context_data, ObjectType(snmp_system))
result2 = nextCmd(snmp_engine, UsmUserData, transport, context_data, ObjectType(snmp_interfaces), lexicographicMode=False)

#принтуем snmp_system
print("snmp_system")
for e in result:
    for a in e[3]:
        print(a)

#принтуем snmp_interfaces
print("snmp_interfaces")
for e in result2:
    for a in e[3]:
        print(a)
