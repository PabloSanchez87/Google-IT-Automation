#!/usr/bin/env python3
import sys
import re
import operator
import csv

# Dictionary to count the number of log entries for each user
per_user = {}  # Split between INFO and ERROR
# Dictionary to count the number of different error messages
errors = {}

# * Read the log file and populate the dictionaries
with open('syslog.log') as file:
    # Read each line in the log file
    for line in file.readlines():
        # Use regex to extract relevant information from each line
        # * Example log file line:
        # "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)

        # Extract elements from the regex match: log type, error message, and username
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        # * Populate the 'errors' dictionary with the error message counts
        # If the error message is not in the dictionary, initialize it with 1
        if error_msg not in errors.keys():
            errors[error_msg] = 1
        else:
            # If the error message already exists, increment its count
            errors[error_msg] += 1

        # * Populate the 'per_user' dictionary with user log entries
        # If the user is not in the 'per_user' dictionary, initialize it with default values
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0

        # If the log entry is of type 'INFO', increment the user's 'INFO' count
        if code == 'INFO':
            per_user[user]["INFO"] += 1
        # If the log entry is of type 'ERROR', increment the user's 'ERROR' count
        elif code == 'ERROR':
            per_user[user]['ERROR'] += 1

# * Sort the 'errors' dictionary by the count of occurrences, from highest to lowest
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

# * Sort the 'per_user' dictionary by username (alphabetically)
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

# * Close the log file after processing (good practice)
file.close()

# * Insert header ('Error', 'Count') at the beginning of the error list
errors_list.insert(0, ('Error', 'Count'))

# * Create CSV file 'user_statistics.csv' to store the per-user statistics
with open('user_statistics.csv', 'w', newline='') as user_csv:
    # Write each user and their counts of INFO and ERROR messages in the CSV file
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' +
                       str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

# * Create CSV file 'error_message.csv' to store the error message statistics
with open('error_message.csv', 'w', newline='') as error_csv:
    # Write each error message and its count in the CSV file
    for key, value in errors_list:
        error_csv.write(str(key) + ',' + str(value) + '\n')

