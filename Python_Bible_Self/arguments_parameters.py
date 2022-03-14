def about(name, age, likes):
    sentence="Meet {} ! He is {} year old and he likes {}.".format(name,age,likes)
    return sentence

# you can also define a default value for nil input but that parameter must be define at the last
# as keyword argument

def about2(name,age,likes="Python"):
    sentence2 = "Meet {} ! He is {} years old and he likes {}.".format(name,age,likes)
    return sentence2


