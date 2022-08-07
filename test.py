import subprocess as sp

def get_username():
    try:
        username = input("Please enter a username: ")
        if not username:
            raise ValueError("Empty input, Username need to be supplied!")
        else:
            passwd_entry = sp.run(['grep', username, '/etc/passwd'], capture_output=True)
            if passwd_entry.returncode == 1:
                print("User not found!")
            elif passwd_entry.returncode == 0:
                print("User found!")
                user_lst = passwd_entry.stdout.decode().split(':')
            else:
                print("Something went wrong!")
                print(passwd_entry.returncode)
    except ValueError as Error:
        print(Error)
        username = input("Please enter a username: ")
    return user_lst

data = get_username()
print(data)