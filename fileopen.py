file = open("networkfile.txt","r")

#reding device information line by line from networkfile
networkadd = file.readline().strip()#raadline means read line by line, strip mean remove the spaces from output
ios = file.readline().strip()
subnetmask = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip() 


#printing the information
print ( "network:",networkadd)
print ("ios version:",ios)
print("subnet:", subnetmask)
print("username:",username)
print("password:",password)



#o/p with out strip()

#network: 10.0.0.0

#ios version 12.2
#


#o/p with strip()
#network: 10.0.0.0
#ios version 12.2
#
                  


