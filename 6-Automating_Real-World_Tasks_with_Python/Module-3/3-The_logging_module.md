# The logging module

The `logging module` in Python is a readily available, robust module that can be used by both novice programmers and professional teams. Because the majority of Python third-party libraries use it, you can combine your log messages with messages from both libraries to create a uniform log for your application.

Many applications, especially backend components that don’t directly interact with users, keep a log of their activities to aid in troubleshooting problems or monitoring the application’s performance. 

The Python logging module provides a standardized way of outputting those log messages to the system console, a file, the system logging daemon (`syslogd`), or other destinations.

Developers will often insert code that logs any or all of the following:

- Actions the program is about to take, is taking, or just completed

- The value of parameters and variables that might affect the program’s behavior

- Return values or output from other components (such as web services or databases)

- Timing and other performance data

You can customize both the formatting of your log and the level of detail that gets logged.


## Five levels of the logging module

A developer decides on a “severity” for each log message. The logger is configured to log anything above a certain severity level; everything else gets ignored.

The severity levels are as follows:

- `DEBUG:` Extra information only needed for debugging. This level often includes values of parameters and variables to help with troubleshooting. Example: logging Parameter x: 42 to aid in diagnosing issues and include parameter values

- `INFO:` Informational message that can be used for tracing the program’s activities. Example: connecting to MySQL database at mydbserver.aws.amazon.com

- `WARNING:` An error that doesn’t require immediate action. Examples: query took longer than 10 seconds, configuration file not found, or reverting to default settings.

- `ERROR:` Serious, but can be a recoverable error. Example: database connection failed, or a file is missing.

- `CRITICAL:` Fatal error. Example: A critical error has occurred! The application will now terminate.

You decide how much detail to put into your log file. Many programs have a `“DEBUG”` flag that you can turn on to output additional debugging information. When things go wrong, more detail is always better than less, especially at the `DEBUG` level. Most of the time you can leave your logging at `INFO` to keep the log readable, but don’t be afraid to throw additional logging into your code. 

If you initialize the logger with `INFO` as the minimum level, then the log will contain everything from `INFO` to `CRITICAL`. `DEBUG` messages will be discarded.

You can configure your logger to include multiple handlers; each one logs to a different destination. This way, you can log to the console and to a file at the same time, with a different level of detail (minimum severity level) for each destination.

## Initializing a logger

Initializing the logger typically refers to the process of setting up and configuring a logging system using the built-in logging module. Initializing the logger involves creating a logger object, specifying its configuration, and defining how log messages should be handled and formatted. 

The steps involve the following: 
- Import the logging module
- Create a logger instance
- Configure the logger
- Start logging messages.  

A simple way to initialize the logger is the following:

```python
# Set the minimum logging level to INFO,
logging.basicConfig(level=logging.INFO)

# Get a logger object
log = logging.getLogger(__name__)

# Start the log file
log.info("Hello world")
```

The `__name__` parameter adds your Python module name to the logger’s output, so if your module is called stuff.py, your log would include “[stuff]” in its output. This way, multiple modules can log to the same file, but you can still quickly find messages from a particular module.

## Alternatives to the logging module 
One popular alternative is `structlog`, which outputs logs in a highly structured JSON format so they can be easily parsed by monitoring systems. With structlog, log messages are not only strings but rich data structures, which can make it easier to search, filter, and analyze logs.

Another is `colorlog`, which adds helpful color highlights when logging to the console. An example of this is assigning different colors to log levels like `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`. This step can make it quicker to spot the severity of each log message at a glance.  

The good news is that these alternatives are nearly drop-in replacements for the built-in logging module, so you don’t need much in the way of code changes to use them. The flexibility of these alternatives means a smooth transition requiring minimal code modifications to integrate them into your Python applications.


## Key takeaways
Python's built-in logging module is a tool suitable for both beginners and experienced programmers, making it a valuable choice for creating uniform logs in applications with third-party libraries. The logging module simplifies the process of recording and outputting log messages, enabling developers to track program activities, parameter values, errors, and performance data in a standardized manner. Developers can customize the format and level of detail in their log files, with five severity levels ranging from DEBUG for debugging to CRITICAL for fatal errors. Initializing the logger involves setting the minimum logging level, creating a logger instance with a module name, and starting the log, making it straightforward for developers to get started with logging.  