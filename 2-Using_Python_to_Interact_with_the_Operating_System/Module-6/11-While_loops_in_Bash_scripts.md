
# Review: While Loops in Bash Scripts

### Basic `while` Loop Example
```bash
#!/bin/bash  # Specifies the script to use the Bash shell
n=1  # Initialize a counter variable with value 1
while [ $n -le 5 ]; do  # Loop as long as `n` is less than or equal to 5
    echo "Iteration number $n"  # Print the current iteration number
    ((n+=1))  # Increment the counter `n` by 1
done
```

#### Command to run the script
```bash
./while.sh  # Executes the script named "while.sh"
```

#### Code Output:
```
Iteration number 1
Iteration number 2
Iteration number 3
Iteration number 4
Iteration number 5
```

### Explanation
In this example, the script initializes a variable `n` with a value of 1 and increments it in each iteration until it reaches 5. The loop terminates once `n` exceeds 5.

---

### Python Script for Random Exits
```python
#!/usr/bin/env python  # Specifies the script to use the system's Python interpreter
import random  # Import the random module for generating random numbers

value = random.randint(0, 3)  # Generate a random integer between 0 and 3
print("Returning: " + str(value))  # Print the value to show what is being returned

sys.exit(value)  # Exit the script with the generated value as the exit status
```

#### Command to run the script multiple times
```bash
./random-exit.py
./random-exit.py
./random-exit.py
```

#### Code Output:
```
Returning: 3
Returning: 2
Returning: 0
```

### Explanation
This script generates a random integer each time it runs and exits with that value as its status. This is useful to simulate different exit statuses for testing purposes.

---

### `while` Loop with Command Retry Logic
```bash
#!/bin/bash  # Use the Bash shell
n=0  # Initialize a counter variable `n`
command=$1  # Assign the first command-line argument to the variable `command`
while ! $command && [ $n -le 5 ]; do  # While the command fails and `n` is less than or equal to 5
    sleep $n  # Wait for `n` seconds before retrying
    ((n+=1))  # Increment the counter `n` by 1
    echo "Retry #$n"  # Print the retry attempt number
done
```

#### Command to run the script
```bash
./retry.sh ./random  # Run the script "retry.sh" with the "random" script as its command
```

#### Code Output:
```
Returning: 3
Retry #1
Returning: 3
Retry #2
Returning: 1
Retry #3
Returning: 3
Retry #4
Returning: 0
```

### Explanation
This script attempts to execute a command up to 5 times if it fails. It waits for an increasing number of seconds between retries. If the command succeeds (exit status 0), the loop stops.

---

### Conclusion
These examples demonstrate different use cases for `while` loops in Bash scripting, including basic iteration, retry logic, and integration with external commands. Understanding `while` loops is essential for controlling script flow in repetitive tasks.

---

**Note**: Make sure your script is executable before running it:
```bash
chmod +x script_name.sh
```
