class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        # Fish inherts attributes and methods from Animal Class
        super().__init__()
        
    def swin(self):
        print("moving in water")
        
    def breathe(self):
        # adding this to the method Breath, but only in this class
        super().breathe()
        print("Doing this underwater")

nemo = Fish()

nemo.breathe()
