import os
import platform
import time

# Función para imprimir en verde
def print_green(text):
    print(f"\033[92m{text}\033[0m")

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
print_green(logo)

# Solicitar al usuario la IP o dominio
target = input("Introduce la IP o dominio: ")

# Determinar el comando de ping según el sistema operativo
param = '-n' if platform.system().lower() == 'windows' else '-c'

# Función para realizar ping y procesar la respuesta
def ping_target(target):
    response = os.popen(f"ping {param} 4 {target}").read()
    if "Request timed out" in response or "100% packet loss" in response:
        print_green("El Servidor Web está caído")
    else:
        packet_loss = 0
        total_time = 0
        count = 0
        for line in response.split('\n'):
            if "time=" in line:
                print_green(line)
                time_ms = int(line.split('time=')[1].split('ms')[0].strip())
                total_time += time_ms
                count += 1
            elif "loss" in line:
                packet_loss = int(line.split('%')[0].split()[-1])
        if count > 0:
            avg_time = total_time / count
            print_green(f"Latencia promedio: {avg_time:.2f} ms")
        print_green(f"Paquetes perdidos: {packet_loss}%")

# Realizar pings en un bucle
while True:
    ping_target(target)
    time.sleep(1)
    
