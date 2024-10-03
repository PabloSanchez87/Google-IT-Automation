# Signaling Processes example

```bash	
ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
```
- Press Control C

- Description: Initiates a ping command to www.example.com, sending ICMP packets to check connectivity and measure round-trip time. The command runs continuously until interrupted.


    ```bash
    --- www.example.com ping statistics ---

    9 packets transmitted, 9 received, 0% packet loss, time 8013ms

    rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms
    ```
    - Sends the SIGINT signal to the ping process, which interrupts the command and terminates it gracefully. This is useful to stop the command when it is no longer needed.
    - This summary shows the number of packets transmitted, received, and the round-trip time (RTT) statistics.

```bash		
ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
```
- Press Control Z: the program stops. 

    - Sends the `SIGTSTP` signal to suspend the `ping` process. The command stops running, but the process is not terminated—it’s moved to the background in a suspended state.

    - Note: At this point, the process is paused and you can check its status with the jobs command.

```bash	
fg
#ping www.example.com
#64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=5 ttl=51 time=93.6 ms
```
- Brings the most recently suspended process back to the foreground, allowing it to continue executing as before. The ping command resumes and displays packet data again.


- Press Control C:
    ```bash
    --- www.example.com ping statistics ---

    9 packets transmitted, 9 received, 0% packet loss, time 8013ms

    rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms
    ```

    - Sends the `SIGINT` signal again to terminate the `ping` command gracefully, showing a summary of the statistics.

    - This final output confirms that the ping command was interrupted and terminated, showing packet statistics.