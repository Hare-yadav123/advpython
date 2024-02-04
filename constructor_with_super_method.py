class parant:
    def __init__(self,r):
        self.raju=r
        self.num=1000
        print("this is a parant class")
    def rat(self):
        print(" relative of the parant ******",self.raju)
        
class child(parant):
    def __init__(self,r):
        super().__init__(r)
        print(' i am a child class')
    def asd(self):
        print("this is a child class")
        
c=child("Raju") 
print(c.num)
c.rat()
c.asd()
   