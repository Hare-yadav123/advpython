'''import csv 
with open('student.csv','w')as csvfile:
    wrt=csv.writer(csvfile)
    for i in range(1):
        n=input('Enter Name')
        dob=input('Enter dob')
        slry=int(input('Enter salary'))
        wrt.writerow([n,dob,slry])'''

# import csv
# with open('student.csv','r')as csvfile:
#     rd=csv.reader(csvfile,)
#     #next(rd)
#     for row in rd:
#         print(row)

# Q.2 example
import csv
# file1=open('fileName.csv','w')
# write=csv.writer(file1)
# str1=input("enter sring:")
# write.writerow([str1])
# file1.close()

# file2=open('fileName.csv','r')
# read=csv.reader(file2)
# for i in read:
#     print(i)
# file2.close()


import csv
# with open('emp.csv ','w')as file2:
#     wr=csv.writer(file2)
#     for i in range(2):
#         fname=input('fname')
#         lname=input('lname')
#         wr.writerow([fname,lname])
#         print(i)
# file2.close()

with open('emp.csv','r')as rdfile:
    rd=csv.reader(rdfile)
    for i in rd:
        print(i)
        
rdfile.close()