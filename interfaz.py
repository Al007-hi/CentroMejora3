import time
from colorama import init, Fore

init(autoreset=True)

def pantalla_inicio(centro):
    print(Fore.CYAN + f"-- Control de Promoción del {centro} --")
    time.sleep(1)
    print(Fore.YELLOW + "+-----------------------------------------------------+")
    print(Fore.YELLOW + "|--------------- Entrando en el sistema --------------|")
    time.sleep(1)
    print(Fore.YELLOW + "|-----------------------------------------------------|")
    print(Fore.YELLOW + "|--------------------- Cargando... -------------------|")
    time.sleep(2)
    print(Fore.YELLOW + "|" + Fore.GREEN + "███████████████████████ 100% ████████████████████████" + Fore.YELLOW + "|")
    print(Fore.YELLOW + "+-----------------------------------------------------+")
    time.sleep(1)
    print(Fore.YELLOW + "+---------------- Hola, BIENVENIDO/A -----------------+")
    print(Fore.YELLOW + f"|== Registro de alumnado en {centro} ==|")
    print(Fore.YELLOW + "+-----------------------------------------------------+")

#Arriba se ecuentra el inicio, la llamo desde el main como pantalla_inicio
#Sin embargo abajo aparece el informe que es lo ultimo que sale, lo importatne
#es que imprimir_informe tiene todas las variables importantes

def imprimir_informe(nombre, edad, n1, n2, n3, media, asistencia, promociona):
    print(Fore.YELLOW + "|---------------------------------------------|")
    print(Fore.YELLOW + "|=============== INFORME FINAL ===============|")

    if edad < 18:
        print(f"Edad: {edad} -> Menor de edad")
    else:
        print(f"Edad: {edad} -> Adulto")

    print(f"Alumno/a: {nombre}")
    print(f"Notas: {n1}, {n2}, {n3}")
    print(f"Media: {media:.2f}")
    print(f"Asistencia: {asistencia}%")
    print(f"¿Promociona?: {promociona}")

    if promociona:
        print(Fore.GREEN + "|---------  FELICIDADES  ---------|")
    else:
        print(Fore.YELLOW + "|-----------  ÁNIMO  -----------|")
