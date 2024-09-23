# Handling Errors

In some cases, **it’s better to raise an error yourself**, and how to test that the right error is raised when that's what you expect. You’ve also learned how to test your code to verify that it does what it should. 

In this reading, you’ll learn about error handling syntax, including raising exceptions, using an assert statement, and the try and except clauses. 

## Exception handling

When performing exception handling, it is important to predict which exceptions can happen. Sometimes, to figure out which exceptions you need to account for, you have to let your program fail.

The simplest way to handle exceptions in Python is by using the `try and except clauses`. 

In the `try` clause, Python executes all statements until it encounters an exception. You use the except clause to catch and handle the exception(s) that Python encounters in the `try` clause.

Here is the process for how it works: 

1. Python runs the `try` clause, e.g., the statement(s) between the `try` and `except` keywords.

2. If no error occurs, Python skips the except clause and the execution of the `try` statement is finished.

3. If an error occurs during execution of the try clause, Python skips the rest of the try clause and transfers control to the corresponding except block. If the type of error matches what is listed after the except keyword, Python executes the except clause. The execution then continues on after the try/except block.

4. If an exception occurs but it does not match what is listed in the `except` clause, it is passed onto try statements outside of that `try/except block`. However, if a handler for that exception cannot be found, the exception becomes an unhandled exception, the execution stops, and Python displays a designated error message. 

Sometimes, a `try` statement can have more than one `except` clause so that the code can specify handlers for different exceptions. This can help to reduce the number of unhandled exceptions.

You can use exceptions to catch almost everything. **It is good practice as a developer or programmer to be as specific as possible with the types of exceptions that you intend to handle, especially if you’re creating your own exceptions.**

## Raise exceptions
**As a developer or programmer, you might want to raise an error yourself.** 

Usually, this happens when some of the conditions necessary for a function to do its job properly aren't met and returning none or some other base value isn't good enough. You can raise an error or raise an exception (also known as “throwing an exception”), which forces a particular exception to occur, and notifies you that something in your code is going wrong or an error has occurred. 

Here are some instances where raising an exception is a useful tool:

- A file doesn’t exist

- A network or database connection fails

- Your code receives invalid input

In the example below, the code raises two built-in Python exceptions:  `raise ValueError` and raise `ZeroDivisionError`. You can find more information on these raises in the example below, along with explanations of potential errors that may occur during an exception.

## Example exception handling
Now that you have an understanding of `try` and `except` clauses, `assert` statements, and raising exceptions, consider the following code examples which use all of these concepts together.

The basic structure of exception handling is as follows: 

```python	
# File reading function with exception handling
def read_file(filename):
	try:
		with open(filename, 'r') as f:
			return f.read()
	except FileNotFoundError:
		return "File not found!"
	finally:
		print("Finished reading file.")
```

Imagine you have a function that reads data from a file and then divides two numbers provided within that file. There are some faults in it that you can catch with exceptions.

```python
def faulty_read_and_divide(filename):
	with open(filename, 'r') as file:
		data = file.readlines()
		num1 = int(data[0])
		num2 = int(data[1])
		return num1 / num2
```

There are several potential issues here:

- The file might not exist, causing a `FileNotFoundError`.

- The file might not have enough lines of data, leading to an `IndexError`.

- The data in the file might not be convertible to integers, raising a `ValueError`.

- The second number might be zero, which would raise a `ZeroDivisionError`.

To address these potential issues, you can add the appropriate exception handling illustrated below:

```python	
def enhanced_read_and_divide(filename):
	try:
		with open(filename, 'r') as file:
			data = file.readlines()
       	 
        # Ensure there are at least two lines in the file
        if len(data) < 2:
            raise ValueError("Not enough data in the file.")
       	 
        num1 = int(data[0])
        num2 = int(data[1])
       	 
        # Check if second number is zero
        if num2 == 0:
            raise ZeroDivisionError("The denominator is zero.")
       	 
        return num1 / num2


	except FileNotFoundError:
    	     return "Error: The file was not found."
	except ValueError as ve:
    	     return f"Value error: {ve}"
	except ZeroDivisionError as zde:
    	     return f"Division error: {zde}"
```
Now, the function `enhanced_read_and_divide` is equipped to handle potential exceptions gracefully, providing informative error messages to the caller. This way, the code will explain when it fails since you have identified potential fault zones such as when dealing with unpredictable inputs or file content.

Notice how the exceptions are instantiated as objects (such as `ValueError ve`) that you can use to further diagnose the issue by printing them out.

The errors should read:

```	
File-level issues:

Value error: Not enough data in the file.

Error: The file was not found.

Data-level issues:

Value error: invalid literal for int() with base 10: 'apple'

Division error: The denominator is zero.
```	

## Assert statements

`assert` statements help you to verify if a certain condition is met and throw an exception if it isn’t. As is stated in the name, their purpose is to "assert" that certain conditions are true at specific points in your program. 

The `assert` statement exists in almost every programming language and has two main uses:

- To help detect problems earlier in development, rather than later when some other operation fails. Problems that aren’t addressed until later in the development process can turn out to be more time-intensive and costly to fix.

- To provide a form of documentation for other developers reading the code.

## Key takeaways
For a bit of light reading, or for more information on raising exceptions, assertions, the try clause, exceptions, or handling errors, visit the following links:

- https://doughellmann.com/posts/python-exception-handling-techniques

- https://docs.python.org/3/tutorial/errors.html#raising-exceptions
 

- https://realpython.com/python-exceptions/

- https://realpython.com/python-raise-exception/#handling-exceptional-situations-in-python