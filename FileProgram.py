#Python program to read the content of a file

# a=str(input("enter the name of the file with .txt extension"))
# file2=open(a,"r")
# line=file.readline()
# while line !=" ":
#     print(line)
#     line=file.readline()
    
#1 file2.close()
#write the file
'''f=open("MyDemo.txt","a")
f.write("hello ward")
f.close()
#Read the file
f=open('MyDemo.txt','r')
print(f.read())

#2
d=open("file.txt","a")
d.write("ram aam khata hai")
d.close()

d=open("file.txt",'r')
print(d.read())'''

#3
# s=open("gh.txt",'a')
# s.write("who are you")
# s.close()

#readline method
'''s=open("MyFile.txt",'r')
print(s.readline())
print(s.readline())'''

#Remove file
# import os
# os.remove("file.txt")

#EX-5
'''a=open("MyDemo.txt","r")
for x in a:
    print(x)'''


#6    
'''fname=input("enter youe file nsme")  
with open(fname,"r")as f:

     for line in f:
    
        w=line.split()
        print(w)
        for i in w:
            for l in i:
                if(l.isdigit()):
                    print(l)'''
                
#7 add two file 
'''f1=input("enter your file name")
f2=input("enter your file for append")
D=open(f1,"r")
Data=D.read()
D.close()

D2=open(f2,"a")
D2.write(Data)
D2.close()'''

#count space 
'''Name=input("enter file name")
k=0
with open(Name,"r")as f:
    for i in f:
        d=i.split()
        for l in d:
            for s in l:
                if (s.isspace):
                    k=k+1
        
print("total space=",k)'''

# Name=input("enter file name")
# with open(Name,"r")as f:
#     for i in f:
#         a=i.title()
#         print(a)

l=[8,9]                                           
li=[4,5,6,'haree']
li.append(2)
print(li)
li.pop(0)
print(li)
li.insert(1,200)
print(li)
li[0]=10
print(li)

t=(70,20)
tu=(4,5,6,6,6)
print(t+tu)
print(tu)
print(len(tu))
# tu[0]=5
# print(tu)
a=tu.count(6)
print(a)

x=tu.index(6)
print(x)


az={4,5,6,8,8,8}
print(az)
# az[1]=10
# print(az)
# x=az.index(2)
# print(x)
a=len(az)
print(a)
ax=set()
print(ax)
ax.add(7)
print(ax)
az.remove(4)
print(az)
am={3,5}
am.union({10,20})
print(am)


