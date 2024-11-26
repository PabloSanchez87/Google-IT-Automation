# Logging

Many Python programmers develop programs that require them to observe values to see what is going on by using `print()` statements. `print()` is a built-in Python function used for simple, immediate output to the console which can be used for debugging or quick information display. 

`Logging` is a more sophisticated and configurable logging framework that allows developers to control the level of detail, destination, and formatting of log messages. Logging makes it suitable for production-grade applications to track and analyze program behavior. print() statements are great for development, but for production, each one of these function calls increases overhead.

One example of `print()` statements causing negative overhead is if low-priority problems arise in a script. A third-party API endpoint isn’t responding in time, so the application tries again and isn’t able to get a response. In these cases, the system doesn't tell you that the system is broken.

For more severe problems, such as a totally offline server dependency or repeated denials for incorrect passwords, you want to know immediately. For your logs, you want to filter out errors that may go away due to external factors (data about outages and potential breaches). 

When logging problems occur, they generally do not happen in isolation. Having a massive amount of noise inside log files can make it hard to trace problems. This ideology is pointed out in the “Observing Application Behavior” chapter of Michal Jaworski’s book, Expert Python Programming, 4th edition. 