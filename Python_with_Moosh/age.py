import datetime

name= input("What is your name : ")
birth_year = int(input("What is your birth year : "))
today = str(datetime.date.today())
curr_year = int(today[:4])
curr_month = int(today[5:7])
curr_day = int(today[8:10])
age = curr_year - birth_year
print(f"{name} is {str(age)} years old...")
print(today)
print(curr_year)
print(curr_month)
print(curr_day)