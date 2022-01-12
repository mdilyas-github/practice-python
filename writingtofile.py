import sys

#adding a string

mystring = "written by ilyas"


#opening file with write mode

myfile =  open("ilyas.txt",'w')   #creating a file in the same folder

#writing my string into the file

myfile.write(mystring)


#close the file
myfile.close()


#reading the file back
myfile = open("ilyas.txt",'r')  #open the file
filecontenet=myfile.read()   #read the file
print(filecontenet)   #print the file
myfile.close()  #close the file