# Basic Linux Commands example

```bash
# 1. Create a New Directory
mkdir mynewdir

# 2. Change Directory
cd mynewdir/

# 3. Display the Current Working Directory
/mynewdir$ pwd

# 4. Copy a File to the Current Directory
/mynewdir$ cp ../spider.txt .

# 5. Create an Empty File
/mynewdir$ touch myfile.txt

# 6. List Files with Long Format
/mynewdir$ ls -l 

#Output:
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 myfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt

#7. List All Files Including Hidden Files
/mynewdir$ ls -la

#Output:
#total 12
#drwxr-xr-x  2 user user  4096 Mai 22 14:17 .
#drwxr-xr-x 56 user user 12288 Mai 22 14:17 ..
#-rw-rw-r--  1 user user     0 Mai 22 14:22 myfile.txt
#-rw-rw-r--  1 user user   192 Mai 22 14:18 spider.txt

# 8. Rename or Move a File
/mynewdir$ mv myfile.txt emptyfile.txt

# 9. Copy a File to Another File
/mynewdir$ cp spider.txt yetanotherfile.txt

# 10. List Files Again
/mynewdir$ ls -l

#Output:
#total 8
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 emptyfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:23 yetanotherfile.txt

# 11. Remove All Files
/mynewdir$ rm *

# 12. List Files After Removal
/mynewdir$ ls -l

#total 0

# 13. Go Back to the Parent Directory
/mynewdir$ cd ..

# 14. Remove the Directory
rmdir mynewdir/

# 15. Verify Directory Removal
ls mynewdir

#ls: cannot access 'mynewdir': No such file or directory
```	