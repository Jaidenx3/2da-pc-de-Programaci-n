"""
Desarrolle un programa en C++ que gestione el registro, consulta y cálculo de datos académicos de alumnos,
permitiendo ingresar información como el código, nombre, género, edad y notas de diversas asignaturas 
(curso 1, curso 2 y curso 3), calcular el promedio de notas de cada alumno y presentar un menú con opciones 
para registrar datos, ver la lista de alumnos, ver Notas por Asignatura, Calcular el promedio y Mostrar Primero y Ultimo.
"""

def registrar_alumno(estudiantes):
    while True:
        codigo = input("Ingrese el código del alumno (solo números): ")
        if codigo.isdigit():
            break
        else:
            print("Error: El código debe contener solo números. Intente de nuevo.")
    nombre = input("Ingrese el nombre del alumno: ")
    genero = input("Ingrese el género del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    while True:
        curso1 = float(input("Ingrese la nota del curso 1 (0 a 20): "))
        if 0 <= curso1 <= 20:
            break
        else:
            print("Error: La nota debe estar entre 0 y 20. Intente de nuevo.")
    
    while True:
        curso2 = float(input("Ingrese la nota del curso 2 (0 a 20): "))
        if 0 <= curso2 <= 20:
            break
        else:
            print("Error: La nota debe estar entre 0 y 20. Intente de nuevo.")
    
    while True:
        curso3 = float(input("Ingrese la nota del curso 3 (0 a 20): "))
        if 0 <= curso3 <= 20:
            break
        else:
            print("Error: La nota debe estar entre 0 y 20. Intente de nuevo.")

    promedio = calcular_promedio(curso1, curso2, curso3)
    estudiante = {
        'codigo': codigo,
        'nombre': nombre,
        'genero': genero,
        'edad': edad,
        'curso1': curso1,
        'curso2': curso2,
        'curso3': curso3,
        'promedio': promedio
    }
    estudiantes.append(estudiante)

def mostrar(estudiantes):
    for estudiante in estudiantes:
        print(f"Codigo: {estudiante['codigo']}, Nombre: {estudiante['nombre']}, "
              f"Género: {estudiante['genero']}, Edad: {estudiante['edad']} ")

def asignatura(estudiantes):
    for estudiante in estudiantes:
        print(f"Codigo: {estudiante['codigo']}, Nombre: {estudiante['nombre']}, "
              f"Curso 1: {estudiante['curso1']}, Curso 2: {estudiante['curso2']}, "
              f"Curso 3: {estudiante['curso3']}")
    
def calcular_promedio(curso1, curso2, curso3):
    return (curso1 + curso2 + curso3) / 3

def mostrar_promedios(estudiantes):
    for estudiante in estudiantes:
        print(f"Codigo: {estudiante['codigo']}, Nombre: {estudiante['nombre']}, "
              f"Promedio: {estudiante['promedio']:.2f}")

def mostrar_primero_y_ultimo(estudiantes):
    if estudiantes:
        primero = estudiantes[0]
        ultimo = estudiantes[-1]
        print("Primero en la lista:")
        print(f"Codigo: {primero['codigo']}, Nombre: {primero['nombre']}, "
              f"Género: {primero['genero']}, Edad: {primero['edad']}, "
              f"Promedio: {primero['promedio']:.2f}")
        print("Último en la lista:")
        print(f"Codigo: {ultimo['codigo']}, Nombre: {ultimo['nombre']}, "
              f"Género: {ultimo['genero']}, Edad: {ultimo['edad']}, "
              f"Promedio: {ultimo['promedio']:.2f}")
    else:
        print("No hay alumnos registrados.")

def datos():
    estudiantes = []
    
    while True:
        print("\nMenu:")
        print("1. Registrar datos")
        print("2. Ver lista de alumnos")
        print("3. Ver notas por asignatura")
        print("4. Calcular promedios")
        print("5. Mostrar primero y ultimo")
        print("6. Salir")
        print("")
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            registrar_alumno(estudiantes)
        elif opcion == 2:
            mostrar(estudiantes)
        elif opcion == 3:
            asignatura(estudiantes)
        elif opcion == 4:
            mostrar_promedios(estudiantes)
        elif opcion == 5:
            mostrar_primero_y_ultimo(estudiantes)
        elif opcion == 6:
            print("Adios!")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")

datos()