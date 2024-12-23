# Logging

Many Python programmers develop programs that require them to observe values to see what is going on by using `print()` statements. `print()` is a built-in Python function used for simple, immediate output to the console which can be used for debugging or quick information display. 

`Logging` is a more sophisticated and configurable logging framework that allows developers to control the level of detail, destination, and formatting of log messages. Logging makes it suitable for production-grade applications to track and analyze program behavior. print() statements are great for development, but for production, each one of these function calls increases overhead.

One example of `print()` statements causing negative overhead is if low-priority problems arise in a script. A third-party API endpoint isn’t responding in time, so the application tries again and isn’t able to get a response. In these cases, the system doesn't tell you that the system is broken.

For more severe problems, such as a totally offline server dependency or repeated denials for incorrect passwords, you want to know immediately. For your logs, you want to filter out errors that may go away due to external factors (data about outages and potential breaches). 

When logging problems occur, they generally do not happen in isolation. Having a massive amount of noise inside log files can make it hard to trace problems. This ideology is pointed out in the “Observing Application Behavior” chapter of Michal Jaworski’s book, Expert Python Programming, 4th edition. 

You might want to set up a way to notify someone in case problems arise. Filtering problems by severity level is a fantastic place to start. Logging allows this filtering with the levels: 
- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

## Printing vs. logging
Printing and logging are both methods you can use to display information, but they serve slightly different purposes and have different implications, depending on the context.

### Printing	

`print()` is a function that prints objects (strings, but also most anything else). The syntax for using the print() function to print to a file is: 

```python
print(open(“my_file.txt”,”r”).read(),file=open(“new_file.txt”,”w”))
```	

`print()` objects sent to the text stream file must be provided as keyword arguments if they are separated by sep. These statements might also be followed by end. sep, end, file, and flush.

The stream file is generally what you interact with, but sometimes you will not use Python with console output, especially in a cloud context where code is deployed that runs on some other computer. In most cases, anything printed out inside the Python code will end up in logs. This is because logs capture all or nothing regarding print().

### Logging
The logging module provides an object-oriented way to print out statements with the additional advantage of using severity levels. More advanced features include the ability to filter which messages you care about, to route to more destinations than just the console/terminal, and to see the difference between normal print() statements and print() statements used for debugging purposes.

## Built-in logging levels 

The logging module provides five built-in log levels. In order of severity, they are `debug`, `info`, `warning`, `error`, and `critical`. These are referred to as methods of the logging object. 

The output of a logging statement will resemble:

```
[LOG_LEVEL]:root:[MESSAGE]  
```

The name “root” in this context means logging was called directly instead of setting up a logger by name.

The following is an example of import logging:

```python
# Set up basic configuration to display all log levels

logging.basicConfig(level=logging.DEBUG)

# Log messages for each severity level

logging.debug("This is a DEBUG message.")

logging.info("This is an INFO message.")

logging.warning("This is a WARNING message.")

logging.error("This is an ERROR message.")

logging.critical("This is a CRITICAL message.")
```

This prints out:

```
DEBUG:root:This is a DEBUG message.

INFO:root:This is an INFO message.

WARNING:root:This is a WARNING message.

ERROR:root:This is an ERROR message.

CRITICAL:root:This is a CRITICAL message.
```

This print out includes all of the pre-defined logging points.

## Handlers

Handlers are advanced ways to manage and route logs. Handlers define the output destinations for log messages, allowing you to control where the log data goes, such as writing to files, sending emails, or printing to the console. 

The most basic handler is `StreamHandler`. The `StreamHandler` class allows you to configure logging to display log messages on the screen, making it useful for providing feedback, debugging, and monitoring during the execution of a program. This is the `print()` equivalent for logging, but StreamHandler also allows routing from arbitrary objects. Handlers can be attached to user-defined loggers using `addHandler()` or can be directly invoked.

Here is an example of a custom logger with a `debug` and a `StreamHandler` attached to it with a different severity level:

```python
import logging

# Setting up the logger and StreamHandler
# Creating a logger
stream_logger = logging.getLogger('stream_logger')

stream_logger.setLevel(logging.DEBUG)  # Set logger to capture all messages from DEBUG level and above

# Ensure no previous handlers are attached
stream_logger.handlers = []

# Creating a StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Set handler to display only messages from INFO level and above

# Adding handler to logger
stream_logger.addHandler(stream_handler)

# Logging messages at different levels
stream_logger.debug("This is a DEBUG message for stream_logger.")
stream_logger.info("This is an INFO message for stream_logger.")
stream_logger.warning("This is a WARNING message for stream_logger.")
stream_logger.error("This is an ERROR message for stream_logger.")
stream_logger.critical("This is a CRITICAL message for stream_logger.")
```

Output:

```text
This is an INFO message for stream_logger.

This is a WARNING message for stream_logger.

This is an ERROR message for stream_logger.

This is a CRITICAL message for stream_logger.
```

### Different types of logging handlers

Besides StreamHandler, there are also many other handlers: 

- FileHandler

- NullHandler

- WatchedFileHandler

- BaseRotatingHandler

- RotatingFileHandler

- TimedRotatingFileHandler

- SocketHandler

- DatagramHandler

- SysLogHandler

- NTEventLogHandler

- SMTPHandler

- MemoryHandler

- HTTPHandler

- QueueHandler

- QueueListener

For more information about logging handlers, click [here](https://docs.python.org/3/library/logging.handlers.html). 

## Logging business data to a database

An advanced use case, but one very common in most cloud operations, is logging business-relevant data, such as logins and expensive requests, to a database. This logging would also generate alerts for outages and other items that require immediate attention. 

To do this with Python logging, one may combine the capabilities of the logging library with a database library. This enables the creation of custom handlers or loggers that interact with the database, allowing seamless storage and retrieval of crucial operational data to enable effective monitoring.

## Key takeaways
These takeaways emphasize the significance of logging for effective software development and production monitoring, as well as the distinction between using `print()` statements and the more structured approach of logging with severity levels and handlers.  

- `Overhead of print()statements in production:` Although using print() statements is convenient for development, it can lead to increased overhead in production environments. 

- `Distinguishing severity levels for effective monitoring:` Differentiating between various issues' severity levels is crucial. By using severity levels in logging, you can effectively filter out transient errors and monitor significant problems.

- `Using logging handlers for advanced log management:` Logging handlers are essential components for directing log messages to various destinations. They provide advanced capabilities, such as filtering messages, routing to multiple destinations, and enabling custom loggers.  

