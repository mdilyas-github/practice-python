#no value of addding empty tuple because it cannot modified

my_typle =()


#cerate type deviceinfo holding ip username and pass
deviceinfo=('1.1.1.1','username','password')



#create set

dev_os_types = {'ios','catos','nxos'}

#can it take duplicates
dev_os_types = {'ios','catos','nxox','ios'}  #o/p  {'catos', 'ios', 'nxox'}

#addding
 dev_os_types.add("csr")
 
 #update
 dev_os_types.update(['csr1'])


#remove
# dev_os_types.remove['csr']


print(dev_os_types)



