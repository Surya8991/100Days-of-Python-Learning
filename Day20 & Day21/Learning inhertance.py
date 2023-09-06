class Animal():
    def __int__(self):
        num_eyes=2
    def breathe(self):
        print("Inhale , Exhale")

class Fish(Animal):
    # Animal is the name of class to inhert
    # Using super().__init() we are inherting the properties of Animal class to Fish Class
    def __int__(self):
        super().__int__()
    def breathe(self):
        super().breathe()
        print("doing this under water")
    def swim(self):
        print("Moving in water.")

nemo=Fish()
nemo.breathe()