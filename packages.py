# it has a collection of module 

import os
# shell scripting using python 
import shutil 
print(os.getcwd())
print(shutil.disk_usage("/"))

total, used, free = shutil.disk_usage("/")

print("total disk space is:", total // (2**30))
print("used disk space is :", used // (2**30))
print(" free space is : ",free // (2**30))

# F string 
print(f" total space is :{total // (2**30)} GB" )
