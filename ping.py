import os
import platform
import time

# Función para imprimir en verde
def print_green(text):
    print(f"\033[92m{text}\033[0m")

# Función para imprimir en rojo
def print_red(text):
    print(f"\033[91m{text}\033[0m")

# Función para imprimir en blanco
def print_white(text):
    print(f"\033[97m{text}\033[0m")

# Logo de texto en rojo brillante
logo = """
\033[91m
██████╗ ██╗███╗   ██╗ ██████╗ 
██╔══██╗██║████╗  ██║██╔════╝ 
██████╔╝██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║██║╚██╗██║██║   ██║
██║     ██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
\033[0m
"""

# Mostrar el logo
print_red(logo)

# Solicitar al usuario la IP o dominio
target = input("Introduce la IP o dominio: ")

# Determinar el comando de ping según el sistema operativo
param = '-n' if platform.system().lower() == 'windows' else '-c'

# Función para realizar ping y procesar la respuesta
def ping_target(target):
    response = os.popen(f"ping {param} 1 {target}").read()
    if "Request timed out" in response or "100% packet loss" in response:
        print_red("Web down")
    else:
        for line in response.split('\n'):
            if "time=" in line:
                print_green(line)
            else:
                print_white(line)

# Realizar pings en un bucle
while True:
    ping_target(target)
    time.sleep(1)
    
