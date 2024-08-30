# Constructors and Other Special Methods 
You can use a class in Python to bundle data and functionality together. When you create a new class, you create a new type of object. 

## Creating an instance of a class
Each time you create an instance of a class, Python calls a special class method the constructor. The constructor’s job is to set up the object, meaning that instance of the class, so it’s ready to be used. Usually this means initializing some variables and doing other simple housekeeping.

When writing a Python class, you define a method called `__init__` to be your constructor. The special name tells Python to use that method as the constructor. Just like any other method, the constructor can take arguments. When making an argument to the class, the first constructor must always be `self`.

Here’s a simple example of a constructor that initializes an object’s variables.
```py class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)

# prints "red"
```

## Modify variables
If we wanted to make our Apple class more flexible, we could allow the user to specify the color and flavor as arguments when creating the object. We can modify our constructor to take those arguments and use them:

```py
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)

# prints "sweet" and "tart"
```

## Other special methods
As you might expect, Python classes have many other special methods. Most of these have default implementations provided by the Python standard library, but you are free to override the behavior of any of them. Like the `__init__` constructor, special methods begin and end with a double underscore, and this is called dunder **method**. The word “dunder” combines the “d” in double and the “under” in **underscore**.

For example, the `__str__` special method controls how your object is converted to a string representation for output. When you print() something, Python calls the object’s `__str__()` method and outputs whatever that method returns. In most cases, the default output is just the class name and a memory location:

```py
>>> print(honeycrisp)
<__main__.Apple object at 0x7ffa68d78970>
```

Let’s override the `__str__` method to be more useful for apples:

```py
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)

honeycrisp = Apple("red", "sweet")
print(honeycrisp)

# prints "an apple which is red and sweet"
```

Here are some of the other special methods you can override in your own classes:

- `__len__` returns the length of the object or collection.

- `__contains__` tests whether the object contains an item.

- `__eq__` tests whether two objects are equal.

## Key takeaways

A constructor (such as `__init__)` is a special class method that sets up the object in Python. When making an argument to a class, the first constructor must always be `self`. Python classes have many special methods available in the standard library. These methods can be overridden using the method called **dunder method**.  