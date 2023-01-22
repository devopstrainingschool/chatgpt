import subprocess

def setup_nfs_server():
    subprocess.run(["yum", "install", "-y", "nfs-utils"])
    subprocess.run(["systemctl", "enable", "rpcbind"])
    subprocess.run(["systemctl", "enable", "nfs-server"])
    subprocess.run(["systemctl", "start", "rpcbind"])
    subprocess.run(["systemctl", "start", "nfs-server"])

    with open("/etc/exports", "a") as exports:
        exports.write("/path/to/export *(rw,sync,no_root_squash)")

    subprocess.run(["exportfs", "-a"])

if __name__ == "__main__":
    setup_nfs_server()
