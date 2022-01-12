import sys

#create empty list
device_detail=[]


#open a file with read mode
myfile= open("device.txt",'r')

#reading single line and strip
myfile_line=myfile.readline().strip()


print("reading line")

 #adding comma sepreation string list into the list
device_detail=myfile_line.split(',')

print(device_detail)
#closefile
myfile.close()

#o/p  ['1.1.1.1', 'user', 'password', '']