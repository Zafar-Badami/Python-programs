#import random

class Coin:

# contructing of an object,  "__init__()" method. Alway use "self" keyword
# pack data in **kwargs"

    def __init__ (self, rare=False, clean = True, heads = True, ** kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
           
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
            
 #define class rust() method rust() for the class "Pound" always use "self" as keyword.
    def rust(self):
        self.colour = self.rusty_colour
        
#define clean() method for the class "Pound" always use "self" as keyword. 
    def clean(self):
        self.colour = self.clean_colour
        
# destruction of an object, "__del__()" method
    def __del__(self):
        print("Coin spent! ")

    
#define flip() method for the class "Pound" always use "self" as keyword. 
    def flip(self):
        head_options = [True, False]
        #choice = random.choice(head_options)
        #self.heads = choice

# create Pound class inherited with Coin class
class Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass":9.5
            }

#unpack dictionary "data"
        super().__init__(**data)
    
