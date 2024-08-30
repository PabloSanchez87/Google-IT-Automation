# List Operations and Methods
## Knowledge
### Common sequence operations
Lists and tuples are both sequences and they share a number of sequence operations. The following common sequence operations are used by both lists and tuples:

- `len(sequence)` - Returns the length of the sequence.

- `for element in sequence` - Iterates over each element in the sequence.

- `if element in sequence` - Checks whether the element is part of the sequence.

- `sequence[x]` - Accesses the element at index [x] of the sequence, starting at zero

- `sequence[x:y]` - Accesses a slice starting at index [x], ending at index [y-1]. If [x] is omitted, the index will start at 0 by default. If [y] is omitted, the len(sequence) will set the ending index position by default.

- `for index, element in enumerate(sequence)` - Iterates over both the indices and the elements in the sequence at the same time.

Because integers are not iterable, they need to be converted to a range as such:

```python
for x in range(len(someList)):
    print(x)
# this will print out a numerical value up to the length of the original string
```

### List-specific operations and methods
One major difference between lists and tuples is that lists are mutable (changeable) and tuples are immutable (not changeable). There are a few operations and methods that are specific to changing data within lists:

- `list[index] = x` - Replaces the element at index [n] with x.

- `list.append(x)` - Appends x to the end of the list.

- `list.insert(index, x)` - Inserts x at index position [index].

- `list.pop(index)` - Returns the element at [index] and removes it from the list. If [index] position is not in the list, the last element in the list is returned and removed.

- `list.remove(x)` - Removes the first occurrence of x in the list.

- `list.sort()` - Sorts the items in the list.

- `list.reverse()` - Reverses the order of items of the list.

- `list.clear()` - Deletes all items in the list.

- `list.copy()` - Creates a copy of the list.

- `list.extend(other_list)` - Appends all the elements of other_list at the end of list

- `map(function, iterable)` - Applies a given function to each item of an iterable (such as a list) and returns a map object with the results

- `zip(*iterables)` - Takes in iterables as arguments and returns an iterator that generates tuples, where the i-th tuple contains the i-th element from each of the argument iterables.

### Tuple use cases

Remember, there are a number of cases where using a tuple might be more suitable than other data types:

- **Protecting data:** Because tuples are immutable, they can be used in situations where you want to ensure the data you have cannot be changed. This can be particularly helpful when dealing with sensitive or important information that should remain constant throughout the execution of a program.

- **Hashable keys:** Because they're immutable, tuples can be used as keys on dictionaries, which can be useful for complex keys.

- **Efficiency:** Tuples are generally more memory-efficient than lists, making them advantageous when dealing with large datasets.

#### The tuple() operator
The `tuple()` operator is used to convert an iterable (like a list, string, or set) into a tuple. Let's see an example:

```py
# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple, 
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)
```
This can sometimes lead to confusion, particularly when tuples are used in function calls or with operators that also use parentheses.

