
# More about managing resources

You've learned a lot about how to avoid memory leaks and manage your OS and network to achieve the best performance. Let’s look at a few more ways you can speed up your application processing and troubleshoot memory and system performance.

## Using concurrency and threading

Python has several tools to streamline the processing of code, including `threading`, `multiprocessing`, and a library called [`asyncio`](https://docs.python.org/3/library/asyncio.html).

With these, you can run things (threads, tasks, and processes) in an overlapping fashion, called **concurrency**. Similarly, you can use **asynchronous threading**, where you can tell the OS to prioritize certain threads over another. Although these are similar, they each have their own advantages.


### Concurrency

Depending on your application’s resource needs, you may be able to use concurrency to help speed up things that are slowing down processing. Concurrency involves adding a bit of extra code to your programming to allow it to run multiple things in a sequence, but with overlapping time frames. For example, you could have hundreds of threads or requests, but you can set them to run on top of each other, instead of waiting for one to complete before the next starts.

In I/O-bound programming, where there is a lot of interfacing with networks or other hardware, using concurrency can help download network-based content faster and more efficiently. In CPU-bound programming, where the program is busy processing data, you can use concurrency to spread heavy CPU processes across multiple threads or requests, but that adding concurrency to your code means ... it’s that right more coding, and that introduces a greater risk of introducing hard-to-find errors into your program.

Learn all about concurrency, different forms of multitasking, ways to enable concurrency outside of asyncio, and much more in this in-depth and helpful [article](https://realpython.com/python-concurrency/). And, for a good overview with clear examples of what concurrency is, read this [article](https://freecontent.manning.com/concurrency-vs-parallelism/).

### Asynchronous threading

Unlike concurrency, which involves processing things in a stacked order, we can also use **threading**—running multiple things at the same time—to increase efficiency.

For example, you might set up your threads like this:

```python
import threading

def thread_function(name):
    print("Thread {} is running".format(name))

if __name__ == "__main__":
    # Create two threads
    thread1 = threading.Thread(target=thread_function, args=("Thread-1",))
    thread2 = threading.Thread(target=thread_function, args=("Thread-2",))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to finish
    thread1.join()
    thread2.join()

    print("All threads finished")
```

### Checking memory usage

Memory leaks can be a big problem when coding because they slow down the processing of your application and may create crashes. When you can evaluate programming to find issues, you can then streamline your code and/or processes to release code cleanly.

Although Python automatically manages memory as part of its language, there are several other tools you can use to look for memory leaks to ensure yours is running as efficiently as possible.

If you’re looking at a section of your code that you suspect may be slowing your application, there are packages, such as [`memory-profiler`](https://pypi.org/project/memory-profiler/), that will evaluate a single function or code, line by line, to show detailed memory use. You can also use it to evaluate your application’s memory usage over time, helping identify memory that isn’t releasing as regularly as it should.

If you need to look at the application as a whole, try [guppy](https://zhuyifei1999.github.io/guppy3/), a library to view and evaluate memory use by different object types.

For more about memory-profiler and other tools, read this [article](https://www.pluralsight.com/resources/blog/software-development/how-to-profile-memory-usage-in-python).

### Checking for network problems

If you’re not a network administrator or engineer, all those acronyms and their configurations can be a bit of a mystery. Lucky for you, you have some in-built tools to help you identify the source of the problem.

The first thing to try is to ping the server to see if it’s a server issue or an actual network issue.

You can also use `ipconfig` / `all` (Windows) or `ifconfig -a` (Linux) to show IP addresses and DHCP connections.

For more examples and details, check out this [article](https://www.linuxjournal.com/content/troubleshooting-network-problems).

## Key takeaways

Many things may cause performance issues in your programming, from memory leaks to network issues, to slow processing times. By knowing some simple tricks to code, scan, and troubleshoot, you can help your program run efficiently as possible.
