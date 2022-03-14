def adder(*num):
    sum = 0
    for n in num:
        sum +=n
    print(f"Sum : {sum}")

adder(3,4,5,6,7,8,0,9)
adder(2,3,4,9,8)
adder(3,5)



def intro(**data):
    print("\nData type of argument : ", type(data))

    for key, value in data.items():
        print(f"{key} is {value}")

intro(FirstName="Ghaffar",LastName="Ahmed", Age=25, Phone=987863636)
intro(FristName="Asif", LastName="Qayum", Email="asif@example.com", Country="Pakistan", Age=54, Phone=989798787)