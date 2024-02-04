#  GENERATORS ARE A FUNCTION THAT RETURN THE SEQUENCE OF THE  VALUE. WE USE YIELD STATEMENT FOR THE RETURN THE VALUE FROM  FUNCTION

#NEXT() FUNCTION=THE FUNCTION IS USED TO RETRIEVE ELEMENT BY ELEMENT FROM A GENERATOR OBJECT

'''def show(a,b):
    yield a
    yield b
    
c,d=show(5,8)
print(type(c))
print(d)
print(c)'''


#GENERATOR OBJECT CONVERT IN LIST
def show(a,b):
    yield a
    yield b
    
result=show(5,8)
print(type(result))
lst1=list(result)
print(lst1)

def num_fine(num):
    for sun in range(num):
        yield sun
fa=num_fine(5)
print(type(fa))
print(fa)
print(next(fa))
print(next(fa))

#generating infinite sequence number

def infinit_sequence():
    num=0
    while True:
        yield num
        num+=1
i=infinit_sequence()
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# for j in infinit_sequence(): infinite loop
#     print(j)



#cheak palodrome number through genrator
def palin_num(num):
    temp=num
    reve_num=0
    while num !=0:
        reve_num=(reve_num*10) + num%10
        num=num//10
    if reve_num==temp:
        print( 'this is palin')
    else:
        print('not plain')
num=int(input("Enter number"))

        

na=222
c=na
rev=0
while na!=0:
    b=na%2
    rev=rev*10+b
    na=na//10
if rev==na:
    print('pailin no')
else:
    print('not palin')