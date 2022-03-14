films={
    "Finding Nemo":[3,5],
    "Hercolus":[18,5],
    "Tarzan":[15,1],
    "Ghost Busters":[12,5]
    }
while True:
    choice=input("Which film you want to watch : ").strip().title()
    if choice in films:
        age = int(input("How old are you : ").strip())
        if age >= films[choice][0]:
            if films[choice][1]>0:
                print("Enjoy the film ! ")
                films[choice][1] -=1
                print(f"ticket left....  {films[choice][1]}")
            else:
                print("No seats available....")
        else:
            print(" You are under age for this movie...")
    else:
        print("We don't have this film... ")
