#list comprihenssion
'''lst1=[1,2,3,4,6]

squar=[j**2 for j in lst1]
print(squar)
 
square_dict={j**2 for j in lst1}
print(square_dict)

square_tuple=(j**3 for j in lst1)
print(square_tuple)

# performing conditional operation on the entire list

lst2=[4,5,6,7,8]
item_quive=[x**3 for x in lst2 if x%2 !=0]
print(item_quive)
item_dict={x:x**3 for x in lst2 if x%2 !=0}
print(item_dict)

# combinig multiple list in one 
l1=[1,2,3,4,6]
l2=[4,5,6,7,8]
add=[j+k for j, k in zip(l1,l2)]
mul=[j*k for j,k in zip(l1,l2)]
print(add)
print(mul)

# flattenig multiple list into one
l3=[[1,2,3],[4,5,6],[7,8,9]]
# for i in l3:
#     for j in i:
flatt=[j for i in l3 for j in i] 
print(flatt)'''

# there are four types of comprehession
'''
list comprehenssion
dictionary comprehension
set comprehenssion
generator comprehenssion
'''
# l1=[1,2,3,4,5,6,8,9,7,22,12,20,50,40]
# even_no=[i for i in l1 if i%2==0]
# print(even_no)

# square_com=[j**2 for j in range(1,10)]
# print(square_com)

# #dictionary comprehenssion
# no=[1,2,3,6,4,5,8,7,9,611,1,5,15,13]
# odd_no={key:key**3 for key in no if key%2 !=0 }
# print(odd_no)

# state=['Bihar','Jharkhand','UP','MP']
# capital=['patna','Ranchu','Lakhnow','bhopal']

# dict_key={key:value for key ,value in zip(state,capital)}
# print(dict_key)


# #Genrator comprehenssion
# l1=[1,2,3,4,5,6,8,9,7,22,12,20,50,40]
# gen=(v for v in l1 if v%2==0)
# for i in gen:
#     print(i) 
    
# a='we are from bihar '
# x=a.index('a')
# print(x)

mul=[ j*j for j in range(5) ]
print(mul)

evn=[j for j in range(20) if j%2==0 ]
print(evn)
 
a=23
if a>0:
    for j in range(2,a//2):
        if j==0:
            print('it prime not num')
    else:
        print('it is prime')
        
        
ab=[5,6,4,8,99,20,30,1,425,74,56,30]
fv=[j for j in ab if j%2 !=0]
print(fv)

l1=[ i*3 for i in range(1,11)]
print(l1)

lst=[[5,6,7],[1,2,3]]
com_l=[j for i in lst for j in i]
print(com_l[0])

ab=[5,6,4,8,99,20,30,1,425,74,56,30]
even_no=[ i for i in ab  if  i%2!=0 ]
print(even_no)

ac=['cga','ghar',' ','g',' ','mn',' ']
print('orignal_lis:',ac)
# while (' ' in ac):
for i in ac:
    if ' ' in i:
        ac.remove(' ')
print('modified list:',ac)

# a=[1,2,3,4,5,6,7,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# ab=[1,2,3,4,5]
# print(ab[3:0:-1])


