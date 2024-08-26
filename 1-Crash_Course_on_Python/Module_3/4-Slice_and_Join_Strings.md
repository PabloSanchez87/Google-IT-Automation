# Slice and Join Strings
Slicing a string is just like taking a slice out of a homemade apple pie. When it comes to strings, slices can be as small or as big as you want. If you want to put two or more of those slices back together, you join them together end-to-end—in Python speak, you “concatenate” them—to make one bigger, single string.

## What is slicing and joining strings?  
When you slice a string, you extract a subset of the original string—sometimes referred to as indexing a string. Joining strings is the process of linking two or more strings together to create a bigger string.

## How to slice strings 
Bracket notation, `[ ]`, is used to specify the start of the index, ending index, or both. If you do not include the starting index, then the slice contains everything from the beginning of the string to the ending index. This is the same if you do not include the ending index. Let’s look at a couple of examples:

**Pro tip:** Remember that the indexes in Python start with 0, and not 1.

```python
string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

#Output:
G
ting
Earthlings
Greet
```

**Note:** When you specify an ending index, Python slices everything up to, but not including the ending index. Notice in the second example the ending index is 8, but the characters sliced are 4–7.

If your index is negative, Python counts back from the end of the string instead of the beginning.

```python
print(string1[55:])     # Prints “” 
```

An optional way to slice an index is by the stride argument, indicated by using a double colon. This allows you to skip over the corresponding number of characters in your index, or if you’re using a negative stride, the string prints backwards.
```python
print(string1[0::2])    # Prints “Getns atlns”
print(string1[::-1])    # Prints “sgnilhtraE ,sgniteerG”
```

## How to join strings 
To join strings in Python, you use the plus operator, `+` , just as if you were adding two numbers together. The following example joins three strings together.

```python
print("Hello" + " " + "world") #Prints “Hello world”
```

## How to combine slicing and joining strings
Now you know how to slice strings and join strings. Now, let’s put the two operations together by taking an unformatted phone number, 2025551212, and return it as a properly formatted U.S. number. In this example, we’ll use phonenum to refer to the unformatted phone number.

```python
# The first 3 digits are the area code:
  area_code = "(" + phonenum[:3] + ")"
```

This function slices the first three numbers from the list.
```python
# The next 3 digits are called the “exchange”:
  exchange = phonenum[3:6]
```

This function slices the numbers 4–6 from the list.
```python
# The next 3 digits are the line number:
  line = phonenum[-4:]
```

This negative index function counts backwards from the end of the numbers, slicing the last four numbers in the list.
```python
# Put the pieces back together into a nicely formatted string:
  return area_code + " " + exchange + "-" + line
```

When you’re done, your code will look like this:
```python
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
```

Finally, we’ll use the print function to join the three previously sliced numbers together in the correct format. With this function definition, when you call print(format_phone("2025551212")), it will print (202) 555-1212. 
```python
print(format_phone("2025551212")) # Outputs: (202) 555-1212
```

## Key takeaways
Slicing and joining strings can be beneficial to correctly format numbers, making it easier to manipulate data in a more efficient and meaningful way. Slicing strings allows you to access individual characters of a string by specifying the index. The index can be as long or as short as you like—you can even have a negative index, if counting backwards is your thing! Joining strings allows you to add two or more strings together, which is beneficial when needing to create a sentence or even properly format different numbers.