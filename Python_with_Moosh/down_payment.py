criminal_record = input("Criminal record? (y/n): ").strip().upper()
if criminal_record == "Y":
    criminal_status = True
    print("Not eligible for Loan")
else:
    criminal_status = False

    if not criminal_status:
        price = int(input("Price of the house ? : ").strip())
        good_rating = input("Is rating good ? (y/n):").strip().upper()
        high_income = input("Is high income? (y/n):").strip().upper()
    
    if good_rating=="Y" and high_income=="Y": #and not criminal_record:
        down_payment = 0.1 * price

    else:
        down_payment = 0.2 * price 

    print("Eligible for loan!.   Criminal record: ",criminal_status)
    print("Down payment: ${}".format(down_payment))

