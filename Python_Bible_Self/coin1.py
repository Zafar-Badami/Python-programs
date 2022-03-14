import random
class Coin:
    def __init__(self, rare=False, heads=True, clean=True, **kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value=self.original_value * 1.25
        else:
            self.value=self.original_value
        
        if self.is_clean:
            self.colour=self.clean_colour
        else:
            self.colour=self.rust_colour
    
    def __del__(self):
        print("Coin spent !")
        
    def rust(self):
        self.colour = self.rust_colour
    
    def clean(self):
        self.colour = clean_colour

    def flip(self):
        head_options = [True,False]
        choice=random.choice(head_options)
        self.heads=choice


class Pound(Coin):
    def __init__(self):
        data = {
            "original_value" : 1.00 ,                  
            "clean_colour" : "gold",
            "rusty colour" : "greenish",
            "num_edges" : 1,
            "diameter" : 22.2, 
            "thickness" : 3.15,
            "mass" : 9.5
        }
        super().__init__(**data)

       
