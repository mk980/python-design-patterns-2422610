import types  # imports type module


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default strategy"

        # if a reference to a function is provided, replace the executed
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # this gets replace by another version if another
        """The default method that prints the name of the strategy being"""

        print("{} is used!".format(self.name))


# replacement method 1


def strategy_one(self):
    print("{} is use to execute method 1".format(self.name))


# replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Let's create out default strategy
s0 = Strategy()

# Let's execute our default strategy
s0.execute()

# Let's create the first variation of our default strategy by providing

s1 = Strategy(strategy_one)

# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
