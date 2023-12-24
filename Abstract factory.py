class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "woof!"

    def __str__(self) -> str:
        return "Dog"


class DogFactory:
    """Concrete factory"""

    def get_pet(self):
        """returns a Dog object"""
        return Dog()

    def get_food(self):
        """returns a Dog food object"""
        return "Dog Food!"


class petStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """Pet_factory is our Abstract Factory"""

        self._pet_factory = pet_factory

    def show_pet(self):
        """utility method to display the details of the objects returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("its food is '{}'".format(pet_food))


# Create a concrete factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = petStore(factory)

# Invoke the utility method to show the details of our get

shop.show_pet()
