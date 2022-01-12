switch = " catalyst 3850"

if "catalyst" in switch:
   switch_type = "catalyst"
elif "nexus" in switch:
   switch_type = "nexus"
else:
   switch_type = "unknown"
print (switch_type)   
   