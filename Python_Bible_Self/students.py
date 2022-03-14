students={
            "Ali": {"id":"ID001","age":25,"grade":"A+"},
            "Jafer": {"id":"ID002","age":26,"grade":"B"},
            "Ahmed": {"id":"ID003","age":27,"grade":"C"},
            "Muslim": {"id":"ID005","age":29,"grade":"B+"},
            "Saad": {"id":"ID004","age":32,"grade":"A"}
             }
while True:
    name=input("Name of Student : ").strip()
    if name not in students:
        print("Sorry name not found !")
    else:
        print("ID : ",students[name]["id"])
        print("Age : ",students[name]["age"])
        print("Grade: "+ students[name]["grade"])
