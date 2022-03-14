# class Person:
#     def __init__(self,name):
#         self.name=name
        
#     def talk(self):
#         print(f"Hi {self.name} welcome aboard")

# john = Person("John Smith")
# john.talk()
# bob=Person("Bob Smith")
# bob.talk()

class Mamal:
    def walk(self):
        print("walk")
    
class Dog(Mamal):
    def bark(self):
        print("bark")
    
class Cat(Mamal):
    def annoying(self):
        print("Annoying")

dog1=Dog()
dog1.bark()
dog1.walk()

cat1=Cat()
cat1.annoying()
cat1.walk()