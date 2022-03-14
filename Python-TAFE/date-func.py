# Calculating the user's Age given their date of birth.
from datetime import datetime
     
Year = int(input("Please enter the year you were born: "))
Month = int(input("Please input the number of the month you were born.")) 
#(For example 8 = August): "))
Day = int(input("Please enter the day you were born "))
    
DateOfBirth = datetime(Year, Month, Day)
Age = datetime.now() - DateOfBirth
     
print("You are " + str(Age.days) + " days old")
    
convertdays = int(Age.days)
AgeYears = convertdays/365
    
print("Or " + str(AgeYears) + " years old to be less precise")
print(type(AgeYears))