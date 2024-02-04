# *args :- it is speacial syntex use in function definition to pass variable lenth agument
# '*' means variable lenth and args is name use for convection. u can use another name

def calculation(*args):
    #ad=a*b
    mul=1
    for i in args:
        mul *=i
    return mul
print(calculation(5,8,5,9,2))
        
        
# **kwargs it is alos speceal syntex used in function definition pass variable lenth keyword arguments
# it is actually a dictionary of the variable names and its value
def TellArr(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
TellArr(arg1="item1",arg2="item2",arg3="items3")


def fun(*args):
    print( args)
    
fun(1,2,3,4,5)