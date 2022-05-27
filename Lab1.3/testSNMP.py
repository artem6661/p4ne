from pysnmp.hlapi import *
from pysnmp.hlapi import UsmUserData

snmp_engine = SnmpEngine()
UsmUserData = UsmUserData(userName="monRO", authKey="ROmonVW!")
transport = UdpTransportTarget(("10.26.44.95", 161))
#context_data = ContextData()

#www = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
#eee = ObjectIdentity("1.3.6.1.2.1.2.2.1.2.1")

#result = getCmd(snmp_engine, UsmUserData, transport, context_data, ObjectType(snmp_system))
