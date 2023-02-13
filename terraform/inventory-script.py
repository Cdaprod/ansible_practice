import socket

def get_host_name():
    """Returns the host name of the current machine."""
    return socket.gethostname()

def get_ip_address():
    """Returns the IP address of the current machine."""
    return socket.gethostbyname(socket.gethostname())

def main():
    """Main function to gather information about the network."""
    host_name = get_host_name()
    ip_address = get_ip_address()
    print(f"Host Name: {host_name}")
    print(f"IP Address: {ip_address}")

if __name__ == "__main__":
    main()
