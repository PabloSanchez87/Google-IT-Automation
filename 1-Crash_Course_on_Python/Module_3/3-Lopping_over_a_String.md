# Looping over a String

Looping over a string allows programmers to examine each character within a string individually, gather information about its occurrences, and perform a given operation. 

There are multiple ways to loop over a string—some ways are more beneficial than others—and which one you choose depends on the information you need. 

## Looping over a string 

To loop over a string means to start with the first character in a string and iterate over each character until the end of the string. Strings are objects that contain a sequence of single-character strings. Yes, a single letter is classified as a string in Python. 

For example, `string[0] `is considered a string even though it is just a single character.

**Note:** Python does not use characters as a type like other programming languages do; it just supports strings with a length of 1.

## `for Loop`

The most direct—and common—way to loop over a string is to use the for loop. Let’s look at an example:

```python
greeting = 'Hello'
for char in greeting:
	print(char)
```

Notice that greeting is defined as the string 'Hello'. The loop begins with char = 0, which is the first element in the string. It directly calls the elements of the string and prints each element on a new line, resulting in the output below:

```python
# Output:
H
e 
l 
l 
o 
```

What if you don’t want the elements of the string but the position of the string instead? You’re in luck because Python can work that magic too!

```python
for i in range(len(greeting)):
	print(i)
```

`len(greeting)` is an integer that tells Python how many characters are in the string. But because it’s an integer, you need to convert it to an iterable sequence by using the range() function. This loop does the same thing as the loop above, but instead of printing elements, it prints integers resulting in the output below:

```python
#Output:
0
1
2
3
4
```

## `while loop with indexing`

This `while` loop is the more “common” `while` loop that programmers often use. This type of loop involves an index variable to represent the current position within the sequence. Most of the time, this will start with 0 for the initial iteration. Let’s take a look at an example:

```python
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1    
```

The initial index value is 0, and the `while` loop continues to execute as long as the index variable is less than the length of the `len(greeting)`. At each iteration, Python prints the value at the current index position (`greeting[index]`). Then, Python increments the index by 1 (`index += 1`) to move to the next position. The output of this example is:

```python
#Output:
H
e
l 
l 
o 
```

**Pro Tip:** In any while loop, you can add conditional statements and stop the iteration process early so that the loop does not examine every character.

## `while loop with slicing`
Using a `while` loop with slicing accomplishes the same thing that a `while` loop with indexing does, like the example you explored above, this is just another way to write a `while` loop. 

You use this `while` loop in combination with string slicing to iterate over a portion of a sequence. Remember, it’s up to you to choose the method for looping over a string based on your level of comfort. There are multiple ways to write lines of code to execute the same result. Let’s explore how a `while` loop with **slicing** results in the same output.

```python
greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1
```

This while loop continues to run as long as the index variable is less than the length of the string, which is determined by using len(greeting). With each iteration, a substring of length 1 is extracted using (`greeting[index:index+1]`) and printed. Then, the index is incremented by 1 (`index += 1`) to move to the next position. 
```python
#Output:
H
e
l 
l 
o 
```

## `List comprehensions`
List comprehensions are a concise way to create lists in Python. Let’s look at an example:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)
```

This example starts with a list of numbers. The second line of code defines the type of transformation you want to execute on each element in the original list. In this case, you’re using this line of code to create a new list called squared_numbers and apply x ** 2 to square each element in the numbers list. The result of each squared element is then printed in a new list:

    [1, 4, 9, 16, 25]

**Note:** List comprehensions can include conditional statements and nested loops, which allows for additional filtering of elements based on specific called conditions.

## Additional advanced string loop techniques
There are additional ways to loop over a string in Python that you should learn, practice, and master. These additional looping techniques include the generator functions, `map()`,  and `zip()`. The `map()` and `zip()` functions are extremely powerful string manipulation tools that demonstrate functional programming concepts. To learn more about these advanced techniques, see these resources:
- [Python - map() function](https://www.tutorialsteacher.com/python/python-map-function)

- [Python zip() method](https://www.tutorialsteacher.com/python/zip-method)

**Pro Tip:**  Looping over multiple strings at once can push the limits of for loops. Because of this, it’s important to be aware of other alternatives to simplify a for or while loop.

## Key takeaways
When you loop over a string, you are able to examine each individual element in the string and manipulate it how you’d like. A `for` loop iterates over each element, and a `while` loop allows you to add conditional statements and stop the iteration process early. As you saw in this reading, there are a variety of methods to loop over a string. It’s up to you to familiarize yourself with each technique and write code according to the advantages and disadvantages of each.  