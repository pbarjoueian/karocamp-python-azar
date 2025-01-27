class Animal:
    def __init__(self, name: str, weight: float, color: str, legs: int = 4):
        self.legs: int = legs
        self.weight: float = weight
        self.color: str = color
        self.name: str = name

    def move(self):
        print(f"{self.name} Is moving...")

    def sleep(self):
        print(f"{self.name} Is sleeping...")

    def eat(self, food: str):
        print(f"{self.name} Is eating {food}")

    def make_noise(self):
        print("Noise......")


class Cat(Animal):
    def __init__(self, name: str, weight: int, color: str, cover: str = "fur"):
        super().__init__(name=name, weight=weight, color=color)
        self.cover = cover

    def make_noise(self):
        print("meow")


class Dog(Animal):
    def __init__(self, name: str, weight: int, color: str, _type: str):
        super().__init__(name=name, weight=weight, color=color)
        self._type: str = _type

    def make_noise(self):
        print("bark")


cat = Cat(name="Gorbe", weight=4, color="black")
cat.move()
cat.make_noise()


dog = Dog(name="Hero", weight=14, color="black", _type="German")
dog.move()
dog.make_noise()
