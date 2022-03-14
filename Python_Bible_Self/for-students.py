students = {
    "male": ["Ali", "Shabbir", "Noman", "Ghazi", "Aman"],
    "female": ["Mumtaz", "Erum", "Mariya", "Zeenat","Nasreeen"]
    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
            
