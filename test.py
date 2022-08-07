import subprocess as sp

try:
     user = input("Please enter a username: ")
     if not user:
        raise ValueError("Empty input, Username need to be supplied!")
except ValueError as Error:
    print(Error)

passwd_entry = sp.run(['grep', user, '/etc/passwd'], check=True)