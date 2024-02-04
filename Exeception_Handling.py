#Lambda function=A function without name is called lambda function .it is also known asanonymas
# Anonymous function are not define using def keyword rather they are define using lambda keyword
#syntax
#lambda argument_list:expression

#EX
'''a=lambda x:print(x)
a(2)'''
# Lambda function  dosen't  have name
#lambda x: print(x)

#lambda function return a function
#show=lambda x: print(x)

#lambda fuction can take zero or any argument but their only one expression
# lambda function not needt return statement

#Example
# show =lambda x,y:x+y
# print(show(4,5))

#Ex2
'''show =lambda x,y:(x+y , x-y,x*y,x/y)
p,q,r,s=show(20,5)
print(p)
print(q)
print(r)
print(s)'''

#EX we can pass actual oe defult or posional argument
# show =lambda x,y=8:x+y
# print(show(4))


#NASTED LAMBDA=A lambda function inside call another lambda function 
'''show =lambda x:(lambda y:x+y)
a=show(10)
print(a(20))'''

# Lambda function pass another function 
# def show(a):
#     print(a(10))
    
# show(lambda x:x)

#return Lambda function
'''def abc():
    y=30
    return (lambda x: x+y)
b=abc()
print(b(20))'''

#immediately invoked function Expression(IIFE)
(lambda x,y:print(x+y))(5,6)