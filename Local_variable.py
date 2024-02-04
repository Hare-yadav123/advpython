# Local variable we can declared inside a function
#The scope of local variable is limted only to that function where it is created.

def add(x):
    y=10
    print(y) #Local variable
    print(x+y)
add(10)
#print(x)    # if print outside then show name error


print