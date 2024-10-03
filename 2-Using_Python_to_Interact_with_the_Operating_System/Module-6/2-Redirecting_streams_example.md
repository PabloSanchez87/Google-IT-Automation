# Redirecting Streams example

```bash	

# 1. View the Contents of a Python Script
cat stdout_example.py 
# File Contents:
#!/usr/bin/env python3
print("Don't mind me, just a bit of text here...")

# 2. Execute the Script
./stdout_example.py 
#Output: Don't mind me, just a bit of text here...

#3. Redirect STDOUT to a File
./stdout_example.py > new_file.txt

# 4. View the Contents of the File
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...

# 5. Append Output to the File
./stdout_example.py >> new_file.txt

# 6. View the Contents Again
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
 #Don't mind me, just a bit of text here...

# 7. View the Contents of Another Script
cat streams_err.py 

#File Contents:
#!/usr/bin/env python3
data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

# 8. Execute the Script with STDIN Redirection
./streams_err.py < new_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR

# 9. Redirect STDERR to a Separate File
./streams_err.py < new_file.txt 2> error_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...

# 10. View the Error Messages in the File
cat error_file.txt 
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR

# 11. Create a New File with echo
echo "These are the contents of the file" > myamazingfile.txt

# 12. View the New File
cat myamazingfile.txt 
#These are the contents of the file
```
