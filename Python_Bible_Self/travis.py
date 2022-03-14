known_users=["Alice","Bob","Clarie","Dan","Emma","Fred","Georgie","Harry"]
# print(len(known_users))

while True:
    print("My name is Travis")
    name=input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        print(f"Hello {name}")
        remove_name=input("Would you like to remove your name from system (y/n)?: ").strip().lower()
        
        if remove_name=="y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove_name=="n":
            print("No problem, I didn't want you to leave anyway")
    else:
        print("Hmmm... I don't think I met you before",name)
        add_me=input("Would you like to add your name is the system (y/n)? :").strip().lower()
        print(add_me)

        if add_me=="y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_me=="n":
            print("No worries, see you around!")
