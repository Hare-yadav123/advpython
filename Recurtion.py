#1 A function calling itself again and again to continoue a value referred to the recursiomn

'''def abc():
    print("I am Haree")
    abc()
abc()'''

#2 
'''a=0#global veriable
def abc():
    global a
    a=a+1
    print(a,"I am Haree")
    abc() 
abc()'''

#Local veriable
# def abc():
#     v=0
#     v=v+1
#     print(v,"I am Haree")
#     abc()
# abc()

#find recursion limit
'''import sys
print(sys.getrecursionlimit())# bydefult limit 1000
sys.setrecursionlimit(200)#setrecursion limit
print(sys.getrecursionlimit())'''
# reverse fun in recursion

def reverse(str1):
    if len(str1)==1:
        return str1ram
    
    else:
        return reverse(str1[1:])+str1[0]
    
str1=input("entrer input")
ab=reverse(str1)
print(ab)
print(type(ab))

'''def cheak(n):
    if n<2:
        return (n%2==0)
    return cheak((n-2))        
n=int(input("enter your no"))
if cheak(n)==True:
    print(" even no")
else:
    print("odd number")
cheak(n)'''

'''def cheak(str,ch):
    if not str:
        return 0
    elif str[0]==ch:
        return 1+cheak(str[1:],ch)
    else:
        return cheak(str[1:], ch)

str=input("give input")
ch=input(" write ch name")
a=cheak(str,ch)
print(cheak(str, ch))


def fact(m):
    if (m<=1):
        return 1
    else:
        return m*(m-1)
m=int(input("number"))
print("fact=",fact(m))
fact(m)'''


# l=[]   
# def sum_num(n):
#     if (n==0):
#         return 1
#     d=n%2
#     l.append(d)
#     d=sum_num(n//10)
                
# n=int(input("enter your no"))
# b=sum_num(n) 
# print(b)

# a=open("MyDemo.txt","r")
# f=a.read("ram am ")
# a.close()
# print(f)