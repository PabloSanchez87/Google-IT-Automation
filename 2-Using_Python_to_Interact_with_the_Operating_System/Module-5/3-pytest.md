# pytest
`Pytest` is a powerful Python testing tool that assists programmers in writing more effective and stable programs. It helps to simplify the process of writing, organizing and executing tests. It can be used to write a variety of tests including: integration, end-to-end, and functional tests. It supports automatic test discovery and generates informative test reports. 

In this reading, you will learn more about pytests, how to write tests with pytest, and its fixtures.

## How to write tests with pytest
Pytests are written with functions that use the operation, `assert()`. 

An `assert` is a commonly used debugging tool in Python that allows programmers to include sanity checks in their code. They ensure certain conditions or assumptions hold true during runtime. 

**If the condition provided to assert() turns out to be false, it indicates a bug in the code, an exception is raised, and halts the program’s execution.** 

Typically, code provides an assert condition followed by an optional message. An example is: 

```python
def divide(a, b):
	assert b != 0, "Cannot divide by zero"
	return a / b
```

```python	

divide(10, 2)
divide(10, 0)


---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[2], line 6
      3 	return a / b
      5 divide(10, 2)
----> 6 divide(10, 0)

Cell In[2], line 2
      1 def divide(a, b):
----> 2 	assert b != 0, "Cannot divide by zero"
      3 	return a / b

AssertionError: Cannot divide by zero
```

An AssertionError message is raised informing the programmer that it is not possible to divide a value by zero.

## Pytest fixtures

**Fixtures are used to separate parts of code that only run for tests.**

They are reusable pieces of test setups and teardown code that are shared across multiple tests. Fixtures benefit developers by assisting in keeping their tests clean and avoiding code duplication. Let’s look at an example of using a pytest in Python:


```python	
import pytest
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False


    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()


    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)


    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
```

In this example, `test_fruit_salad` requests `fruit_bowl`. When pytest recognizes this, it executes the fruit_bowl fixture function and takes the object it returns into `test_fruit_salad` as the `fruit_bowl` argument. 

## Key takeaways

Pytest is a user-friendly testing framework for developers writing code in Python to focus on creating simple and clear tests. Pytests are written using the `assert()` operation to compare actual values with expected results. 

Fixtures provide developers a way to share common test data and environment configurations while ensuring consistent testing conditions.  