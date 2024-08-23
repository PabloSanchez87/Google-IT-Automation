# Use the command-line
The command-line is used to tell your computer what to do. You can use it to access servers, move files, change directories, and write scripts. 

In this reading, you will learn how to write Python scripts at the command-line along with the Python GUI IDLE. 

We will also cover the different ways you can access the command-line based on your operating system. 

## Using the command line on MacOS

- Using the spotlight search, type in “terminal.” 
- Select the terminal application. You should see your username followed by the $ sign. 
- MacOS comes with Python 2.7 pre-installed. 
- You can install Python 3 from [python.org](https://www.python.org/)
- Just remember, this means that you will have 2 versions of Python installed on your Mac, and you will need to pay special attention to your paths.
- To check which version of Python you have installed on your Mac, use the following command.

    ```bash
    python --version
    ```
- To check for Python3, use the following command. 

    ```bash
    python3 --version
    ```

## Using the command line on Windows OS
- In Windows, open the start menu. In the search box type cmd. 
- Right-click on cmd and select Run as administrator. 
- This will open up the command-line. 
- Windows OS does not come with Python installed. 
- Visit the official Python [download page](https://www.python.org/downloads/windows/) for Windows. 
- Select the Windows installer (64-bit) or (32-bit). 
- After the installer is downloaded, double–click the file. 
- Select **Install launcher for all users**. 
- Follow the prompts during installation. 
- Make sure to select the **Add python.exe PATH checkbox**. 
- This will allow you to launch Python from the command line. 
- Once installation is complete, you can check for Python from the command line.
- To check for Python, use the following command. The version of Python you installed will appear. 

    ```powershell
    python --version
    ```

## Using the command line on Linux OS
- Access the Linux terminal using Ctrl + Alt + T. 
- This will allow you to check for Python. 
- Type python. 
- Python comes preinstalled on most Linux systems. 
- If the command is not found, you can install Python by writing `sudo apt install python3`. 
- You can begin writing Python code from the terminal. 
- Simply type python to use the interactive mode.
-  You can also write Python scripts using Linux with IDLE which we will cover next. 


## Using IDLE
- Python IDLE is included with Python installations on Windows and MacOS. You can download IDLE using your package manager on Linux. 

- Python IDLE is an interactive interpreter or file editor that allows you to easily write Python scripts and programs. IDLE provides syntax highlighting, code completion, and automatic indentation. 

- Double click on the IDLE icon to open it on your computer. This will open a blank Python interpreter window. You can begin writing code right away. 

    ![alt text](/resources/idle.png)

    You can also open a new file. Go to File → Open → New File from the menu bar. Here you can write a Python file. Once you have completed writing your Python code in the file, go to File → Save As. Give your Python file a name. Hit Save. To run the Python code in the file you saved click Run → Run Module from the menu.

    ![alt text](/resources/example_idle.png)

## Key takeaways

Whichever operating system you are using, you will be able to run Python from the command-line.  Using a text editor like IDLE and running python from the command-line  is best for executing and debugging individual scripts or .py files. 

## Resources for more information
Here is a list of additional resources for writing and running Python on your local machine. 

- A [guide](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955) to using terminal (command-line) on Mac, Windows, and Linux operating systems. 

- [IDLE documentation and instructions](https://docs.python.org/3/library/idle.html)

- [Python Scripts vs. Jupyter Notebooks](https://learnpython.com/blog/python-scripts-vs-jupyter-notebooks/)


