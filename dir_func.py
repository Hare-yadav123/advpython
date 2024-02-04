'''dir() is inbuilt function in the python which return the list of  attributes and methods of the object(object means module ,class, function,list,dictionary,string)
'''
#print(str.__doc__)
# dir function
# python3 code to demonstrated dir()
#when no parametetr are passed
#1 note that we have no imported any module
'''print(dir())

import random
import math
import datetime
                # return the mudule names add to the locals namesspace
print(dir())'''

#2 when module object is passed as parameter 
import random
#print list which contain  names of attribute in random function
print(dir(random)) # module object is passed as parameter


#3 call dir with dictionary so they return the availabel all method in dict
a={}
b=[]
print("dict method or ",dir(a))
print("list attribute or method :",dir(b))

#4 creationb of simple class with __dir__ and demonstrated its working
class Super_market:
    def __dir__(self):
        return [" custemer name","product","quntity","price ","date"]
    
sup=Super_market()
print(dir(sup))

