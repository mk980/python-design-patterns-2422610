class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""

    def __init__(self) -> None:
        self.name = "British"

    # Note the different method name here!
    def speak_english(self):
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized
    method name"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add a new dictionary item that established the mapping between
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


# List to store speaker objects

objects = []


# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
