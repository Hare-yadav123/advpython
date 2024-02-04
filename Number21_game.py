
#python code to play 21 Number return the nearest myultiple 
def NearestMultiple(num):
    if num>=4:
        near= num + (4 -(num%4))
    else:
        near=4


def lose1():
    print('\n\n you lose!')
    print('Better luyck next time')
    exit(0)
    
#cheak whether number are consecutive
def cheak(xyz):
    i=1
    while i<len(xyz):
        if (i<xyz[i]-xyz[i-1]) !=1:
            return False
        i =i+1
    return True

# start the game
def start1():
    xyz=[]
    last=0
    while True:
        print("Enter 'F' to take for the fiest chance ")
        print("Enter 'S' to take for the fiest chance ")
        chance=input('>')
        #player take the first chance
        if chance=='F':
            while True:
                if chance==20:
                    lose1()
                else:
                    print('\n your turn')
                    print('\n how many number do you want to wish the enter')
                inp=int(input('>'))
                if inp > 0 and inp <=3:
                    comp=4-inp
                else:
                    print('wrong input ,you are disqualify this game')
                    lose1()
                    
                i,j=1,1
                print('now enter value')
                while i <=inp:
                    a=input('>')
                    a=int(a)
                    xyz.append(a)
                    i=i+1
                    
                # store the last element of xyz
                last=xyz[-1]
                #cheak whether number input number are consecutive
                if cheak(xyz)==True:
                    if last==21:
                        lose1()
                        
                    else:
                        # computer turn
                        while j<=comp:
                            xyz.append(last+j)
                            j=j+1
                        print('Order input after computer turn is :')
                        print(xyz)
                        last=xyz[-1]
        # player take the second chabnce
        elif chance=='S':
            comp=1
            last=0
            
            while last<20:
                #  computer turns
                j=1
                while j<=comp:
                    xyz.append(last+j)
                    j=j+1
                print('Order input after computer turn is :')
                print(xyz)
                if xyz[-1]==20:
                    lose1()
                else:
                    print('\n your turn')
                    print('\n how many number do you want to wish the enter')
                    inp=input('>')
                    inp=inp(inp)
                    i=1
                    print('Enter your value')
                    while i <=inp:
                        xyz.append(int(input('>')))
                        i=i+1
                    last=xyz[-1]
                    if cheak(xyz)==True:
                        #prnt xyz
                        near=NearestMultiple(num)
                        comop=near-last
                        if comp==4:
                            comp=3
                        else:
                            comp=comp
                    else:
                        # if input not cosecutive automatically disqualified
                        print('\n you did not input consecutive integer')
                        # you disqualified this game
                        lose1()
                           
        print('\n\n CONGRATULATION')    
        print('you won')  
        exit(0)     
    else:
        print('wrong choice')
        
game=True
while game==True:
    print('player 2 is computer')  
    
    print('Do you want to play the 21 game (yes\no)') 
    ans=input('>')
    if ans=='yes':
        start1()
    else:
        print('do you want to quite the game (yes/no)')
        nex=input('>')
        if nex=='yes':
            print('you are quiting game...')
            exit(0)
        elif nex=='no':
            print('contunouing')
        else:
            print('wrong choice')
            
                
        
                    
                    
    
    
    
    
    
    
    
    