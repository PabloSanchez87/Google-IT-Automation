
# Exemplar: Performance Tuning in Python Scripts

## Introduction
In Python scripts, you can improve performance or enable a script to run more quickly on limited or dedicated hardware by choosing suitable programming techniques and utilizing resources like GPUs or CPUs. This document will introduce basic strategies for identifying performance bottlenecks in Python and demonstrate approaches that can speed up Python code significantly.

### Key Topics Covered
1. Basic time command for testing performance.
2. Strategies for improving performance in CPU-bound tasks.
3. Examples of common CPU and memory optimizations.

Let’s start with CPU-bound tasks.

## CPU-bound
The term CPU-bound refers to tasks that are limited by the CPU’s processing power. Many programs in coding can be CPU-bound because they perform intense calculations that require a significant amount of processing time. Python offers several methods to optimize CPU-bound tasks, allowing for smoother, faster execution. This section will introduce you to performance optimization techniques for CPU-bound tasks.

### Profiling
Profiling is essential for identifying parts of the code that consume the most CPU resources. Python’s `cProfile` library can help you locate bottlenecks. Once identified, you can either optimize the code or parallelize the task by distributing the work across multiple cores.

Here’s how you can install `psutil` and check the CPU usage:

```python
import psutil
psutil.cpu_percent()
```

You can specify the interval by passing the following command:

```python
psutil.cpu_percent(interval=3)
```

Import `psutil` in Python and check the clocking CPU usage as well as RAM by running the lines below:

```python
import psutil
psutil.cpu_percent()
```

### Output:
The result will be CPU utilization as a percentage, and can be run within intervals.

```plaintext
20.5  # example output
```

### Basic `time` command
The time command is available in all operating systems and helps you measure the performance of scripts and commands. Running a script or program with `time` will display how long it took to execute.

```bash
time <command>
```

### Common options in `time` command:

| Option | Use                               |
|--------|-----------------------------------|
| -p     | Portable output                   |
| -f     | Adjusts the format for output     |
| -o     | Append the result to a specific file |

Example:
To use the `time` command with `ls` for a basic example:

```bash
time -p ls
```

This command provides a detailed breakdown of execution time.

## Multiprocessing
Another approach is to use multiprocessing, which allows you to divide tasks across different processes, each running on a different CPU core. Python’s `multiprocessing` module helps you implement this.

Here’s an example of using multiprocessing to handle two tasks in parallel:

```python
import multiprocessing

def task():
    print("Executing task")
    
if __name__ == '__main__':
    p = multiprocessing.Process(target=task)
    p.start()
    p.join()
```

This will run two tasks in parallel.

## Conclusion
These examples provide an overview of different methods and processes that Python supports for performance tuning. Choosing the right technique based on the task—such as using `cProfile` for profiling or `psutil` for CPU monitoring—can help you enhance performance. Python’s multiprocessing and parallel processing capabilities are especially useful for CPU-bound tasks, ensuring faster execution and optimized resource utilization.


```python
#!/usr/bin/env python3

from multiprocessing import Pool
import multiprocessing
import subprocess
import os

home_path = os.path.expanduser("~")

src = home_path + "/data/prod/"
dest = home_path + "/data/prod_backup/"

def sync_data():
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    with Pool(multiprocessing.cpu_count()) as pool:
        pool.apply(sync_data)
```	