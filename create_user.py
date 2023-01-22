import subprocess

def add_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    try:
        subprocess.run(["useradd", "-m", "-s", "/bin/bash", "-p", password, username], check=True)
        print(f"User {username} created successfully!")
    except subprocess.CalledProcessError as e:
        print("Failed to create user:", e)

if __name__ == "__main__":
    add_user()