#### Tuples with mutable objects
Although tuples themselves are immutable, they can contain mutable objects, such as lists. This means that although the tuple cannot be modified (for example, you can't add or remove elements), the mutable elements within the tuple can be changed.

```py
# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = 'x'  
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])
```

#### Returning multiple values from functions
One of the most useful aspects of tuples in Python is their ability to return multiple values from a function. This allows a function to produce more than one result, providing flexibility and improving code readability.

Here's an example:
```py
def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

result = calculate_numbers(10, 2)
print(result)  # Outputs: (12, 8, 20, 5.0)
```

In the above function, the four arithmetic calculations are returned as a tuple, which can be assigned to a single variable (result), or "unpacked" into multiple variables:

```py
def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8
```
This is a powerful feature that makes Python functions extremely versatile.

#### List comprehensions
A list comprehension is an efficient method for creating a new list from a sequence or a range in a single line of code. It is a best practice to add descriptive comments about any list comprehensions used in your code, as their purpose can be difficult to interpret by other coders.

- `[expression for variable in sequence]` - Creates a new list based on the given sequence. Each element in the new list is the result of the given expression.

    - Example: `my_list = [ x*2 for x in range(1,11)]`

- `[expression for variable in sequence if condition]` - Creates a new list based on a specified sequence. Each element is the result of the given expression; elements are added only if the specified condition is true. 

    - Example: `my_list = [ x for x in range(1,101) if x % 10 == 0 ]` 

Note that tuples do not have comprehensions but a similar functionality can be achieved with: 

`tuple(i for i in (1, 2, 3))`

#### When to use for loops or list comprehensions

In Python, list comprehensions are generally used for creating new lists from existing ones in a concise and readable manner, especially when the task involves simple transformations or filtering of elements. 

for loops are more versatile and are preferred when the operation is more complex, requires multiple lines of code, involves statements other than expression (like print, pass, continue, break), or when you need to iterate over a list without creating a new one.

## Coding skills
### Skill Group 1

- Use a `for` loop to modify elements of a list.

- Use the `list.append()` method.

- Use the `string.endswith()` and `string.replace()` methods to modify the elements within a list.

    ```py
    # This block of code changes the year on a list of dates.
    # The "years" list is given with existing elements. 
    years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

    # The variable "updated_years" is initialized as a list data type 
    # using empty square brackets []. This list will hold the new list
    # with the updated years. 
    updated_years = []
    # The for loop checks each "year" element in the list "years".
    for year in years:
        # The if-statement checks if the "year" element ends with the 
        # substring "2023". 
        if year.endswith("2023"):
            # If True, then a temporary variable "new" will hold the 
            # modified "year" element where the "2023" substring is 
            # replaced with the substring "2024".
            new = year.replace("2023","2024")
            # Then, the list "updated_years" is appended with the changed
            # element held in the temporary variable "new".
            updated_years.append(new)
        # If False, the original "year" element will be appended to the 
        # the "updated_years" list unchanged.
        else:
            updated_years.append(year)

    print(updated_years) 
    # Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]
    ```

### Skill Group 2
- Use a list comprehension to return values

    ```py
    # This list comprehension creates a list of squared numbers (n*n). It
    # accepts two integer variables through the function’s parameters.
    def squares(start, end):
        # The list comprehension calculates the square of a variable integer 
        # "n", where "n" ranges from the "start" to "end" variables inclusively.
        # To be inclusive in a range(), add +1 to the end of range variable.
        return [n*n for n in range(start,end+1)] 

    print(squares(2, 3))  # Should print [4, 9]
    print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
    print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

### Skill Group 3
- Use a list comprehension to modify elements of a list.

- Use the `string.replace()` method within a list comprehension.

- Use the `string[index]` method within a list comprehension.

    ```py
    # This block of code also changes the year on a list of dates using a
    # different approach than demonstrated in Skill Group 1. By using a 
    # list comprehension, you can see how it is possible to refactor the
    # code to a shorter, more efficient code block. 

    # The "years" list is given with existing elements.
    years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

    # The list comprehension below creates a new list "updated_years" to
    # hold the command to replace the "2023" substring of the "year"
    # element with the substring "2024". This action will be executed if
    # the last 4 indices of the "year" string is equal to the substring
    # "2023". If false (else), the "year" element will be included in the
    # new list "updated_years" unchanged.
    updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]

    print(updated_years) 
    # Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]
    ```

### Skill Group 4
- Use the `string.split()` method to separate a string into a list of individual words.

- Iterate over the new list using a for loop.

- Modify each element in the list by slicing the element’s string at a given [1:] index position and appending the substring to the end of the element.

- Convert a list back into a string.

    ```py
    # This function splits a given string into a list of elements. Then, it
    # modifies each element by moving the first character to the end of the 
    # element and adds a dash between the element and the moved character. 
    # For example, the element "2two" will be changed to "two-2". Finally,
    # the function converts the list back to a string, and returns the
    # new string.
    def change_string(given_string):

        # Initialize "new_string" as a string data type by using empty quotes.`
        new_string = ""

        # Split the "given_string" into a "new_list", with each "element"
        # holding an individual word from the string.
        new_list = given_string.split()

        # The for loop iterates over each "element" in the "new_list".
        for element in new_list:
            # Convert the list into a "new_string" by using the assignment
            # operator += to concatenate the following items: 
            # + Each list "element" (starting at index position [1:]), 
            # + a dash "-", 
            # + append the first character of the "element" (using the index 
            # [0]) to the end of the "element", and finally,
            # + a space " " to separate each "element" in the "new_string".
            new_string += element[1:] + "-" + element[0] + " "

        # Return the list that has been converted back into a string.
        return new_string

    print(change_string("1one 2two 3three 4four 5five")) # Should print "one-1 two-2 three-3 four-4 five-5"  
    ```

### Skill Group 5
- Use the `string.join()` method to concatenate a string that provides a list name and its elements.
    ```py
    # This function accepts a list name and a list of elements, and returns
    # a string with the format: "The "list_name" list includes: element1, 
    # element2, element3". 
    def list_elements(list_name, elements):
        # This task can be completed in a single line of code. The 
        # concatenation of strings, "list_name", and the list "elements" can
        # occur on the return line. In this case, the string "The " is added 
        # to the "list_name", plus the string " list includes: ", then the
        # "elements" are joined using a comma to separate each element of the 
        # list.
        return "The " + list_name + " list includes: " + ", ".join(elements)

    print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))
    # Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"
    ```

### Skill Group 6
- Use `map()` and convert the map object to a list so we can print all the results at once.

    ```py
    # A simple function to add 1 to a given number
    def add_one(number):
        return number + 1

    # A list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Use map to apply the function to each element in the list
    result = map(add_one, numbers)

    # Convert the map object to a list to print the result
    print(list(result))

    # Outputs: [2, 3, 4, 5, 6]
    ```

### Skill Group 7
- Use `zip()` to combine a list of names and ages into a list of tuples, and print all the tuples at once.

    ```py
    # Two lists
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]

    # Use zip to combine the lists
    combined = zip(names, ages)

    # Convert the zip object to a list to print the result
    print(list(combined))

    # Outputs: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    ```

## Resources    
For additional information about list and tuple operations and methods, please visit:

- [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) - Official python.org documentation for list, tuple, and range sequence operations.

- [Lists](https://docs.python.org/3/library/stdtypes.html#lists) - Official python.org documentation for list operations and methods. 

- [Tuples](https://docs.python.org/3/library/stdtypes.html#tuples) - Official python.org documentation for tuple operations and methods  