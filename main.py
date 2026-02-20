from interfaz import pantalla_inicio, imprimir_informe
from validaciones import pedir_nombre, pedir_edad, pedir_nota, pedir_asistencia
from calculos import calcular_media, comprobar_promocion


centro = "CIPFP Luís Suñer Sanchis"
pantalla_inicio(centro)

alumnos = [] 


while True:
    print("--- Nuevo alumno ---")

    nombre = pedir_nombre()
    edad = pedir_edad()

    n1 = pedir_nota("Nota evaluación 1 (0-10): ")
    n2 = pedir_nota("Nota evaluación 2 (0-10): ")
    n3 = pedir_nota("Nota evaluación 3 (0-10): ")

    asistencia = pedir_asistencia()

    media = calcular_media(n1, n2, n3)
    promociona = comprobar_promocion(media, asistencia)

    alumno = {
        "nombre": nombre,
        "edad": edad,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "asistencia": asistencia,
        "media": media,
        "promociona": promociona
    }

    alumnos.append(alumno)

    # PREGUNTA DESPUÉS DE LA ASISTENCIA
    continuar = input("¿Quieres añadir otro usuario? (s/n): ").lower().strip()
    #Si si que quierie otro usuario empieza desde arriba (la intro no)
    if continuar != "s":
        break


print("=== ALUMNOS REGISTRADOS ===")

for i, alumno in enumerate(alumnos, start=1):
    print(f"{i}. {alumno['nombre']}")

while True:
    opcion = input("¿De qué alumno quieres el informe? (número): ").strip()

    if opcion.isdigit():
        indice = int(opcion) - 1
        if 0 <= indice < len(alumnos):
            alumno = alumnos[indice]
            break
        else:
            print("❌ Número fuera de rango.")
    else:
        print("❌ Introduce un número válido.")


imprimir_informe(
    alumno["nombre"],
    alumno["edad"],
    alumno["n1"],
    alumno["n2"],
    alumno["n3"],
    alumno["media"],
    alumno["asistencia"],
    alumno["promociona"]
)
