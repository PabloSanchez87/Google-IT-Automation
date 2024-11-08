
# Exemplar: Debug and solve software problems

## Introduction

In the previous lab, you were a member of your company’s IT department. A colleague that recently left the company wrote a program that’s 90% complete; it’s designed to read some data files with information on employees and then generate a report. It was up to you to finish the code—this includes fixing any errors, bugs, and slowness that might be in the unfinished code.

This exemplar is a walk-through of the previous Qwiklabs activity, including detailed instructions and solutions. You may use this exemplar if you were unable to complete the lab and/or you need extra guidance in completing lab tasks. You may also refer to this exemplar to prepare for the graded quiz in this module.

## Debug issue

You have a `start_date_report.py` Python script with a bunch of functions like `get_start_date()`, `get_same_or_newer()` and others. This script will operate on the data file `employees-with-start-date.csv`, which is generated from a file URL within the script. The script then generates a report of all employees that started on the given start date.

To list files on the home directory, use the following command:

```bash
ls
```

### Output:

```plaintext
start_date_report.py
```

Grant the executable file permission to the `start_date_report.py`:

```bash
sudo chmod +x ./start_date_report.py
```

Now, run the python program `start_date_report.py`:

```bash
./start_date_report.py
```

Enter the values for the year, month, and day respectively as the prompt appears.

### Output:

```plaintext
Getting the first start date to query for.
The date must be greater than Jan 1st, 2018
Enter a value for the year: 2018
Enter a value for the month: 2
Enter a value for the day: 3
Traceback (most recent call last):
  File "./start_date_report.py", line 13, in <module>
    start_date = get_start_date()
  File "./start_date_report.py", line 29, in get_start_date
    year = input("Enter a value for the year: ")
TypeError: 'str' object cannot be interpreted as an integer
```

The program crashes with a **TypeError**. This is because it reads the values entered as prompts as strings. Refer to the function `date.datetime()` within the script. It expects all arguments passed to the `date.datetime()` function to be of integer type, but in our case, the input values are strings.

To resolve this, **EDIT** `start_date_report.py` using the following commands:

```bash
nano ./start_date_report.py
```

Now, search for the `get_start_date()` function and bypass all the string variables that’s taken from user input to the integer class. Here’s how to explicitly cast the data type of these two variables: `year, month, and day` from strings to integers.

Example: `year = int(input("Enter a value for the year: "))`

Simplify, save and re-run the command with month and day as integers.

The `get_start_date()` function should now look like this:

```python
def get_start_date():
    print("Getting the first start date to query for.")
    print("The date must be greater than Jan 1st, 2018")
    year = int(input("Enter a value for the year: "))
    month = int(input("Enter a value for the month [1-12]: "))
    day = int(input("Enter a value for the day [1-31]: "))
    print()
    return datetime.datetime(year, month, day)
```

Save the `start_date_report.py` script file by clicking Ctrl+o, the Enter key, and Ctrl+x.

Run the `start_date_report.py` Python script:

```bash
./start_date_report.py
```

### Output:

```plaintext
Getting the first start date to query for.
The date must be greater than Jan 1st, 2018
Enter a value for the year: 2018
Enter a value for the month: 2
Enter a value for the day: 3
Started on Feb 03, 2018: [‘Debbie Pickett’]
Started on Feb 06, 2018: [‘Thomas Nicholson’]
Started on Feb 09, 2018: [‘David Maxwell’]
Started on Feb 15, 2018: [‘Nina Atkinson’]
```

## Improve performance

Once you debug the issue, the script will start processing the file but it takes a long time to complete. This is because the program goes slowly line by line instead of printing the report quickly. You need to debug why the program is slow and then fix it. In this section, you need to find bottlenecks, improve the code, and make it more efficient.

The problem with the script is that it’s downloading the whole file and then going over it for each date. In the current script it takes almost 2 minutes to complete (1:52 on GCP). An optimized script should generate reports for the same date within a few seconds.

To check the execution time of a script, add a prefix `time` and run the script.

### Example:

```bash
time ./test.py
```

To resolve this issue, open the `start_date_report.py` script using nano editor. Now, modify `get_same_or_newer()` function to preprocess the file, so that the output generated can be used for various dates instead of just one.

Here are a few hints to fix this issue:

1. Download the file only once from the URL.
2. Preprocess it so that the same calculation doesn’t need to be done over and over again. This can be done in two ways. You can choose any one of them:
   - To create a dictionary with the start dates and then use the data in the dictionary instead of the complicated calculation.
   - To sort the list by `start_date` and then go by date.

Choose any one of the above preprocessing options and modify the script accordingly.

Once you’ve completed editing the Python script, save the file by clicking Ctrl+o, the Enter key, and Ctrl+x.

Run the `start_date_report.py` Python script:

```bash
./start_date_report.py
```

### Output:

```plaintext
Getting the first start date to query for.
The date must be greater than Jan 1st, 2018
Enter a value for the year: 2018
Enter a value for the month: 2
Enter a value for the day: 3
Started on Oct 06, 2016: ['Darius Goodwin']
Started on Oct 15, 2016: ['Tara Boyce']
Started on Dec 26, 2016: ['Isley Fuentes']
```

Now, you’ve improved the performance of the script.

## Congratulations!

Congrats! You’ve successfully fixed errors, bugs, and increased the performance of execution. Debugging an issue is a process that requires determination since by fixing a repeatable call will be beneficial as an IT Specialist.
