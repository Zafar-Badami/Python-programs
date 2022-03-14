# weight = int(input("Weight : "))
# unit_measure = input("(L)bs or (K)gs: ")
# if unit_measure.upper() == 'L':
#     print(f"You are {weight*0.45} kilograms")
# else:
#     print(f"You are {weight/0.45} Pounds")

secret_num = 9
attempts = 1 
while attempts <= 3:
    guess=int(input(f"Guess No {attempts} : "))
    attempts +=1
    if guess == secret_num:
        print("You win!")
        break
else:
    print("You fail...") 
