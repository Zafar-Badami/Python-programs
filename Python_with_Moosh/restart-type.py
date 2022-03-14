name = input("Name: ")
balance = 100.50

#Method 1:
print(name+" has $"+str(balance))

#Method 2:
print("%s has $%f"%(name,balance))
print("%-10s has $%.2f"%(name,balance))

#Method 3:
print("{} has ${}".format(name,balance))
print("{} has ${:.2f}".format(name,balance))
print("{:<10} has ${:.2f}".format(name,balance))
print("{:>10} has ${:.2f}".format(name,balance))
print("{:^10} has ${:.2f}".format(name,balance))
print("{:*^10} has ${:.2f}".format(name,balance))
