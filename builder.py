""" Builder patterns include FOUR kind of roles
1. director, 2. abstract builder, 
3. concrete builder, 4. object builder(product)"""


class Director:
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """Abstract builder"""

    def __init__(self) -> None:
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete builder --> provides parts and tools to work on the"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class Car:
    """Product"""

    def __init__(self) -> None:
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self) -> str:
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
