'''pandas is open source python based  library ,used in data manupulation application requairing high performance
  # This was develop by wes Mckinny in 2008 for data analysya'''
  
# Dtatfram= A datafram is 2D mutable and tabular structure for representing data lebelled with axis and columns
#syntex
import pandas as pd 
# datafram=pd.DataFram(data,index, column,dtype)

# how will you combine diffrent pandas  dataframe
 
#append()method
# 

#print(pd.concat([df1,df2]))
# df=df1.join(df2)
# print(pd.DataFrame(df))

#2 can you create a series from the dictionary object in pandas
'''one dimentional array capable of storing different data types is called a series'''
dict_series={'Name':'Ram','address':'Bihar','Edu':'Degree'}
series=pd.Series(dict_series)
print('directry object',series)






# 3How will you identify and deal with missing value in datfram
''' we can identify if a data fram has missing values by using the isnull() and isna() method'''

#missing_data_cunt=df.isnull().sum()
# import pandas as pd
# import numpy as np
# lst1=[4,7,'mango',None,9,None,5,None,None]
# mvc=pd.DataFrame(lst1)
# l=mvc.isnull()
# nm=mvc.isnull().sum()
# print(l)
# print('sum of nuull data',nm)

# 4 csv file read example
# data=pd.read('stident.csv')
# se=pd.notnull(data[5])
# print(se)

#5 fillinf missing value used fillna()
# import pandas as pd
# import numpy as np
# lst1=[4,7,'mango',None,9,None,5,None,None]
# mvc=pd.DataFrame(lst1)
# j=mvc.fillna("value") # fillna method
# print('filna value input in place of None',j)

# 6 what do u understand by reindexing in panads
'''Reindexing in panads can be used by changed the index of rows and columns of dataframe'''
# reindex() method used for reindexing
# column=['a','b','c','d','e','f']
# index=['A','B','C','D','E','F']
# #create dataframe of random value of array
# df4=pd.DataFrame(np.random.rand(6,6),columns=column,index=index)
# print(df4)
# print("data frame after reindexing")
# print(df4.reindex(['B','A','C','D','E','F']))

# 7  example2
# col=['m','n','o','p','v']
# ind=['B','A','C','D','g']
# df5=pd.DataFrame(np.random.rand(5,5),columns=col, index=ind)
# print(df5)

# print("after reindexing")
# new=['j','k','l','m','h']
# print(df5.reindex(new))


# 8 reindexing the columns using axis keyword***
# column=['m','n','o','p','v']
# index=['B','A','C','D','g']
# df6=pd.DataFrame(np.random.rand(5,5),columns=column,index=index)
# print(df6)
# column=['Q','R','T','Y','U']
# print('after reindexing columns')
# print(df6.reindex(column,axis='columns'))

# 9 Replacing the missing value
# Q. how to add new column to pandas dataframe
# using list
# import pandas as pd 
# data={'Name':['Haree','Raju','Vishanu','Karan'],'Age':[20,22,25,23],'Qualification':['B-Tech','M-sc','BA','B-com']}
# df=pd.DataFrame(data)
# address=['Bihar','Panjab','Jharkhan','Bihar']
# df['address']=address
# print(df)
# re={'name':['raju','karan'],'age':[45,20]}
# dp=pd.DataFrame(re)

# print(dp)

# 10 using assign() method
# data={'No':[40,50,80,70],'paper':['english','hindi','math','science']}
# df=pd.DataFrame(data)
# print(df.assign(address=['bhutan','bangladesh','kerla','delahi']))

# 11 insert method
# data={'No':[40,50,80,70],'paper':['english','hindi','math','science']}
# df=pd.DataFrame(data)
# print(df.insert(0,'address',['china','pakistan','tamil','delahi'],True))


# Q. How will you delete indices ,row and coloumns from dataframe
''' 1. Excute "'(del df.index.name)'" for removing the index by name
2. Alternatively , the (df.index.name ) place of name assigned None'''
# import pandas as pd
# data1={'Name':['ram','shayam','bhanu'],'Aim':['doctor','Engg','IAS'],'no':[4,5,8]}
# df=pd.DataFrame(data1)
# print("origiana data frame")
# print(df)
# df.drop(['Name'],inplace=True,axis=1)
# print(df)

#Q. can u get items of series 1 are not available in another series 2
'''This can be achived by using ~ not/negation or isin() method '''
# dn1=pd.Series([1,2,3,4,5,6])
# dn2=pd.Series([11,5,8,7,6,4,])
# dn3=dn1[~dn1.isin(dn2)]
# print(dn3)

# db1=pd.Series([ 'a','b','c','w','d','r','m','n'])
# db2=pd.Series([ 'a','v','c','f','d','g','m','n'])
# db=db1[~db1.isin(db2)]
# print(db)

#how wiil you get the items that are not common to both the given series A and B
'''we can achived by performing thr unoin of both  then taking intersection of both'''
# import numpy as np
# db3=pd.Series([ 'a','b','c','w','d','r','m','n'])
# db4=pd.Series([ 'a','v','c','f','d','g','m','n'])
# p_unuin=pd.Series(np.union1d(db3,db4))
# p_intersect=pd.Series(np.intersect1d(db3,db4))
# db5=p_unuin[~p_unuin.isin(p_intersect)]
# print(db5)


# Q.5.while importing data from different sources, can the pandas library recognize dates
''' yes ,it can but we need to add the parse_dates argument while we reading data from the sources'''
# example
'''import pandas as pd 
from datetime import datetime
dateparser=lambda date_val:datetime.strptime(date_val, '%Y-%m-%d %H:%M:%S')
df=pd.read_excel("file.csv",parse_dates=['datetime_column'],date_parser=dateparser)
print(df)'''



# import pandas as pd 
# import numpy as np 
# data=np.random.rand(2,4,5)
# p=pd.Panel(data)
# print(p)

ac=pd.Series([4,5,6])
ax=pd.Series([7,8,9])
av='ac'.join(ax)
print(av)
