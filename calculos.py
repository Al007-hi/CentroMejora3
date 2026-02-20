def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3
#Esto de arriba o suma los tres y lo divide entre 3


def comprobar_promocion(media, asistencia):
    aprobado_por_media = media >= 5
    aprobado_por_asistencia = asistencia >= 85
    return aprobado_por_media and aprobado_por_asistencia
