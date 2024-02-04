# Q. what do understand by NumPy
''' NumPy is the most  popular,easy to use,versatile ,open source ,python based ,general
-purpose package that is used for processing array. 
# it is short for NUMerical python'''
# it is used to perform verious operation
# Trignometric,static,alzebric,brodcastin ,Bitwise operation,Coping and viewing array,sereachin,shortin and counting

# Q.2 what are the steps to create 1D,2D and 3D array
'''import numpy as np
one_dimentional_list=[1,2,3]
one_dimentional_arr=np.array(one_dimentional_list)
print("1 D araay is :",one_dimentional_arr)'''

#2D array
'''two_dimentional_list=[[1,2,3],[4,5,6]]
two_dimentional_arr=np.array(two_dimentional_list)
for i in two_dimentional_arr:
    print("two dimento arr:",i)'''
    
#3D   
'''three_dimention_list=[[[1,2,3],[4,5,6],[7,8,9]]]
three_dimention_arr=np.array(three_dimention_list)
print("3D array:")  
print(three_dimention_arr)'''

# nd array ceation = This array can be achived 'ndmin' attributes and ndim
'''import numpy as np 
ndArray=np.array([1,2,3,4],ndmin=6)
print(ndArray)
print("dimention of array:",ndArray.ndim)'''



# Q. as input given arrar , and another new column then you have delet second column from array and add new culumn after replacing second column from array
'''import numpy as np
arr_col=[[4,5,6,7],
         [7,8,9,2],
         [4,5,8,2]]
new_col=[0,1,2]
a=[6,9,8]
np_data=np.array(arr_col)
for i in np_data:
    print(i)
print('****************')
# delete second column
del_arr=np.delete(arr_col,1,axis=1)
print(del_arr)
# add new column
add=np.insert(del_arr,1,new_col,axis=1)  #insert
print(add)'''


# Q. how will you read csv data in to an array in numpy
'''import numpy as np
csv_data=np.loadtxt('fileName.csv',delimiter=',',dtype=str)
print(csv_data)'''

# other method is genfromtxt
# read=np.genfromtxt('student.csv',dtype=str)
# print(read)

# Q. how will reverse the array    
# arr=np.array([1,2,3,4,5,7,8,9])
# rev_arr=arr[::-1]
# print(rev_arr)

# Q. How will you find the nearest of the give value and their index
'''we can use np.abs() functin find nearst value and np.argmin() function for findinding index'''
'''import numpy as np
elm_arr=np.array([45,20,36,78,50,60])
near_value = 30
# find the nearset array of given value 85
deff_ele_val= np.abs(elm_arr-near_value)
# find the indext of nearst value 
index= deff_ele_val.argmin()

print(" origina array is:",elm_arr)
print("near value :",near_value)
print(" nearst value of 85 is :",elm_arr[index])
print("index of nearest array:",index)'''

# exa2
'''def value(ar,x):
    ax=np.asarray(ar)
    ne_val=(np.absolute(ar-x)).argmin()
    #ind=ne_val.argmin()
    return ax[ne_val]
    return ind

ar=np.array([4,5,6,7,8])
x=9   
print(ar)
print(value(ar, x))'''

# Q. how will you find  shape of given numpy array
''' In numpy we will use an attributce called shape which return tuple  '''

'''arr1=np.array([7,8,9,4,5,6])
arr2=np.array([[5,6,9,0,8],[1,2,6,5,0]])
print('1-D array:',arr1.shape)
print('2-D array:',arr2.shape)'''