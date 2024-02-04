'''import random
name=input("what is your name")
print("Good luck",name)

words=['rainbow','mango','computer','science','player','programming','python','board','geeks','random','reverse','mouse','zebra','dog']
# function will chose one random word from this list
word=random.choice(words)
print('guesses  the character',word)
guesses=''
turns=16
while turns> 0:
    # count the number of time user faild
    failds=0
    # all the characters  from the input
    # word taking one at a time
    print()
    guess=input('guesses a charcter')
    for char in word:
        #compairin the charecter with the charecter in thre guesses
        if char in guesses:
            print(char,end='')
        else:
            print("-")
            
            failds +=1
    if failds==0:
        # user csn win the game if failur is 0 and 'you win' give as output
        print('you win')
        # this is print charect word
        print('The word is',word)
        break
    # if user has input the wrong alphabet the it will ask user enter another alphabet
    # print()
    # guess=input('guesses a charcter')
    # every inpute giess store in guesses
    guesses +=guess
    # cheak input with charactor in word
    if guess not in word:
        turns -=1
        # if character does not match the word  the wrong give in output
        print('wrong')
        # thie will print number of turn left for the user
        print('you have ', turns,'more guesses')
        
        if turns==0:
            print('you loose')  '''
            
import random

name=input('Enter your name')
print('Best of luck :',name)

words=['parrot','fish','cock','beach','bachelar','army']
word=random.choice(words)
print(word)
guesses=''
turn=10
while turn>0:
    faild=0
    guess=input('Enter your guess charecter:')
    for char in word:
    
        if char in guesses:
            print(char,end='')
        else:
            print('-')
            faild +=1
    guesses +=guess
    if faild==0:
        print('you are win',word)
        break
    
    if guess not in word:
        turn -=1
        print('you are wrong , please chhose anotge char')
        print(f'your turn is{turn}')

        if turn==0:
            print('you lose this game')
    
    
            

