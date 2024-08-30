# List Comprehension Examples

You can create a list from an iterable using a for loop, which is a useful way to iterate over an iterable:

```python
new_list = []
for thing in list_of_things:
    new_list.append(do_something(thing))
```

There is also a more streamlined way to do this by using a list comprehension. A list comprehension allows you to create a new list from an iterable in a single line. This line achieves the same result as the previous for loop, but in a more concise way:

```py
new_list = [do_something(thing) for thing in list_of_things]
```

List comprehensions can be used with tuples in Python, too. Here is an example of a list of tuples. In this example each tuple will contain the numbers 1, 2, and 3. This code will create 5 sets of (1,2,3).

```py
# Create a list of tuples where each tuple contains the numbers 1, 2, and 3.
numbers = [(1, 2, 3) for _ in range(5)]
```

## `For` loop vs. list comprehension

The two code blocks below compare performing the same process using a list comprehension and a for loop. The line `[x*2 for x in range(1,11)]` is a simple list comprehension. This single line of code iterates over a range from 1 to 10, multiplies each element in the range by 2, and ultimately creates a new list from all multiples of 2 from 2 to 20. 

The second block of code below is a for loop designed to carry out the same function as the list comprehension. The for loop, however, requires three lines of code. 

```py

### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)

# Select Run to compare the two results.

#Output:
List comprehension result:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Long form code result:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## List comprehension with conditional statement
You can also use conditionals with list comprehensions to build even more complex and powerful statements. You can do this by appending an if statement to the end of the list comprehension. For example, `[x for x in range(1,101) if x % 10 == 0]` generates a new list containing all the integers divisible by 10 from 1 to 100. The if statement evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, the number is added to a new list.

```py
print("List comprehension result:")
print([x for x in range(1,101) if x % 10 == 0])

# The list comprehension above accomplishes the same result as
# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

# Select Run to observe the two results.

#Output
List comprehension result:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Long form code result:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

List comprehensions can be really powerful, but they can also be complex, resulting in code that’s hard to read. Be careful when using them, because they might make it more difficult for someone else looking at your code to easily understand what the code is doing. It is a best practice to add descriptive comments about any list comprehensions used in your code. This helps to communicate the purpose of list comprehensions to other coders. Comments will also help you remember the goal of the code when performing future code additions and maintenance. 

### Practice exercise

This exercise walks you through how to write a list comprehension to create a list of squared numbers (n*n or n**2). It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively. For example, squares(2, 3) should return a list containing [4, 9].

1. The function receives the variables “start” and “end” through the function parameters. 

2. In the `return` line, start by entering the list brackets [ ] that will contain the list comprehension.

3. Between the brackets [ ]:  
    a. Enter the arithmetic expression to square a variable “n”. 

    b. To the right of the square expression, write a `for` loop that iterates over “n” in a `range()` from the “start” to “end” variables.

    c. Ensure the “end” range value is included in the `range()` by adding 1 to it.

4. Run your code to see if it works!  If needed, the solution to this code is included in the “Study Guide: List Operations and Methods” reading under “Skill Group 2” (list comprehensions). 

```python
def squares(start, end):
    return [x**2 for x in range(start, end + 1)]

print(squares(2, 3))    # Should print [4, 9]
print(squares(1, 5))    # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))   # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```




