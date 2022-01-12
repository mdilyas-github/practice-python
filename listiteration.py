devicelist=('1.1.1.1','2.2.2.2','3.3.3.3')
print(devicelist)

#o/p  ('1.1.1.1', '2.2.2.2', '3.3.3.3')

for ip in devicelist:
 print(ip)
 
 #o/p
 #1.1.1.1
# 2.2.2.2
# 3.3.3.3

#list of list
ios_device=('1.1.1.1', '2.2.2.2', '3.3.3.3')
nxos_devices=('1.1.1.1', '2.2.2.2', '3.3.3.3','4.4.4.4')
asa_devices=('100.1.1.1','20.2.2.2.','303.3.3.3')
all_devices=(ios_device,nxos_devices,asa_devices)

print(all_devices)

# (('1.1.1.1', '2.2.2.2', '3.3.3.3'), ('1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4'), ('100.1.1.1', '20.2.2.2.', '303.3.3.3'))

for ipadd in all_devices:
  print(ipadd)