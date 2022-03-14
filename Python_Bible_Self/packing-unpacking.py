# pack/unpack using * with funtions 
# (make value list seperate values with space or before parameter # make argument list unlimited)

def add(*numbers):
    total=0
    for number in numbers:
        total=total+number
    return total
    
# pack/unpack using '**' in keyword argements

dictionary = {"name":"Khalid", "age":34,"likes":"Tennis"}

def about(name,age,likes):
    
    sentence="Meet {} ! He is {} years old and he likes {}".format(name,age,likes)
    return sentence

# args and kwargs using ** packing

def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))
    
