
#? Default args
def my_func(a, b=2):
    print(a+b)

# my_func(a=2)
# my_func(a=2, b=8)

#? unlimited positional *args
def add(*numbers):
    # soma = 0
    # for n in args:
    #     soma += n
    print(sum(numbers))

# add(9, 5, 6, 7, 8)

#? unlimited optional keyword **kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
# calculate(5, add=3, multiply=5)

class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make = "Nissan", model = "Skyline")
print(my_car.colour) #returns "none"