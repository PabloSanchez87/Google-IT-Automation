
# For Loops in Bash Scripts


### Basic `for` Loop Example
```bash
#!/bin/bash  # Specifies the script to use the Bash shell

for fruit in peach orange pear; do  # Iterate over a list of three elements: peach, orange, and pear
    echo "I like $fruit"  # Print a message for each fruit
done
```

#### Command to run the script
```bash
./fruits.sh  # Executes the script named "fruits.sh"
```

#### Code Output:
```
I like peach!
I like orange!
I like pear!
```

### Explanation
This script iterates over three different elements (`peach`, `orange`, and `pear`) and prints a message for each one using the `for` loop.

---

### Using `basename` to Rename Files
```bash
cd old_website/  # Navigate to the directory "old_website"
ls -l  # List all files in the directory in long format
```

#### Code Output:
```
total 0
-rw-r--r-- 1 user user 0 May 24 10:19 about.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 contact.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 footer.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 header.HTM
-rw-r--r-- 1 user user 0 May 24 10:19 index.HTM
```

### Extracting File Names Without Extension
```bash
for file in *.HTM; do  # Loop through each file with the ".HTM" extension in the directory
    name=$(basename "$file" .HTM)  # Use `basename` to remove the ".HTM" extension
    mv "$file" "$name.html"  # Rename each file to have a ".html" extension instead
done
```

#### Command to run the script
```bash
./rename.sh  # Run the script named "rename.sh"
```

#### Code Output:
```
mv about.HTM about.html
mv contact.HTM contact.html
mv footer.HTM footer.html
mv header.HTM header.html
mv index.HTM index.html
```

### Explanation
The `for` loop iterates through all files with the `.HTM` extension in the current directory. For each file, it removes the `.HTM` extension using `basename` and renames it with a `.html` extension. Finally, the `mv` command changes the filename to the new name.

---

### Final Output After Renaming
```bash
ls -l  # List all files in the directory to see the changes
```

#### Code Output:
```
total 4
-rw-r--r-- 1 user user 0 May 24 10:19 about.html
-rw-r--r-- 1 user user 0 May 24 10:20 contact.html
-rw-r--r-- 1 user user 0 May 24 10:20 footer.html
-rw-r--r-- 1 user user 0 May 24 10:20 header.html
-rwxr-xr-x 1 user user 90 May 24 10:19 index.html
```

### Explanation
The `ls -l` command lists all the files in the directory after renaming, showing that each `.HTM` file has been successfully converted to `.html`.

---

### Conclusion
These examples demonstrate basic use cases of the `for` loop in Bash, such as iterating through a list of values and processing files in a directory. Using `for` loops with commands like `basename` can simplify complex file manipulations in scripts.

---

**Note**: Make sure to make your script executable before running it using:
```bash
chmod +x script_name.sh
```
