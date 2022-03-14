from pickle import FALSE


climate = 'cold-hot'
if climate == 'hot':
    print("It's hot day. drint a lot of water")
elif climate == 'cold':
    print("It's cold day, wear warm clothes")
else:
    print("It's lovely day")

price = 1000000
goodcredit = False

if goodcredit:
    DPpercent = 0.1
else:
    DPpercent = 0.2
downpayment = price * DPpercent
# print("Prie of the house : $" + str(price))
# print("Downpayment       : $" + str(int(downpayment)))

name=input("Enter your name : ")
size = len(name)
if size < 3 or size > 50:
    print("Input must be between 3 and 50 charaters...")
else:
    print("Name looks good...") 