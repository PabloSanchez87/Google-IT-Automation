# Exception handling

Exception handling in Python is a method that allows developers to manage errors or exceptions that can occur during the execution of a program. Exceptions are errors that disrupt the normal flow of a program where the code cannot recover from automatically.

Some examples of exceptions are the following:

- Attempting to divide by zero

- Referencing a variable that doesn’t exist

- Attempting to open a file that doesn’t exist

- Connecting fails to a remote server

Exception handling is special code you can add to your program to ensure that a program doesn't crash when an error occurs. This method also provides the opportunity to respond to errors in a controlled and meaningful way.

## The most common types of exceptions

When an error arises while a program is being executed, one of Python's built-in exceptions may occur. Some of the most common exception types in Python are the following: 

- `NameError` - usually due to a typo in a variable name

- `AttributeError` - also usually a typo, in calling a method on an object

- `ValueError` - parameter value is incorrect

- `TypeError` - sending a string when a function is expecting an int or calling a function with the wrong number or type of arguments

- `ImportError` - when Python can’t find a module you’re trying to import

- `FileNotFoundError` - when you try to perform file-related operations (opening, reading, writing, or deleting) on a file or directory that does not exist

### `except` statements

In Python, you use the `except` statement as part of exception handling to catch and handle specific types of exceptions that may occur during the execution of a program. It is used to recover from the error or notify the user. 

An example of an `except` statement is:

```python
try:
  # Try to append to a file that is normally not writable
  # for anyone other than root 
  f = open("/etc/hosts", "w+")
except IOError as ex:
  # The variable "ex" will hold details about the error
  # that occurred
  print("Error appending to file: " + str(ex))
else:
  # If there was no exception, close the file.
  f.close()
```

## Differences with syntax errors and exceptions
As the name implies, syntax errors result from incorrect syntax in the code. They cause Python to terminate the program. Syntax errors usually occur due to typographical errors in the code, such as incorrectly indenting a line or misspelling a variable or function name. 

When a program is syntactically accurate, yet the code produces an error, exceptions occur. Although this error does not prevent the application from running, it alters how the program normally runs.

Syntax errors are related to the structure and grammar of the code and are detected before the program runs; whereas, exceptions are runtime errors that occur while the program is executing and are typically related to unexpected conditions or invalid operations. Syntax errors prevent the program from running, while exceptions can be caught and handled to allow the program to continue running despite encountering errors.

## Avoiding defensive code

Defensive code is a type of coding that aims to anticipate and handle exceptional conditions, errors, or unexpected inputs in a way that prevents the program from crashing or behaving unpredictably. Python coders, also known as Pythonistas, generally say “it’s better to ask forgiveness than permission.” This means that rather than adding lots of defensive code, you should just operate as usual and catch exceptions if they occur.

That means, instead of doing this:

```python
if isinstance(user, dict) and "first_name" in user:
  first_name = user["first_name"]
```

Do this instead:

```python
try:
  first_name = user["first_name"]
except KeyError:
  print("User does not have a first_name field")
```

## Key takeways
Exception handling in Python is a mechanism that allows you to handle errors and exceptional situations that may occur during the execution of a program. There are a great deal of exception types, but some of the most common are `NameError`, `AttributeError`, `ValueError`, `TypeError`, and `ImportError`. Syntax errors are related to the code's structure and grammar and are detected before the program runs.  In contrast, exceptions are runtime errors that occur during program execution, often due to unexpected conditions or invalid operations.   

