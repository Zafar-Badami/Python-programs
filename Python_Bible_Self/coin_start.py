#import random
class Pound:

# contructing of object

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value=1.25
        else:
            self.value = 1.00
            
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True

# destruction of an object
    def __del__(self):
        print("Coin spent! ")

 #define rust() method for the class "Pound" always use "self" as argument in it.    
    def rust(self):
        self.colour = "greenish"

#define clean() method for the class "Pound" always use "self" as argument in it.      
    def clean(self):
        self.colour = "gold"

#define flip method
    def flip(self):
        head_options = [True, False]
        #choice = random.choice(head_options)
        #self.heads = choice
