import subprocess as sp


def get_user_passwd(user):

    passwd_entry = sp.run(['grep', user, '/etc/passwd'], check=True)
    if passwd_entry.returncode == 0:
        passwd_entry.stdout.decode('utf-8').split(':')[1]

        def get_user_groups(user):
            groups = sp.run(['groups', user], check=True)
            groups.stdout.decode('utf-8').split()
        
        # Create a dictionary of user information
        user_struct = {}
        user = user_struct['username'] = passwd_entry[0]
        user_uid = user_struct['uid'] = passwd_entry[2]
        user_gid = user_struct['gid'] = passwd_entry[3]
        user_home_dir = user_struct['home_dir'] = passwd_entry[5]
        user_shell = user_struct['shell'] = passwd_entry[6]
        user_secondary_groups = user_struct['secondary_groups'] = get_user_groups(
            user)

    elif passwd_entry.returncode == 1:
        print("User not found or mispelled!")


def create_user(user_struct):
    sp.run(['useradd', '-u', user_struct['uid'], '-g', user_struct['gid'], '-d',
           user_struct['home_dir'], '-s', user_struct['shell'], user_struct['username']], check=True)
    for group in user_struct['secondary_groups']:
        sp.run(['usermod', '-a', '-G', group,
               user_struct['username']], check=True)
    return user_struct


def main():
    pass


if __name__ == '__main__':
    # Get username to check in passwd
    # Create a list of user attributes from passwd entry.
    # Check if gid is the same as as uid.
    # if not, check /etc/group for gid and say entry
    main()