class Borg:

    """The Borg design pattern"""

    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make an attribute dictionary


class Singleton(Borg):

    """The Singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)  # update the attribute dictionary

    def __str__(self):
        return str(self._shared_data)


# Let's create a singleton object and add our first acronym

x = Singleton(HTTP="Hyper Text Transfer Protocol")

# print the object

print(x)

y = Singleton(SNMP="simple network management protocol")
print(y)
