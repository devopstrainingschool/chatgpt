import subprocess

def add_user(username, password):
    try:
        subprocess.run(["useradd", "-m", "-s", "/bin/bash", "-p", password, username], check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to create user:", e)

if __name__ == "__main__":
    add_user("example", "password")
