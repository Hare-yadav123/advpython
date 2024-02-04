# 1 Calling  a python function
'''def fun():
    print("welcome to mumbai")
fun()'''


#2
def add(num1:int,num2:int):
    '''Add two number'''
    num3=num1+num2
    return num3
ans=add(5,6)
print(f"the addition of num={ans}")

#3
def is_prime(n):
    if n in [2,3]:
        return True
    if(n==1) or (n%2==0):
        return False
    
                       
print(is_prime(15))

#simple pythhon functin find even or odd

def even_odd(x):
    if x%2==0:
        return 'even '
    else:
        return 'odd'
e=even_odd(13)
print(e)


#Defult argument
def defult(x,y=20):
    print("x:",x)
    print("y:",y)
    
defult(12)

# Keyword argument
def student(fistname,lastname):
    print(fistname,lastname)
    
student(fistname='Hree', lastname='yadav')

#veriable lenth argument
def MyValue(*hjk):
    for arg in hjk:
        print(arg)
        
MyValue('Haree','raju','raju','amarjeet','ankush')

#8
def MyValue(**hjk):
    for key,value in hjk.items():
        print(key,value)
        
MyValue(fistname='Hree', lastname='yadav')




#9Document string  or doctstring
def evenodd(x):
    if (x%2==0):
        print("even")
    else:
        print("odd")   
print(evenodd.__doc__)


#function inside function(recrurtion)
def f1():
    s='you are great'
    
    def f2():
        print(s)
    f2()
f1()


##
def cheak_func(data):
    l=data[0]
    s=data[0]
    
    for num in data:
        if num>l:
            l=num
        elif num<s:
            s=num
    return l,s 

print(cheak_func([1,22,33,4,5,6-78,80]))



h=int(input('enter your number'))

if (h==1) or (h%2==0):
    print('not prime')
else:
    print('prime number')


















