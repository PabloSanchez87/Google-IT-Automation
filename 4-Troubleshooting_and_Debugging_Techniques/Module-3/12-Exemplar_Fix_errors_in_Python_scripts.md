
# Exemplar: Fix errors in Python scripts

## Introduction

In the previous lab, you were an IT professional who’s in charge of the deployment and maintenance of software in your company’s fleet. A piece of software that’s deployed on all machines in your fleet threw an error on a number of these machines. You hadn’t written the software and didn’t have access to the source code, but you could examine the environment where the software was running and tried to work out what was going on.

This exemplar is a walk-through of how the previous Quicklab activity, including detailed instructions and solutions. You may use this exemplar if you were unable to complete the lab and improve your grade in completing lab tasks. You may also refer to this exemplar to prepare for the graded quiz in this module.

## ModuleNotFoundError

Since you haven’t written the software and don’t have access to the source code, you’ll need to examine the environment where the software is running and try to work out what’s going on. There’s a python script in a folder named `/usr/bin/infrastructure` in `/user/bin` directory that reads data from a CSV file and prints the data to the terminal in a nicely formatted manner. Let’s run this script and see whether it generates any errors.

```bash
cd /
python3 /usr/bin/infrastructure
```

### Output:

```python
import matplotlib
ModuleNotFoundError: No module named ‘matplotlib’
```

The script crashed, displaying a `ModuleNotFoundError`. This error is raised when an `import` statement has trouble importing a specific module. You could also see the module that the `import` statement hasn’t found (i.e., `matplotlib`). We’ll need to install this module before we continue to run the script again.

### Fix:

In order to fix this error, you need to install the `matplotlib` python library using `pip3`:

```bash
pip3 install matplotlib
```

`Matplotlib` is a plotting library for the Python programming language and its numerical mathematics extension `NumPy` (installed upon installing matplotlib). It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits. Even simpler, it’s a visualization library in python for 2D plots of arrays.

## NoFileError

After installing the necessary modules, run the script again.

```bash
python3 /usr/bin/infrastructure
```

### Output:

```bash
Scanning for data.csv...
NoFileError: Could not find data.csv in the working directory
```

This time it returns a `NoFileError` with a message that it could not find `data.csv` file in the working directory. Try debugging this issue.

### Fix:

Let’s navigate to the working directory and see if the `data.csv` file exists.

```bash
cd /
ls
```

### Output:

```bash
data.bak
```

As you can see, the file `data` has the extension `.bak`. As we mentioned earlier, the script `infrastructure` works on CSV files. Inspect the error message, which says that it didn’t find a `data.csv` file. We’ve now found the root cause of the issue. Let’s move forward by renaming the file `data.bak` to `data.csv`.

```bash
mv data.bak data.csv
```

Now, navigate back to the root directory and run the script again.

```bash
cd /
python3 /usr/bin/infrastructure
```

### Output:

```bash
MissingColumnError: Could not find column company in data.csv
```

This now gives a `MissingColumnError`. It says that it couldn’t find a column named `company` within the `data.csv` file.

## MissingColumnError

Let’s check the `data.csv` file for the missing column name.

```bash
cat /data.csv
```

### Output:

```csv
firstname,surname,job title
Oliver,Jefferson,Quan Vel Corporation,IT Resident
Xenos,Snow,Tellus LLC,CTO
Emerson,Delgado,Sagittis Ltd,CFO
Dustin,Daughtery,Pharetra Corp.,IT Resident
```

So, the column name is actually missing. Let’s add the column name and run the script again.

Grant the permissions to the `data.csv` file.

```bash
sudo chmod 777 /data.csv
```

Open `data.csv` file using nano editor.

```bash
nano /data.csv
```

Add the missing column name and save the file by clicking `Ctrl+o`, followed by `Enter key` and `Ctrl+x`.

Now, run the script again:

```bash
python3 /usr/bin/infrastructure
```

### Output:

```bash
student@Linux-Instances:~$ python3 /usr/bin/infrastructure
student@Linux-Instances:~$
```

This time you fixed all the errors!

## Congratulations!

Congrats! You’ve correctly understood the error messages and fixed them by tracking down the root cause. This will help you as an IT professional who’s in charge of the deployment and maintenance of software in your company’s fleet.
