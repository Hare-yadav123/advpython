# set is a also collection of data and bult in type of data which unorderd ,unindexed and we can't add duplicate items but we can add new items,set creat with curly brcket{}

#example of unorderd set
set1={'mango',45,'apple',25.5,'Ram'}
print(set1)

#example of can't add duplicate item in set
# set1={'mango',45,'apple',25.5,'Ram'}
# set1.add(45)
# print(set1)

#example of .add() method ,we can add new items in set insted duplicate item
set1={'mango',45,'apple',25.5,'Ram'}
set1.add('banana')
print(set1)

#example of .update() add multiple items
set1={'mango',45,'apple',25.5,'Ram'}
set1.update('home','ludo',200,'youdha')
print("update",set1)

#example of len set
set1={'mango',45,'apple',25.5,'Ram'}
l=len(set1)
print(l)

#example of remove methiod set
set1={'mango',45,'apple',25.5,'Ram'}
set1.remove(45)
print(set1)

#example of pop method set
set1={'mango',45,'apple',25.5,'Ram'}
set1.pop()
print(set1)

#example of copy method set
set1={'mango',45,'apple',25.5,'Ram'}
s=set1.copy()
print(s)

#example of union method set
set1={'mango',45,'apple',25.5,'Ram'}
set2={20,'banana'}
set3=set1.union(set2)
print("union methd",set3)









