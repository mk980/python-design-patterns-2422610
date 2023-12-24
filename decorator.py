from functools import wraps


def make_blink(function):
    """define the decorator"""

    # this makes the decorator transparent in terms of its name and docs
    @wraps(function)

    # define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()
        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# apply decorator here
@make_blink
def hello_world():
    """original function"""
    return "Hello world!"


# Check the result of decorating
print(hello_world())

# check the function name is still the same name of the function being decorated
print(hello_world.__name__)
print(hello_world.__doc__)
