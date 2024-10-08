
# Log Analysis with Regular Expressions - Updated Practice Guide

## Introduction
In this practice, the main objective was to automate the analysis of a log file (`syslog.log`) to extract meaningful information and generate two separate reports based on user activities and errors encountered in the system. This process involved using regular expressions, dictionary operations, and file handling techniques to parse the log file and create reports in CSV format.

The entire workflow was broken down into several key steps, which are documented below:

## Step 1: Initial Log Analysis
The first task was to explore the contents of the `syslog.log` file. Using commands like `cat` and `grep`, we were able to filter the logs to show messages of interest, such as `INFO` and `ERROR` logs related to the `ticky` service.

```bash
cat syslog.log
grep "ERROR" syslog.log
grep "INFO" syslog.log
```

From this analysis, we observed two main patterns:
- `INFO` logs indicating successful operations with the format:  
  `Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)`
  
- `ERROR` logs highlighting issues encountered, such as permission errors or failed connections:  
  `Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)`

## Step 2: Creating the `ticky_check.py` Script
The main script, `ticky_check.py`, was designed to read the `syslog.log` file, extract relevant information using regular expressions, and generate two different reports:
1. **`error_message.csv`**: A report summarizing all the unique error messages and their frequency.
2. **`user_statistics.csv`**: A report showing the number of `INFO` and `ERROR` messages generated by each user.

The structure of the script was as follows:

```python
#!/usr/bin/env python3

import re
import csv
from collections import defaultdict

# Initialize dictionaries for storing error counts and user statistics
error_counts = defaultdict(int)
user_statistics = defaultdict(lambda: {"INFO": 0, "ERROR": 0})

# Open and read the syslog.log file
with open("syslog.log", "r") as file:
    for line in file:
        # Match and extract INFO messages
        info_match = re.search(r"ticky: INFO .* \((\w+)\)$", line)
        if info_match:
            user = info_match.group(1)
            user_statistics[user]["INFO"] += 1

        # Match and extract ERROR messages
        error_match = re.search(r"ticky: ERROR ([\w ]+) \((\w+)\)$", line)
        if error_match:
            error_message, user = error_match.groups()
            error_counts[error_message] += 1
            user_statistics[user]["ERROR"] += 1

# Sort the errors by frequency
sorted_errors = sorted(error_counts.items(), key=lambda item: item[1], reverse=True)

# Sort the users alphabetically
sorted_users = sorted(user_statistics.items())

# Write the error report to error_message.csv
with open("error_message.csv", "w") as error_file:
    writer = csv.writer(error_file)
    writer.writerow(["Error", "Count"])
    writer.writerows(sorted_errors)

# Write the user statistics report to user_statistics.csv
with open("user_statistics.csv", "w") as user_file:
    writer = csv.writer(user_file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for user, stats in sorted_users:
        writer.writerow([user, stats["INFO"], stats["ERROR"]])
```

## Step 3: Correcting Errors and Adjustments
During the initial runs of the script, some errors were encountered. The script was generating more users than expected due to including users without `INFO` or `ERROR` activity. After reviewing the outputs and comparing them against the expected results, the script was refined to include only relevant users and correctly format the CSV files.

## Step 4: Generating and Visualizing HTML Reports
Once the CSV files (`error_message.csv` and `user_statistics.csv`) were correctly generated, the next step was to convert them into HTML reports using a secondary script, `csv_to_html.py`. This script transformed the CSV data into HTML tables for easy visualization.

```bash
./csv_to_html.py error_message.csv /var/www/html/error_message.html
./csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html
```

After running these commands, the HTML files could be viewed in a browser using the following URLs:

```
[External_IP_Address]/error_message.html
[External_IP_Address]/user_statistics.html
```

## Final Report Results
After adjustments and validations, the final reports were consistent with the expected outputs:

- **`error_message.html`**: Displayed the error types and their respective counts.
- **`user_statistics.html`**: Showed the count of `INFO` and `ERROR` messages generated by each user.

## Lessons Learned
This project reinforced the following concepts:
1. **Regular Expression Proficiency**: Using `re.search` and capture groups to extract specific log details.
2. **File Handling**: Reading and writing CSV files using Python's `csv` module.
3. **Data Structuring**: Organizing data with dictionaries to build structured outputs.
4. **Bash & Python Integration**: Combining shell scripting with Python to automate tasks effectively.

## Conclusion
The `ticky_check.py` script successfully generated the required reports, and by following structured debugging and iterative improvements, we were able to match the expected outputs. This practice emphasized the importance of accuracy in log parsing and the value of visualizing results for system monitoring.

This `.md` file serves as a comprehensive guide for replicating the lab and troubleshooting common issues encountered during the implementation.
