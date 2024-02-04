print('1 for add')
print('2 for sub')
print('3 for mul')
print('4 for div')
f1=int(input('Enter your first number'))
f2=int(input('Enter your second number'))
choise=int(input('enter your choice'))
if choise==1:
    add=f1+f2
    print(add)
elif choise==2:
    subtract=f1-f2
    print(subtract)

elif choise==3:
    multiply=f1*f2
    print(multiply)
    
elif choise==4:
    divide=f1/f2
    print(divide)
else:
    print('This input is rong ! please choose right input')
    

