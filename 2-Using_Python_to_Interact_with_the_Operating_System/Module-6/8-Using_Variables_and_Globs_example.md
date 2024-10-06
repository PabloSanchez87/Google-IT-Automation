
# Using Variables and Globs

This document covers the use of variables and glob patterns in Bash scripting as demonstrated in the instructional video. The following examples and outputs will help clarify how to use variables and wildcard patterns effectively in Bash.


### Using Variables in Bash
```bash
example=hello  # Assigns the string "hello" to the variable named "example"
echo $example  # Prints the value of the variable "example"
```

#### Code Output:
```
hello
```

### Common Mistake with Variables
```bash
example = hello  # This line contains spaces around the equal sign, which is incorrect in Bash variable assignment.
```

#### Code Output:
```
Command 'example' not found, did you mean:
  command 'example1' from deb pvm-examples (3.4.6-2build1)
```

This error occurs because spaces around the equal sign are not allowed when assigning variables in Bash.

---

### Script Using Variables and Patterns
```bash
#!/bin/bash  # Specifies the script to use the Bash shell
line="------------------------------------------------"  # Defines a variable called "line" to store the dashed line
echo "Starting at: $(date)"; echo $line  # Prints start time and the value of the variable "line"

echo "UPTIME"; uptime; echo $line  # Displays the label "UPTIME", runs the uptime command, and prints the line
echo "FREE"; free; echo $line  # Displays "FREE", runs the free command, and prints the line
echo "WHO"; who; echo $line  # Displays "WHO", runs the who command, and prints the line

echo "Finishing at: $(date)"  # Displays the finishing time
```

#### Command to run the script
```bash
./gather-information.sh  # Runs the script named "gather-information.sh"
```

#### Code Output:
```
Starting at: Mi 22. Mai 17:30:30 CEST 2019
------------------------------------------------

UPTIME
  17:30:30 up 8 days,  1:51,  2 users,  load average: 0.00, 0.00, 0.00
------------------------------------------------

FREE
               total        used        free      shared  buff/cache   available
Mem:         4037132      862132      444720      10032     2730280     2875336
Swap:        2097148      6156     2090992

------------------------------------------------

WHO
user    :0           2019-05-14 15:39 (:0)
user    pts/1        2019-05-14 15:40 (192.168.122.1)

------------------------------------------------
Finishing at: Mi 22. Mai 17:30:30 CEST 2019
```

### Using Globs in Bash
```bash
echo *.py  # Matches and lists all filenames that end with ".py" in the current directory
```

#### Code Output:
```
action_deprecation.py areas.py capitalize.py charfreq.py check_deprecation.py check_localhost.sh
```

**Explanation**: The `*.py` pattern tells the shell to list all files with a `.py` extension in the current directory.

---

### Matching Files that Start with "c"
```bash
echo c*  # Matches all files in the current directory that start with "c"
```

#### Code Output:
```
capitalize.py charfreq.py check_localhost.sh
```

**Explanation**: The `c*` pattern lists all files whose names start with "c" in the current directory.

---

### Matching All Files
```bash
echo *  # Lists all files and directories in the current directory
```

#### Code Output:
```
(... all the files in the directory ...)
```

**Explanation**: The `*` pattern matches any filename or directory name in the current directory.

---

### Using Question Marks to Match Patterns
```bash
echo ?????.py  # Matches all files with exactly five characters followed by ".py"
```

#### Code Output:
```
areas.py hello.py
```

**Explanation**: Each question mark `?` matches exactly one character. So, `?????.py` matches files that have five letters followed by the `.py` extension.

---

### Conclusion
These examples show how variables and glob patterns are used to manipulate and filter file names in a directory using Bash. Proper understanding of these patterns can simplify file management and script automation.

---

**Note**: Remember to run `chmod +x script.sh` to make your script executable before running it.
