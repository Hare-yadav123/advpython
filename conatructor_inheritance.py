# by defult ,constructor of parant class inharits in child class it is called con inheri

class parant:
    def __init__(self):
        self.num=1000
        print("this is a parant class")

class child(parant):
    def asd(self):
        print("this is a child class")
        
c=child() 
print(c.num)  
c.asd()