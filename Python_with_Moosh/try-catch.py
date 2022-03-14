try:
    age = int(input("Age : "))
    income = int(input("Income : "))
    risk = income/age  
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero...")
except ValueError:
    print("invalid input ...")