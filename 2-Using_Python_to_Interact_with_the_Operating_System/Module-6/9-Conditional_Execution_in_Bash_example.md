
# Conditional Execution in Bash

### Basic Conditional Example
```bash
if grep "127\.0\.0\.1" /etc/hosts; then  # Check if the string "127.0.0.1" exists in the /etc/hosts file
    echo "Everything ok"  # If the pattern is found, print this message
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"  # If the pattern is not found, print an error message
fi
```

#### Command to run the script
```bash
./check_localhost.sh  # Execute the script named "check_localhost.sh"
```

#### Code Output:
```
127.0.0.1    localhost
Everything ok
```

### Explanation
In this example, we use the `if` keyword along with the `grep` command to search for a pattern. If the pattern is found, the command returns success (exit code 0), and the `then` block is executed. If not, the `else` block runs.

---

### Using `test` Command for Conditionals
```bash
if test -n "$PATH"; then echo "Your path is not empty"; fi  # Check if the PATH variable is not empty
```

#### Code Output:
```
Your path is not empty
```

### Explanation
The `-n` option checks if a string is non-empty. In this case, it checks if the `$PATH` variable contains any value.

---

### Alternative Syntax for Conditionals
```bash
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi  # Alternative syntax using square brackets
```

#### Code Output:
```
Your path is not empty
```

### Explanation
Square brackets `[` and `]` are another way to write conditionals in Bash. They work similarly to the `test` command, providing a more readable way to structure conditional statements.

---

### Conclusion
These examples demonstrate basic conditional execution in Bash. Using `if`, `test`, and various syntaxes, you can control script behavior based on the results of commands or variable values. Understanding these concepts is crucial for writing more complex scripts.

---

**Note**: Remember to make your script executable before running it using:
```bash
chmod +x script_name.sh
```
