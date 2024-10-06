
# Creating Bash Scripts

### Bash Script Code Example 1
```bash
#!/bin/bash  # This line specifies that the script should be executed using the Bash shell
echo "Starting at: $(date)"  # Displays the start date and time
echo  # Prints an empty line for readability

echo "UPTIME"  # Display the label "UPTIME"
uptime  # Shows how long the system has been running, users connected, and system load
echo  # Prints an empty line

echo "FREE"  # Display the label "FREE" for memory usage
free  # Shows the system's memory usage
echo  # Prints an empty line

echo "WHO"  # Display the label "WHO" for logged-in users
who  # Shows the list of users currently logged in
echo  # Prints an empty line

echo "Finishing at: $(date)"  # Displays the end date and time
```

#### Command to run the script
```bash
./gather-information.sh  # Executes the bash script named "gather-information.sh"
```

### Output Example 1:
```
Starting at: Mi 22. Mai 17:13:06 CEST 2019

UPTIME
  17:13:06 up 8 days,  1:34,  2 users,  load average: 0.00, 0.00, 0.00

FREE
               total        used        free      shared  buff/cache   available
Mem:         4037132      871336      253040      10032     2911856     2865984
Swap:        2097148       4364     2092784

WHO
user    :0           2019-05-14 15:39 (:0)
user    pts/1        2019-05-14 15:40 (192.168.122.1)

Finishing at: Mi 22. Mai 17:13:06 CEST 2019
```

### Bash Script Code Example 2
```bash
#!/bin/bash  # Specify that this is a Bash script
echo "Starting at: $(date)"; echo  # Display start time and add a line break

echo "UPTIME"; uptime; echo  # Print UPTIME label, run uptime command, and add a line break
echo "FREE"; free; echo  # Print FREE label, run free command, and add a line break
echo "WHO"; who; echo  # Print WHO label, run who command, and add a line break

echo "Finishing at: $(date)"  # Print the finish time
```

#### Command to run the script
```bash
./gather-information.sh  # Run the bash script named "gather-information.sh"
```

### Output Example 2:
```
Starting at: Mon 13 May 2019 02:52:11 PM CEST

UPTIME
  14:52:11 up 17 days,  2:35,  1 user,  load average: 0.70, 1.01, 1.16

FREE
               total        used        free      shared  buff/cache   available
Mem:        32912600    19966400     1003304     321672    11942896    12281516
Swap:       20250620     612352    19638268

WHO
user    tty7         2019-04-29 12:19 (:0)

Finishing at: Mon 13 May 2019 02:52:11 PM CEST
```

### Conclusion
The examples show two variations of a basic Bash script that outputs system information such as uptime, memory usage, and users currently logged in. Both scripts function as expected, producing similar results with different formatting.

---

**Note**: Ensure that the script has executable permissions before running it:
```bash
chmod +x gather-information.sh
```
