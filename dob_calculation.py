from datetime import date

dob=date(2001,5,25)
t=date.today()
age=t.year-dob.year-((t.month, t.day)<(dob.month,dob.day))
print(age)