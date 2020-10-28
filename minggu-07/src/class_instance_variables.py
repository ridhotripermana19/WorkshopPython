class Dog:

    # class variable shared by all instances
    kind = 'canine' 
    
    def __init__(self, name):
        # instance variable unique to each instance
        self.name = name
        # creates a new empty list for each dog
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)   # shared by all dogs
print(e.kind)   # shared by all dogs

print(d.name)   # unique to d
print(e.name)   # unique to e

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks) # unique to d
print(e.tricks) # unique to e