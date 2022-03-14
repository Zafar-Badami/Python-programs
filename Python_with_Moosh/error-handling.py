try:
    age = int(input("Your age : "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("Invalid input....")