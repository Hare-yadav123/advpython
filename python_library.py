# Q. difference b/w python module and package
'''The module is a single python file .a module can import other modules (otrher pythgon file)
as object  
where package is the folder/Directory where different subpackage or module reside
2. Python module is created by saving the file with the extention of .py
and this file we can use accross the project 
             but '''
 
'''class Bmw:
    # first we create a construction pof class
    #and add the member to it here modulw
    def __init__(self):
        self.models=['8i','x7','z9','p2','l6']   
        
    #a normal print function
    def out_Models(self):
        print('There are a availabel models in Bmw:')
        for model in self.models:
            print('\t%s' %model)
b=Bmw()'''
# Q. whatbare some most important built-in module used in  python
''' os, math, random calenedr ,datetiume json ,csvfile,sqlite3,sys,re ,pickle,abc '''
  
  
  #Q can you cheak easly all charector given in string are alphanumeric
''' yes we can use isalnum() for cheak it'''
a='andcg12333'
b='@#4123addkjd'
print(a.isalnum())
print(b.isalnum())


#q. what do you mean GIL
''' gil stand for glonal interpreter lock use for manage threading in python
becouse of gil multi thred working same as single thread in python '''
import time
from threading import Thread
c=50000000000
def countDown(n):
    while n>0:
        n -=1
      
start=time.time()
countDown(c)
end=time.time()
print('time taken',end-start)


# Q. what is PYTHONPATH
''' PYTHONPATH is a enviroment veriable that is use to set the path for  user-define modules  so thst
it can directly impoirted into a python programm ,
or this veriable help the python interpretor for finding path or location of user define module.
it is also responsible for handling the defult search'''


#Q identify bugs and performing static analysis in python
''' yes , we can use tool like  pycheaker and pylink find out bug which are used static analysis
pycheaker help the finds bugs in python source code file and raise alert for issue
 but pylink cheaks for the modules coding standerds and support different pulgin'''



#Q,writew a program takes asequence of number and cheak it if all number are unique
def chek_lenth(n):
    if len(n)==len(set(n)):
        return True 
    else:
        return False 
    
print(chek_lenth([4,5,6,8]))  
print(chek_lenth(2,2,5,57,8)) 



