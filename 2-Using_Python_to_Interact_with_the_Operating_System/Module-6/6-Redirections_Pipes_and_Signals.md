
# Redirections, Pipes, and Signals

In Linux, understanding how to manage input and output streams, and how to control processes, is essential for developers. This guide covers basic concepts such as redirections, pipes, and signals to control process execution.

## Managing Streams
The following redirectors are used to control the input and output streams of your programs:

- **`command > file`**: Redirects standard output to a file, overwriting the file if it exists.
  
- **`command >> file`**: Redirects standard output to a file, appending to the file if it exists.

- **`command < file`**: Redirects standard input from a file.

- **`command 2> file`**: Redirects standard error to a file.

- **`command1 | command2`**: Connects the output of `command1` to the input of `command2`, creating a pipeline between the two commands.

## Operating with Processes
When interacting with processes in a Linux environment, the following commands are useful to know:

### `ps` Command
- `ps`: Lists the processes executing in the current terminal for the current user.
- `ps ax`: Lists all processes currently executing for all users.
- `ps e`: Shows the environment variables for the processes listed.

### `kill` Command
- `kill PID`: Sends the `SIGTERM` signal to the process identified by `PID` (Process ID). This command is used to terminate a running process gracefully.

### Foreground and Background Process Control
- `fg`: Brings a stopped or background job to the foreground, allowing it to resume normal operation.
- `bg`: Moves a stopped job to the background, allowing other commands to be run in the foreground.

### Job Management
- `jobs`: Lists the jobs currently running or stopped in the background. Useful for managing and identifying processes.

### Monitoring System Processes
- `top`: Displays a live, real-time view of system processes using the most CPU time. Press `q` to quit the command.

## Key Takeaways
- **Redirections**: Control where the output and input streams of commands go.
- **Pipes**: Connect the output of one command to the input of another.
- **Process Control**: Use commands like `ps`, `kill`, and `jobs` to manage and control processes running on the system.
- **Monitoring**: Use `top` to get real-time information on process usage.

Understanding these commands and concepts is fundamental for efficient system management and troubleshooting in Linux.
