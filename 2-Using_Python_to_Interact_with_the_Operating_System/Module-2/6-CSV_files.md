# .csv files
The most common format for importing and exporting data for spreadsheets is a `.csv` format. A Comma Separated Values (`.csv`) file is a plain text file that uses—you guessed it—commas to separate each piece of data. You may already be familiar with `.csv` files if you have saved a spreadsheet in the `.csv` format. Here is a simple example of a `.csv` file displaying employee information:

```python
Name, Department, Salary

Aisha Khan, Engineering, 80000

Jules Lee, Marketing, 67000

Queenie Corbit, Human Resources, 90000
```

Notice that each row represents an employee’s information, and the values are separated by commas. 

In this reading, you will examine different commands to use when working with .csv files in Python and be provided with additional links for more information.

## Module contents
The `.csv` module is a built-in Python functionality used to read and work with `.csv` files. Let’s look at how the `.csv` module defines some of these functions:

- `csv.reader` This function returns a reader object that iterates over lines in the .csv file.

- `csv.writer` This function returns a writer object that’s responsible for converting the user’s data into delimited strings on the given file-like object.

- `class csv.DictReader` This function creates an object that functions as a regular reader but maps the information in each row to a dictionary whose keys are given by the optional `fieldname` parameters.

## Dialects and formatting parameters

Dialects are rules that define how a `.csv` file is structured, and parameters are formed to control the behavior of the `.csv` reader and writer and live within dialects. The following  features are supported by dialects:

- `Dialect.delimiter` This attribute is a one-character string used to separate fields and defaults to a comma.

- `Dialect.quotechar`  This attribute is a one-character string used to quote fields containing special characters and defaults to ‘ ‘’ ‘.

- `Dialect.strict`  This attribute’s default is False, but when `True`, `exception` `csv.Error` will be raised if an error is detected.

## Reader objects
A reader object contains the following public methods and attributes:

- `csvreader._next_()` This method returns the next row of the reader’s iterable object as a list or a dictionary, parsed properly to the current dialect. Typically, you would call this next(reader).

- `csvreader.dialect` This attribute is a read-only description of the dialect in use by the parser.

## Writer objects
Writer objects provide you the capability to write data to a `.csv` file. Let’s look at a couple of public methods and attributes for writer objects:

- `csvwriter.writerows(rows)` This method writes all elements in rows to the writer’s file object and formats following the current dialect.

- `csvwriter.dialect` This attribute is a read-only description of the dialect being used by the writer.

## Key takeaways

If you haven’t worked with `.csv` files yet, it’s only a matter of time. Become familiar with the `.csv` module’s reader and writer objects to work more efficiently with `.csv` files. The modules, features, and attributes in this reading are only some of the commands that can be used while working with `.csv` files. 

## Resources for more information
- This [document](https://docs.python.org/3/library/csv.html) provides additional information on how to read and write functions using .csv files.

- This [document](https://realpython.com/python-csv/) provides additional information on what a .csv file is, how to parse .csv files with Python’s built-in .csv library, and how to parse .csv files with the pandas library.