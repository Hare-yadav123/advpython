from array import*
a=array("i",[1,5,5,5,5,9,9,8,7])
count={}
for j in a:
    if j in count:
        count[j]+=1
    else:
        count[j]=1
for key,value in count.items():
    print(key,"=",value)
    
    
data=[4,5,6,8,9,5,2,3,4,7,1,2,89,7,9,4]
count={}
for k in data:
    if k in count:
        count[k] +=1
    else:
        count[k] =1
for l , m in count.items():
    print(l,':',m)
    
