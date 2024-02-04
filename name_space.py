# names= name or identifier  mean a simple variable name that use in our program. in the python we declear a variable and them assign to the object  (object means list,dictionary,class, method,function)
my_list=[1177]
str1='232'
#my_ist and str1 both are varibles names and 1117 or '023' is object
''''namespace =  In simple word namespce is a collection of names and detail of the objects  refrence by names

3we can understand namespace as dictionary like in dictionar is a key and value pairs means 
key=name  and value = object in python 


# There are four type of name space in python.
(1) built-in namespace in python:- A built-in namespace contain the names of built-in function and object
like print() , input(), int()'''

built_names=dir(__builtins__)
for name in built_names:
    print(name)
#there are 152 builtins name already define in python 3.8   

#(2) global namespace
''' global namespace define as module or program lavel,
its mean it cantain name of object which define in module or the main program'''
myNum1=10  # global namespace
my_Num2=20
def add(num1,num2):
    tem=num1+num2
    return tem
print(add(80,90))

#(3) local namespce
''' local namespace create for class, function,loop level,
this variable name cannot be access outside of blok of code or function where they define'''
def add(num1,num2):# local  namespace 
    tem=num1+num2 # local variable
    return tem # local veriablre
print(add(10,20))


def add(num1,num2):
    tem=num1+num2
    
    def print_sum():
        print(tem)
        
    return tem
print(add(20,50))


