
# Review: Advanced Command Interaction

### Viewing the Last Lines of a Log File
```bash
tail /var/log/syslog  # Display the last 10 lines of the "syslog" file located in /var/log directory
```

#### Code Output:
```
May 24 10:17:01 ubuntu.local CRON[257236]: (root) CMD ( cd / && run-parts --report /etc/cron.hourly)
May 24 10:18:41 ubuntu.local rsyslogd: -- MARK --
May 24 10:25:19 ubuntu.local systemd[1]: Reloading.
```

### Using `cut` to Extract Specific Columns
```bash
tail /var/log/syslog | cut -d' ' -f5-  # Display the last 10 lines and extract columns starting from the 5th field
```

#### Code Output:
```
CRON[257236]: (root) CMD ( cd / && run-parts --report /etc/cron.hourly)
rsyslogd: -- MARK --
systemd[1]: Reloading.
```

### Explanation
The `cut` command uses the `-d` flag to specify a delimiter (space `' '`) and the `-f` flag to select fields starting from the fifth one. This removes the timestamp and hostname from the logs.

---

### Combining Commands to Analyze Logs
```bash
cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head  # Extract columns, sort, count unique entries, sort again, and display top 10
```

#### Code Output:
```
41 systemd[1]: Starting Network Manager Script Dispatcher Service...
41 systemd[1]: Started Network Manager Script Dispatcher Service.
41 systemd[1]: NetworkManager-dispatcher.service: Succeeded.
41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: start running ordered scripts...
41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: new request (1 scripts)
41 dhclient[757]: DHCPREQUEST for 192.168.122.103 on ens3 to 192.168.122.1 port 67 (xid=0x3a5ff7ed)
41 dhclient[757]: DHCPOFFER of 192.168.122.103 from 192.168.122.1 (xid=0x3a5ff7ed)
41 dbus-daemon[592]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
41 dbus-daemon[592]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='/dbus-org.freedesktop.nm-dispatcher.service'
9 systemd[1]: Started Run anacron jobs.
```

### Explanation
The command extracts specific fields from the syslog, sorts the lines, counts the number of unique entries, and displays the most frequent log messages. This helps identify common events in the log file.

---

### Analyzing Multiple Log Files Using a Script
```bash
#!/bin/bash  # Specify the script should run using the Bash shell

for logfile in /var/log/*log; do  # Loop through each log file in the /var/log directory
    echo "Processing: $logfile"  # Print the name of the current log file
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5  # Extract fields, count unique messages, and display top 5 messages
done
```

#### Command to run the script
```bash
./toploglines.sh  # Execute the script named "toploglines.sh"
```

#### Code Output:
```
Processing: /var/log/user.log
  23 system-updater[199481]: DEBUG Command exited with status 0
  19 system-updater[46682]: DEBUG Command exited with status 0
  16 system-updater[175060]: DEBUG Command exited with status 0
  11 /usr/bin/lock: called by /bin/bash for . uid 0, euid 0.
  11 network-manager-dhclient-hooks: Dispatching run of '/etc/dhcp/dhclient-exit-hooks.d/hostname' ...

Processing: /var/log/Xorg.0.log
  87 Printing DDC gathered Modelines:
  87 Modeline "1920x1080"x0.0  141.00  1920 1936 1952 2104  1080 1083 1097 1116 -hsync +vsync (67.0 kHz eP)
  87 EDID vendor "AUO", prod id 5949
  78 vendor "AUO", prod id 5949
  78 DDC gathered Modelines:
```

### Explanation
This script processes each log file in the `/var/log` directory and displays the top 5 most frequently occurring messages along with their counts. It’s useful for analyzing large numbers of log files and identifying patterns.

---

### Conclusion
These examples show how to extract, analyze, and manipulate log files using commands like `cut`, `sort`, and `uniq`. The final script combines these commands to automate log file analysis across multiple files, making it a powerful tool for system administrators.

---

**Note**: Make sure your script is executable before running it:
```bash
chmod +x toploglines.sh
```
