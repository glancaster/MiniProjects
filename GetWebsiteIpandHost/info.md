# Get Website Ip and Host Information

# Description
User will be able to enter in a website address and it return be given the ip address and host name of the website. 

Tags: Python, Networking
Libraries: socket

# Introduction
1. We will import in the socket library from Python.
`import socket`

2. Set up a function that we can use to process the task.
`def get_hostname_IP():
    pass`

3. We want the user to supply the website for the task so we'll use Python's built-in `input()`
`hostname = input("Enter Website Address: ")`
This will pop up in the terminal with the message "Enter Website Address: ", the user will be able to supply whatever they want.

4. Since we hope that they'll supply the right website that the socket library will accept, we need to wrap it in a try-except statement.
`try:
    # some logic
except:
    # some logic if it fails`

5. The hostname is also the website address that they gave so we can print that out to the terminal.
For the Ip address, the `socket.gethostbyname()` will be used and since it's the only call, we can wrap it into the print statement with a f-string.
`print(f"Hostname: {hostname}")
print(f"IP: {socket.gethostbyname(hostname)}")`

6. If the logic fails, let's have the user come here for the right details.
`print("Invalid Hostname, see info.md")`
# Code 
See main.py.

# Tests
Run `python -m pytest main.py`
