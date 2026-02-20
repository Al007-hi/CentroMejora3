from colorama import Fore

def pedir_nombre():
    while True:
        nombre = input("Nombre y apellidos: ").strip()
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print(Fore.RED + "❌ Pon solo letras y espacios.")


def pedir_edad():
    while True:
        edad_input = input("Edad: ").strip()
        if edad_input.isdigit():
            edad = int(edad_input)
            if 16 <= edad <= 100:
                return edad
            else:
                print(Fore.RED + "❌ La edad debe estar entre 16 y 100.")
        else:
            print(Fore.RED + "❌ Introduce un número válido para la edad.")


def pedir_nota(texto):
    while True:
        valor = input(texto).replace(",", ".").strip()
        try:
            nota = float(valor)
            if 0 <= nota <= 10:
                return nota
            else:
                print(Fore.RED + "❌ La nota debe estar entre 0 y 10.")
        except ValueError:
            print(Fore.RED + "❌ Introduce un número válido.")


def pedir_asistencia():
    while True:
        valor = input("Asistencia (%): ").replace(",", ".").strip()
        try:
            asistencia = float(valor)
            if 0 <= asistencia <= 100:
                return asistencia
            else:
                print(Fore.RED + "❌ La asistencia debe estar entre 0 y 100.")
        except ValueError:
            print(Fore.RED + "❌ Introduce un número válido.")
