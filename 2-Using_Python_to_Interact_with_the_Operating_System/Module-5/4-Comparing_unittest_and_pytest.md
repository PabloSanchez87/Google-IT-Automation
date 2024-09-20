# Comparing unittest and pytest
Both `unittest` and `pytest` provide developers with tools to create robust and reliable code through different forms of tests. Both can be used while creating programs within Python, and it is the developer’s preference on which type they want to use.

In this reading, you will learn about the differences between `unittest` and `pytest`, and when to use them.

## Key differences
`Unittest` is a tool that is built directly into Python, while `pytest` must be imported from outside your script. 

Test discovery acts differently for each test type. `Unittest` has the functionality to automatically detect test cases within an application, but it must be called from the command line. `Pytests` are performed automatically using the prefix test_. 

`Unittests` use an object-oriented approach to write tests, while `pytests` use a functional approach. 

`Pytests` use built-in assert statements, making tests easier to read and write. On the other hand, `unittests` provide special assert methods like assertEqual() or assertTrue().

Backward compatibility exists between `unittest` and `pytest`. Because unittest is built directly into Python, these test suites are more easily executed. But that doesn’t mean that pytest cannot be executed. Because of backward compatibility, the unittest framework can be seamlessly executed using the pytest framework without major modifications. This allows developers to adopt pytest gradually and integrate them into their code.

## Key takeaways
`Unittest` and `pytest` are both beneficial to developers in executing tests on their code written in Python. Each one has its pros and cons, and it is up to the developer and their preference on which type of testing framework they want to use. 