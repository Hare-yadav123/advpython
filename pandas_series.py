import pandas as pd 
# a=pd.__version__
# print('pandas version:',a)

# lst_s=[1,2,-3,4,"data base"]
# series=pd.Series(lst_s)
# print(series)

# li=['raju','ram',2,8,6]
# p=pd.Series(li)
# print(p)

# se=pd.Series((4,8,7,'haree'))
# print(se)
#short tric for making series
# series2=pd.Series([1,2,38,'hsree'])
# print(series2)

#Empty series
# empty_s=pd.Series([])
# print('Empty series',empty_s)

#data series with manual index value
# series4=pd.Series([1,2,3,4],['a','b','c','d'],dtype=float, name='data value')
# ser5=pd.Series([5,6,7],['j','k','k'])
# print(ser5)
# print(series4)

# same value copy only write index
# scalar_s=pd.Series(0.5,[1,2,3,4])
# print(scalar_s)

# # we can access the series value using index
# series2=pd.Series({1:'haree',2:'ram'})
# print(series2)
# print(series2[2])

# we can slice and use conditional statemnent
# series2=pd.Series([1,2,38,5,8])
# print(series2[-1:])
# print("*****")
# k=series2[series2>2]
# print(k)

# # we can add  subtract multiplay, divide two series use + operater
# series6=pd.Series([1,2,3,4])
# series7=pd.Series([1,2,3,4,5])

# print(series6*series6)

# import  pandas as pd
# l1={'fruit_name':['mango','graps','apple','banana','gava','pineapple','pomigrant'],'count':[20,30,40,10,13,15,45]}
# dat1=pd.DataFrame(l1)
# print(dat1)

# write data in csvfile
# import csv
# with open('pid1.csv','w')as csvfile:
#     wt=csv.writer(csvfile)
#     for i in range(1):
#         name=input('Name:')
#         Roll=int(input('Roll No:'))
#         course=input('course:')
#         branch=input('Branch Name:')
#         wt.writerow([name,Roll,course,branch])


# with open('stdata.csv','w')as csvfile:
#     write=csv.writer(csvfile)
#     for i in range(10):
#         Name=input('Enter Name:')
#         Class=int(input('enter class:'))
#         Address=input('Enter address:')
#         Age=int(input('enter age:'))
#         write.writerow([Name, Class , Address , Age])
       
       
# import pandas as pd 
# import numpy as np
# from matplotlib import pyplot as plt
# rd=pd.read_csv('stdata.csv') 
# print(rd)
# rd1=rd
# rd.iloc[0:5,1]=np.NaN
# print(rd1.head())
# #it reperset True and False
# print(rd1.isna())

# #
# import pandas as pd 
# import numpy as np
# from matplotlib import pyplot as plt
# y=np.arange(0,10,1)
# print(y)
# cv=plt.plot(x,y)
# print(cv)
# print(plt.xlabel('x-axis'))
# print(plt.ylabel('y-axis'))
 
# create data bar dtata 
# from matplotlib import pyplot as plt

# data1={'apple':20,'banana':50,'orange':30}
# name=list(data1.keys())
# value=list(data1.values())
# print(plt.bar(name, value))

#find out the string lenth without using len() method 
# faf='harendra'
# count=0
# for i in faf:
#     count=count+1
# print(count)

# #
# import numpy as np
# arr=np.arange(0,10)
# op=arr[arr%2!=0] # find odd number  using  numpy array
# print('odd array:',op)

# arr[arr%2==1]=-1  # convert odd number in -1
# print('conver odd number in -1:',arr)

# how can you get common items between two Numpy array 
# import numpy as np
# a=np.array([1,2,3,4,5,3,4,8,6])
# b=np.array([4,2,7,8,0,5,6,9,10])
# print('common array:',np.intersect1d(a,b))

# how can you convert the fiest char of each element in pandas series to uppercast
# import pandas as pd 
# p1=pd.Series(['array','banana','mobile','gun'])
# print(p1)
# print('***************************88')
# p2=p1.map(lambda x:x.title())
# print(p2)

# how would u calculate the number of characterin each word in each series
# import pandas as pd
# p3=pd.Series(['array','banana','mobile','gun'])
# p4=p3.map(lambda a : len(a))
# print(p4)
 
 
# import pandas as pd 
# d1=pd.read_csv('stdata.csv')
# data=d1.head(6)
# da=d1.tail()
# print('tail return button to top row',da)

# print('show info here',d1.info())
# print('head return top to button value ',data)

# data1=data.rename(columns={'Add':'Address'})
# d2=data1.head()
# print(d2)

# dict_series={'Name':'Ram','address':'Bihar','Edu':'Degree'}
# series=pd.Series(dict_series)
# d=[20,30,40,50]
# da=pd.Series(d)
# print(da)
# ds=pd.DataFrame(d)
# print(ds)
# print('directry object',series)


# ad=[4,5,8,8,None,'mango']
# mv=pd.DataFrame(ad)
# us=mv.isnull()
# print(us)

# import random
# import numpy as np
# col=['m','n','o','p','v']
# ind=['B','A','C','D','g']
# df5=pd.DataFrame(np.random.rand(5,5),columns=col,index=ind)
# print(df5)