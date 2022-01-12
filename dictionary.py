#define dictionary name person add key and value in it
person = {"name" : "ilyas"}

#adding item in the dectionary
person['education']='cisco'


print(person.keys())
print(person.values())
print(person.items())
   
   
   
for keyvalue in person.items():
      print(keyvalue[0],'\t',keyvalue[1])
	  
	  
	 #o/p name     ilyas
       #education        cisco
 