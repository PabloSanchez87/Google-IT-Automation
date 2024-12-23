# Exception handling examples

In Python, we can prevent errors or we can catch them by using exceptions. The frequently-used exception commands are `try/except`, `raise`, and `finally`. 

`try/except` is like a safety net that catches errors and prevents your program from crashing. 

`raise` is like a red flag that alerts you to a problem. 

`finally` is like a parachute that helps you land safely,  even if your program crashes. 

## Using `try/except`

Use `try/except` when you think your code may raise an error. For example, opening a file may raise an error if the file does not exist or cannot be opened. Connecting to another host on the network raises an error if the host is unavailable. Rather than allowing the program to crash, `try/except` allows you to catch the error by providing an error message.  

Let’s take a look at an example. This function tries to print the value of x. If x has not been defined yet, print() will raise a `NameError`.

```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")

#Output:
Variable x is not defined
```

Another example shown below tries to append data to a file. If the file is not found, it prints a message. If there is any other error (such as “permission denied”), it prints the actual error. Finally, if there is no exception, it closes the file.

```python
try:
  f = open("/etc/hosts", "w+")
  f.write("Success!")
except FileNotFoundError:
  print("Data file not found")
except Exception as ex:
  print("Error appending to file: " + str(ex))
else:
  f.close()

#Output
Error appending to file: [Errno 30] Read-only file system: '/etc/hosts'
```

## Using `raise`

Use `raise` when your code cannot continue to execute due to an error or incorrect input. 

This example will raise a `TypeError` if x is not an integer value:  

```python
x = "hello"


if not isinstance(x, int):
  raise TypeError("Only integers are allowed")

#Output:
Error on line 5:
    raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed
```

The example below takes one argument and validates it. It raises either a `TypeError` or `ValueError` if it is invalid. This function first checks to make sure that the port number is an integer. If it is not an integer, the function raises a TypeError exception. The function then checks to make sure that the port number is between 1024 and 65535. This is because port numbers below 1024 are typically reserved for system services. If the port number is outside of this range, the function raises a ValueError exception. If the port number is valid, the function then starts the server on that port.

```py
def start_server(port):
  if not isinstance(port, int):
    raise TypeError("Port number must be an integer")
  elif port < 1024 or port > 65535:
    raise ValueError("Port number is invalid")
```

## Using `finally`

You use a `finally` block to clean up after executing a code, whether that code raises an exception or not. It is often used to clean up resources like network connections or to return a value to the calling function. For example, you can use finally to close a file or a database connection after you’re done. 

Make sure your finally block doesn’t accidentally throw another exception. Let’s see an example:  

```py
try:
  f = open("/etc/hosts", "w+")
except:
  print("Error appending to file: " + str(ex))
finally:
  f.close()  # causes error if the file could not be opened
```
If opening the file causes an exception, then f has no value, and the finally block will cause another exception that will not be detected.

## Key takeaways
The exceptions in Python help you catch the code errors. These commands include `try/except`, `raise`, and `finally`. The `try/except` exception allows you to catch errors before they happen. The `raise` exception is used when your code cannot continue to execute due to an error or incorrect input and alerts you. The `finally` exception helps you clean up after executing a code, whether that code raises an exception or not.  
