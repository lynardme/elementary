"""The user expectation yields multiple, related objects"""

class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """returns a Dog object"""

    def get_food(self):
        """returns a Dog food object"""

class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """petfactory is our Abstract Factory"""

    def show_pet(self):
        """Utility method to display the details of the objects returned by the DogFactory"""

        print()