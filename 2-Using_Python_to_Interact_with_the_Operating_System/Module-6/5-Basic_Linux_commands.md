
# Basic Linux Commands

Basic Linux commands are beneficial for developers when interacting with a Linux operating system through the command-line interface. They are commonly used to work with files and directories, making it easier to manage the system's structure. Typically, these commands are straightforward, easy to learn, and provide extended functionalities for more advanced operations. Developers can quickly look up the syntax for any of these commands if needed.

In this guide, you will review basic Linux commands with examples provided along the way.

## Managing Files and Directories
Many applications configure themselves by reading files. They are designed to read and write files in specific directories. Because of this, developers need to understand how to move and rename files, change their permissions, and do simple operations on their contents. Here are some common commands:

### `mv` Command
The `mv` command is used to move one or more files to a different directory, rename a file, or both at the same time.

- **Note**: Linux is case-sensitive, so `mv` can also be used to change the case of a filename.

Examples:
- `mv myfile.txt dir1/` - Moves a file to the specified directory.
- `mv file1.txt file2.txt file3.txt dir1/` - Moves multiple files to the directory `dir1/`.

### `cp` Command
The `cp` command is used to copy one or more files.

Examples:
- `cp file1.txt file2.txt` - Copies `file1.txt` to `file2.txt`.
- `cp file1.txt file2.txt file3.txt dir1/` - Copies multiple files to the directory `dir1/`.

### `chmod`, `chown`, and `chgrp` Commands
These commands are used to change file permissions and ownership. For example, `chmod` can make a file readable by everyone on the system before moving it to a public directory.

Example:
- `chmod +r file.html && mv file.html /var/www/html/index.html` - Grants read permissions and moves the file to a public directory.

## Operating with the Content of Files
Every programmer will use files for something. Whether it’s for configuration, data, or input and output, programmers work with files and need to know how to operate with their contents.

### `cut` Command
The `cut` command extracts specific fields from a data file.

Examples:
- `cut -f1 -d"," addressbook.csv` - Extracts the first field from a CSV file.
- `cut -c1-3,5-7,9-12 phones.txt` - Extracts specific columns (1-3, 5-7, 9-12) from a text file.

### `sort` Command
The `sort` command sorts the contents of a file.

Examples:
- `sort names.txt` - Sorts the input alphabetically.
- `sort -r names.txt` - Sorts inputs in reverse alphabetical order.
- `sort -n numbers.txt` - Sorts numbers in ascending order.

## Combining Multiple Commands
Linux commands can be combined using pipes (`|`) for more powerful operations.

Examples:
- `ls -l | cut -w -f5,9 | sort -rn | head -10` - Displays the 10 largest files in the current directory.
- `cut -f1-2 -d"," addressbook.csv | sort` - Extracts the first and last names from a CSV file and sorts them.

## Additional Commands

### `id` Command
The `id` command prints information about the current user. This command is useful when dealing with permission errors.

Example:
- `id`
  ```
  uid=3000(tradel) gid=3000(tradel) groups=3000(tradel),0(root),100(users),545(builtin_users),999(docker)
  ```

### `free` Command
The `free` command displays information about the system's memory.

Example:
- `free -h` - Prints memory usage in a human-readable format.

## Key Takeaways
Basic Linux commands assist developers in different types of tasks related to managing files and directories and working with the content of each file. These commands allow developers to work more efficiently and effectively.
