name=input("Enter your name ? :")
if len(name)<=3:
    print("Name should be longer than atleast 3 characters ")
elif len(name)>15:
    print("Name should not be longer than 15 characters..")
else:
    print("Name looks good!")
