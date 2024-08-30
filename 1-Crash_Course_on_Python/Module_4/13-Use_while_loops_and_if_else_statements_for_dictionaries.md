# Use while loops and if else statements for dictionaries
You’ve learned that `if` statements are used as a form of decision making. `If` statements tell your computer to perform a conditional execution based on the value of an expression. Using `else` in conjunction with an if statement allows your computer to evaluate `for` multiple conditions and run a statement if other conditions are `false`. In other words, else is the condition that runs if all other statements are not `true`.

You’ve also learned that `while` loops instruct your computer to continuously execute your code based on the value of a condition, but it will only continue to execute as long as the evaluation statement is `True`. Once that statement is no longer `True`, the loop exits and the next line of code will be executed. 

In this reading, you will learn about using `while` loops and `if else` statements for dictionaries, and see examples demonstrating the benefits of using them in your Python code. 

## `while` loops  
Dictionaries are used to organize elements into collections using pairs of keys and values. But what do you do when you need to search a collection of data for a value? That’s where `while` loops come in. A `while` loop will iterate through conditions until one comes up `False`, unlike a for loop, which will iterate through the entire dictionary, one row at a time. Consider the following example: 

```py 
for item in someDictionary:

    <code goes here>
```

versus:

```py
while someDictionary:

    <code goes here>
```

Notice the difference between the `for` loop and the `while` loop—unlike the `for` loop, the `while` loop does not require calling a variable to act as a counter, or the “item” variable in the `for` loop. `for` loops anticipate a specific structure—like a list—and when called, will iterate through the entire list, until it gets to the end.  `while` loops can be used more universally when the structure of your data set is more ambiguous. 

## `if else` statements 

`if else` statements are useful if you want to find and check for specific values and perform specific actions based on the result. Consider the following example:  

```py
# Check if a key exists in the dictionary and perform different actions based on the result
key = 'banana'
if key in myDictionary:
	print(f"The value of {key} is {myDictionary[key]}")
else:
	print(f"{key} is not found in the dictionary")
```

The goal here is to search if the key “banana” exists in the dictionary. The first line determines the key, “banana,” which is what we want to search for in the dictionary. The second line uses an if statement to search for the key within the dictionary and prints the value of that particular key `if` the condition is `True`. The `else` statement will return that the key was not found in the dictionary if the condition is `False`. As an example, this code block will return “The value of banana is 3” or “banana is not found in the dictionary” when it is run. 

## Key takeaways

`while` loops and `if else` statements are methods you can use to search for values within a dictionary. If you want to search through an entire dictionary quickly to find a value, use a `while` loop. If you want to search through a dictionary to find and check a value, use an `if else` statement to return the value and perform specific actions based on the result. 