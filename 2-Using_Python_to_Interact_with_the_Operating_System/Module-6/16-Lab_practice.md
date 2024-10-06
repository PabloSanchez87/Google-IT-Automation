
# Lab Summary: Edit Files Using Substrings

This lab involves scripting with Bash and Python to rename files in compliance with a company's naming policy. Below is a structured overview of the tasks completed during the lab.

## Introduction
In this lab, you practiced using several Linux commands and scripting techniques to modify filenames. The goal was to change the username in various files from `jane` to `jdoe` using both Bash and Python scripts. You learned to search, manipulate, and update file names using regular expressions, text processing commands, and automation through scripting.

## What You'll Do
- Practice using the `cat`, `grep`, and `cut` commands for file operations.
- Use `>` and `>>` commands to redirect I/O streams.
- Replace a substring using Python.
- Run Bash commands from within Python.

### Prerequisites
- Familiarity with the Linux environment and the following commands:
  - `cat`
  - `grep`
  - `cut`

## Exercise Overview

### Scenario
Your coworker Jane Doe currently has the username `jane` but needs to change it to `jdoe` to comply with the company's naming policy. While the username has already been changed, there are still several files named with Jane's previous username. For example, `jane_profile_07272018.doc` needs to be updated to `jdoe_profile_07272018.doc`.

### File Structure in `data` Directory
You began by listing the files in the `data` directory:

```
janez_profile_11042019.doc  jdoe_profile_07272018.doc  kwood_profile_04022017.doc  pchow_pic_05162019.jpg
jdoe_contact_07292018.csv   kwood_pic_04032017.jpg     list.txt
```

### Tasks
#### 1. Find Files Using Bash Script
You created a Bash script called `findJane.sh` that finds all files containing `jane` and stores them in a text file called `oldFiles.txt`. You used commands like `grep` and `cut` to extract the necessary information.

```bash
#!/bin/bash
grep " jane " ~/data/list.txt | cut -d ' ' -f 3 > oldFiles.txt
```

You then used `test` to check the existence of these files before storing their paths in `oldFiles.txt`. Once completed, you verified the results using:

```bash
cat oldFiles.txt
```

**Output:**
```
/home/student/data/jane_profile_07272018.doc
/home/student/data/jane_contact_07292018.csv
```

#### 2. Rename Files Using Python Script
Next, you wrote a Python script named `changeJane.py` to rename the files using the `subprocess` module. The script iterated over each line in `oldFiles.txt`, replaced `jane` with `jdoe` in the filenames, and used the `mv` command to rename the files.

```python
#!/usr/bin/env python3
import sys
import subprocess

# Open the file containing the old filenames
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        old_name = line.strip()  # Remove any surrounding whitespace
        new_name = old_name.replace("jane", "jdoe")  # Replace "jane" with "jdoe"
        subprocess.run(["mv", old_name, new_name])  # Rename the file
```

You executed the script using:

```bash
./changeJane.py oldFiles.txt
```

#### Final Output After Renaming
Navigated to the `/data` directory and listed the renamed files:

```
janez_profile_11042019.doc  jdoe_profile_07272018.doc  kwood_profile_04022017.doc  pchow_pic_05162019.jpg
jdoe_contact_07292018.csv   kwood_pic_04032017.jpg     list.txt
```

### Congratulations!
You've successfully renamed files containing `jane` to `jdoe` using both Bash and Python scripting techniques. This lab demonstrated the power of combining both scripting languages to handle file manipulation tasks efficiently.

## Key Takeaways
- **Bash Scripting**: Effective for text processing, file management, and quick operations in the shell.
- **Python Scripting**: Provides flexibility and power for more complex operations and can call system commands through the `subprocess` module.
- **Combining Bash and Python**: Allows for versatile and automated solutions to handle large-scale data processing tasks.

Great job completing this lab and gaining a deeper understanding of Linux commands and scripting techniques!
