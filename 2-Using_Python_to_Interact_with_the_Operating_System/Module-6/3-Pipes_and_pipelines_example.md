# Pipes and Pipelines

```bash	
ls -l | less
#(... A list of files appears...)
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
     # 7 the
     # 3 up
     # 3 spider
     # 3 and
     # 2 rain
     # 2 itsy
     # 2 climbed
     # 2 came
     # 2 bitsy
     # 1 waterspout.
```
- `ls -l | less`	
    - Description: Lists all files in the current directory using ls -l and pipes (|) the output to the less command, allowing for paginated viewing. This is useful when dealing with long outputs that don't fit on a single screen.
- `cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head`
    - Description: Analyzes the frequency of words in the file spider.txt using a combination of commands connected by pipes.

```bash	
cat capitalize.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())
```

- This Python script reads lines from standard input (STDIN), capitalizes the first letter of each line, and prints the modified line. It uses the sys.stdin to process input directly from the pipeline or file redirection.

```bash	
cat haiku.txt 
#advance your career,
#automating with Python,
#it's so fun to learn.
```	
- Displays the contents of the haiku.txt file, which contains a short haiku poem.

```bash	
cat haiku.txt | ./capitalize.py 
#Advance your career,
#Automating with python,
#It's so fun to learn.
```	
- Pipes the contents of haiku.txt to the capitalize.py script, which capitalizes the first letter of each line.

```bash	
./capitalize.py < haiku.txt
#Advance your career,
#Automating with python,
#It's so fun to learn.
```
- Uses input redirection (<) to feed the contents of haiku.txt to the capitalize.py script. This achieves the same result as the previous example but uses a different method to provide input to the script.