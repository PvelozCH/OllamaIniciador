import subprocess
import os
#Colores a utilizar
CELESTE = "\033[96m"
ORIGINAL = "\033[0m"
VERDE = "\033[92m"

def iniciarOllama():
    subprocess.run(["bash", "ejecutarOllama.sh"])
def titulo():
    print(rf"""{CELESTE}
    ________  .__  .__
    \_____  \ |  | |  | _____    _____ _____
    /   |   \|  | |  | \__  \  /     \\__  \
   /    |    \  |_|  |__/ __ \|  Y Y  \/ __ \_
   \_______  /____/____(____  /__|_|  (____  /
           \/               \/      \/     \/
   ________ .___   _____
   \_____  \|   | /  _  \
     _(__  <|   |/  /_\  \
    /       \   /    |    \
   /______  /___\____|__  /
          \/            \/
 
 {ORIGINAL}""")



#Menu inicial
def menu():
    while True:
        os.system("clear")
        titulo()
        print(rf"{VERDE}╔══════════════════════════╗")
        print("║ 1. Iniciar OLLAMA        ║")
        print("║ 2. Subir archivo         ║")
        print("║ 3. Salir                 ║")
        print("╚══════════════════════════╝")
        print(f"{ORIGINAL}")
        opcion = input("👉 Elige una opción (1-3): ")

        if opcion == "1":
            iniciarOllama()
            input("Presiona Enter para continuar...")
        elif opcion == "2":
            print("⚠️ Caractetística no implementada aún")
            input("Presiona Enter para continuar...")
        elif opcion == "3":
            print("👋 Has elegido salir. ¡Adiós!")
            input("Presiona Enter para continuar...")
            os.system("clear")
            break
        else:
            print("⚠️ Opción no válida.")
            input("Presiona Enter para continuar...")

#ejecutar menu
menu()

