class Cat: 
    _MEOWS = 3 

    @property
    def MEOWS(self): 
        return Cat._MEOWS
        
    @MEOWS.setter
    def MEOWS(self, value):
        raise AttributeError("Cannot modify MEOWS. It is a constant.")
            
    def meow(self): 
        for _ in range(self.MEOWS): 
            print("meow")   

Cat.MEOWS = 5 

cat = Cat()
print(cat.MEOWS)
cat.meow()