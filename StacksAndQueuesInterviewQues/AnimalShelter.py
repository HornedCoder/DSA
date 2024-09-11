class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def __str__(self):
        return str(self.cats) + str(self.dogs)
    
        
    def enque(self,animal,type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    def dequeCat(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.cats.pop(0)
        

    def dequeDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            return self.dogs.pop(0)


    def dequeAny(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result
    
c = AnimalShelter()
c.enque('Cat1','Cat')
c.enque('Cat2','Cat')
c.enque('Dog1','Dog')
c.enque('Cat3','Cat')
c.enque('Dog2','Dog')

print(c)
c.dequeAny()
c.dequeCat()
print(c)