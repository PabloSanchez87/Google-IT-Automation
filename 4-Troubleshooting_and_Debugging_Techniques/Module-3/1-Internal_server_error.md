# Internal server error
Have you ever tried to access a website but received an error message? There’s a good chance it was an HTTP 500 internal server error response code. These server error codes respond when something goes wrong while processing the request. As a software developer, if an internal server error appears, it is important to determine what and where the error is, correct it, and understand why it occurred to avoid the same type of error in the future.

In this reading, you will learn more about different internal server errors, why they occur, and view a typical message that users see if one exists.


## What is an internal server error?
An internal server error is a Hypertext Transfer Protocol (HTTP) response, communicating to the user that an error occurred before completing a specific request. In short, the server tried to do something, but it failed. The most common internal server error is an HTTP 500 error, but other common error codes include 200, 301, 302, 304, 403, 404, and 503. Here is an example of what an internal server error might look like in a browser:

![alt text](/resources/error505.png)

A Google website that displays a 500 error message informing the user that something is wrong with the server.

## Why do internal server errors occur?
Internal server errors can occur for different reasons, including various glitches in the website’s programming. Typically, this type of error occurs when there are bugs in the code. They can also occur if a database becomes unavailable, the server runs out of memory, or the application encounters a permission error. The downside to internal server errors is that they do not provide you with information on what exactly is wrong. As a developer, the error code only provides the general type of error occurring. Run different tests or set various parameters to try to reproduce the error. If you can reproduce the error, that will help you identify the issue and correct it.

## Key takeaways 
An internal server error is displayed when a web server cannot fulfill or complete a request. An internal server error informs you that an error exists but does not tell you exactly what the error is or where it is located. Troubleshoot by running tests to determine what and where the bugs are in your code and correct them to eliminate internal server errors.

