def lbs_to_kg(weight):
    return weight *0.45

def kg_to_lbs(weight):
    return weight/0.45

def find_max(numbers):
    maxi=numbers[0]
    for i in numbers:
        if i > maxi:
            maxi=i
    return maxi