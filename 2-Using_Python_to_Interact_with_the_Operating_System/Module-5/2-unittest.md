# unittest

A unittest provides developers with a set of tools to construct and run tests. These tests can be run on individual components or by isolating units of code to ensure their correctness. By running unittests, developers can identify and fix any bugs that appear, creating a more reliable code. In this reading, you will learn about unittest concepts, how to use and when to use them, and view an example along the way.

## Concepts

Unittest relies on the following concepts:

- `Test fixture:` 

    This refers to preparing to perform one or more tests. In addition, test fixtures also include any actions involved in testing cleanup. This could involve creating temporary or proxy databases, directories, or starting a server process.

- `Test case:` 

    This is the individual unit of testing that looks for a specific response to a set of inputs. If needed, TestCase is a base class provided by unittest and can be used to create new test cases.

- `Test suite:` 

    This is a collection of test cases, test suites, or a combination of both. It is used to compile tests that should be executed together.

- `Test runner:` 

    This runs the test and provides developers with the outcome’s data. The test runner can use different interfaces, like graphical or textual, to provide the developer with the test results. It can also provide a special value to developers to communicate the test results. 

## Use case

Let’s look at a test case example where the Python code simulates a cake factory and performs different functions. These include choosing different sizes and flavors of a cake, including small, medium, and large, and chocolate or vanilla. 

In addition, the simple class allows developers to add sprinkles or cherries to the cake, return a list of ingredients, and return the price of the cake based on size and toppings. 

Run the following code: 


```python
from typing import List


class CakeFactory:
 def __init__(self, cake_type: str, size: str):
   self.cake_type = cake_type
   self.size = size
   self.toppings = []

   # Price based on cake type and size
   self.price = 10 if self.cake_type == "chocolate" else 8
   self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0

 def add_topping(self, topping: str):
     self.toppings.append(topping)
     # Adding 1 to the price for each topping
     self.price += 1

 def check_ingredients(self) -> List[str]:
     ingredients = ['flour', 'sugar', 'eggs']
     ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
     ingredients += self.toppings
     return ingredients

 def check_price(self) -> float:
     return self.price

# Example of creating a cake and adding toppings
cake = CakeFactory("chocolate", "medium")
cake.add_topping("sprinkles")
cake.add_topping("cherries")
cake_ingredients = cake.check_ingredients()
cake_price = cake.check_price()


cake_ingredients, cake_price

```

```
Output:

(['flour', 'sugar', 'eggs', 'cocoa', 'sprinkles', 'cherries'], 14)
```

In the code above, the cake factory class and methods are defined. 

Now it’s time to **define the unittest methods** to test the different functions of the code. 

The `test suite` includes tests for the cake’s flavor, size, toppings, ingredients, and price. The first test case in the suite will intentionally provide the wrong value—and that’s what we want! Create specific statements to make sure the program is behaving as it should. 

That includes providing incorrect data to determine if the program will provide failed results. Because unittest is class-based,  encapsulate these statements into test methods.

```python
import unittest

class TestCakeFactory(unittest.TestCase):
 def test_create_cake(self):
   cake = CakeFactory("vanilla", "small")
   self.assertEqual(cake.cake_type, "vanilla")
   self.assertEqual(cake.size, "small")
   self.assertEqual(cake.price, 8) # Vanilla cake, small size

 def test_add_topping(self):
     cake = CakeFactory("chocolate", "large")
     cake.add_topping("sprinkles")
     self.assertIn("sprinkles", cake.toppings)

 def test_check_ingredients(self):
     cake = CakeFactory("chocolate", "medium")
     cake.add_topping("cherries")
     ingredients = cake.check_ingredients()
     self.assertIn("cocoa", ingredients)
     self.assertIn("cherries", ingredients)
     self.assertNotIn("vanilla extract", ingredients)

 def test_check_price(self):
     cake = CakeFactory("vanilla", "large")
     cake.add_topping("sprinkles")
     cake.add_topping("cherries")
     price = cake.check_price()
     self.assertEqual(price, 13) # Vanilla cake, large size + 2 toppings


# Running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))
```

This results in the output: 


```py
..F.
======================================================================
FAIL: test_check_price (__main__.TestCakeFactory)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython-input-9-32dbf74b3655>", line 33, in test_check_price
    self.assertEqual(price, 13) # Vanilla cake, large size + 2 toppings
AssertionError: 14 != 13

----------------------------------------------------------------------
Ran 4 tests in 0.007s

FAILED (failures=1)
<unittest.runner.TextTestResult run=4 errors=0 failures=1>
```

The program calls the TextTestRunner() method, which returns a runner (TextTestResult). It says one failure occurred: the statement self.assertEqual(price, 13) was incorrect, as it should have been 14. How can we correct that part of the test? Update that part of the code to the following:

```python	
import unittest


# Fixing the test_check_price method
class TestCakeFactory(unittest.TestCase):
 # ... Other tests remain the same

 def test_check_price(self):
     cake = CakeFactory("vanilla", "large")
     cake.add_topping("sprinkles")
     cake.add_topping("cherries")
     price = cake.check_price()
     self.assertEqual(price, 14) # Vanilla cake, large size + 2 toppings

# Re-running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))
```

And now the program works as expected, as the results provide no failures and are: 

```py
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
<unittest.runner.TextTestResult run=1 errors=0 failures=0>
```

## Key takeaways

Unittest can assist developers in building a strong and effective code for their programs. The tools allow developers to test small, isolated functionality units to catch bugs and glitches that could potentially cause larger problems if run with the overall code program. 