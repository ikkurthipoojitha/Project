import os
import re
filename=input("enter file name")
f=open(filename,'r')
for line in f:
     x=re.findall('\S+@\S',f)
     print(x)
     
