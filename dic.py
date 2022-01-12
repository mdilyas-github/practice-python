from pprint import pprint

#simple empty list and uses


devicesa={}

devices={'ip':'11.11.1.1','version':'15.1','username':'ilyas'}

print(devicesa)  #empty list  o/p {}
print(devices)  #list of devices o/p {'ip': '11.11.1.1', 'version': 15.1, 'username': 'ilyas'}


#assign not real copy only pointing to it
devicesc=devices

print(devicesc)  #o/p {'ip': '11.11.1.1', 'version': 15.1, 'username': 'ilyas'}
pprint(devicesc)  #o/p from pprint  {'ip': '11.11.1.1', 'username': 'ilyas', 'version': 15.1}

#shallow copy  (it will copy devices to devx memory
devx=devices.copy()

pprint(devx)   #o/p {'ip': '11.11.1.1', 'username': 'ilyas', 'version': 15.1}

devx['version']='1.1' #modify the version values
pprint(devx)   

print(devices)