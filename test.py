import subprocess as sp
import sys

def get_username():
    try:
        username = input("Please enter a username: ")
        if not username:
            raise ValueError("Empty input, Username need to be supplied!")
        else:
            user_exists = sp.run(['grep',username, '/etc/passwd'], stdout=sp.DEVNULL)
            if user_exists.returncode == 1:
                print("User not found!")
            elif user_exists.returncode == 0:
                print("User found!")
                user_lst = sp.check_output(['grep',username, '/etc/passwd']).decode('utf-8').split(':')
            else:
                print("Something went wrong!")
                print(passwd_entry.returncode)
    except ValueError as Error:
        print(Error)
        username = input("Please enter a username: ")
    return user_lst

if sys.version_info.major == 2:
    print("Script needs to run with python3 at the moment")
elif sys.version_info.major == 3:
    data = get_username()
    groups = sp.check_output(['groups',data[0]]).decode('utf-8').split()
    print(groups[2:])
    