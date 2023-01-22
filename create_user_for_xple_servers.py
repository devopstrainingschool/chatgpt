import subprocess

def add_user():
    username = input("Enter a username: ")
    servers_passwords = {}
    servers = input("Enter a list of servers in the format of 'username@hostname', separated by commas: ").split(",")
    for server in servers:
        password = input(f"Enter password for {server}: ")
        servers_passwords[server] = password

    for server in servers:
        try:
            subprocess.run(["sshpass", "-p", servers_passwords[server], "ssh", "-o", "StrictHostKeyChecking=no", server, "useradd", "-m", "-s", "/bin/bash", "-p", servers_passwords[server], username], check=True)
            print(f"User {username} created successfully on server {server}!")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create user on server {server}: {e}")

if __name__ == "__main__":
    add_user()
