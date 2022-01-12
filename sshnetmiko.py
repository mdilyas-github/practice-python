import netmiko






ip_address='172.28.8.31'
username = 'admin'
password = ""                  #password



#dir(netmiko)

connection=netmiko.ConnectHandler(ip=ip_address,device_type="cisco_ios",username=username,password=password)

#dir(connection)

print(connection.send_command("show ip int brief"))
print(connection.send_command("show ver"))



#//trying to copy the output and save in a file  (still testing)

op=print(connection.send_command("show ver"))     
myfile=open('ilyasssh.txt','w')
myfile.write(op)  

connection.disconnect() #to disconnect