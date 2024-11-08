
# Resources for debugging crashes

## Comprehensive resources for debugging crashes

As you progress in handling complex code, debugging can become more challenging. However, there’s no need to worry; we’ve got resources to help you with advanced scenarios.

A top suggestion is to use a debugger of your choice and apply the techniques we’ve covered earlier in this course. This means setting breakpoints, checking variables, and going through your code step-by-step. These skills will greatly improve your ability to spot and fix issues in your software effectively.

To tackle software crashes, it’s crucial to understand debugging tools and techniques. That’s why we’ve gathered helpful resources to guide you. They’ll help you grasp the intricacies of debugging, even tricky concepts like concurrency and segmentation faults. Plus, you’ll find real-world examples with easy-to-read Python code on GitHub. So, let’s dive into these resources and simplify debugging for you.

## Debugging tools and techniques

There are a few resources you can use to help you with concurrency and debugging your programs. In the article [Speed up your Python program with concurrency](https://realpython.com/python-concurrency/), you find an in-depth exploration of Python concurrency concepts and how they can lead to potential crashes. Understanding concurrency pitfalls is essential for diagnosing complex issues related to parallel execution.

Another great article is [Threaded asynchronous magic and how to wield it](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32) on the [HackerNoon](https://hackernoon.com/) website. This article delves into the complexities of threaded asynchronous programming and offers insights into debugging techniques specific to asynchronous code, which can often result in hard-to-trace crashes.

## Diagnosing segmentation faults

A segmentation fault—sometimes referred to as a segfault—occurs when your Python program attempts to access a location in memory that it isn’t allowed to access or is read-only. Refer to the [Definitive list of common reasons for segmentation faults](https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults) article for a list of common reasons behind segmentation faults, along with detailed explanations. Understanding these reasons is fundamental to troubleshooting crashes related to memory access violations.

Another article you can use for information on segmentation faults is [Debugging segmentation faults](https://sites.google.com/a/case.edu/hpcc/hpc-cluster/ridermarkov-software/programming-computing-languages/cc/debugging-segmentation-faults?authuser=0) by Case Western Reserve University. Although this article was written for debugging segmentation faults in C and C++, you can use this information to help you with the same problem in your Python programs.

## Real-world code examples

Discovering and understanding real-world Python code can be an exciting journey, especially if you’re looking to enhance your programming skills. It’s like peering into the inner workings of a well-built machine to understand how it functions.

These real-world repositories on GitHub house such code—they are like treasure chests of knowledge waiting to be explored. Some of the invaluable resources for learning and debugging include these GitHub repositories:

- [Minecraft](https://github.com/fogleman/Minecraft)
- [CherryPy web framework](https://github.com/cherrypy/cherrypy)
- [Flask web application framework](https://github.com/pallets/flask)
- [Tornado web framework](https://github.com/tornadoweb/tornado)
- [Howdoi command line tool](https://github.com/gleitz/howdoi)
- [Bottle web framework](https://github.com/bottlepy/bottle/blob/master/bottle.py)
- [SQLAlchemy database toolkit](https://github.com/sqlalchemy/sqlalchemy)

By delving into this list of well-structured code, you’re not just learning how to write Python; you’re also gaining insights into common problems and the art of advanced debugging. On the other hand, although having access to these GitHub repositories is a valuable reference, we strongly advise beginners to prioritize the study of [complete applications](https://github.com/home-assistant/core). This approach tends to be more accessible and comprehensible.

## Key takeaways

As you continue to dive into these resources, remember that debugging crashes is both an art and a science. By understanding the principles behind concurrency, memory management, and debugging techniques, and by studying practical examples from real-world code, you’ll be better equipped to diagnose and resolve crashes effectively in your own projects.
