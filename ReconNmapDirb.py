import os
import subprocess

def run_nmap(target):
    print(f"Ejecutando Nmap en {target}...")
    nmap_command = f"nmap -sS -sV -oN nmap_results.txt {target}"
    subprocess.run(nmap_command, shell=True)
    print("Resultados de Nmap guardados en nmap_results.txt")

def run_dirb(target):
    print(f"Ejecutando Dirb en {target}...")
    dirb_command = f"dirb http://{target} -o dirb_results.txt"
    subprocess.run(dirb_command, shell=True)
    print("Resultados de Dirb guardados en dirb_results.txt")

def main():
    target = input("Introduce la dirección IP o el dominio a escanear: ")
    
    run_nmap(target)
    run_dirb(target)

if __name__ == "__main__":
    main()
