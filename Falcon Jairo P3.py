"""
Desarrollar  un  programa  en  C++  que  permita  ingresar  y  almacenar  el  código,  el  nombre, nota 1, 
nota 2 y nota 3 de un curso. Mostrar el promedio de cada estudiante y la cantidad de estudiantes desaprobados. 
Finalmente, ordene los datos en base de los promedios. Muestre los datos ordenados. 
"""

def promedios(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def mostrar(estudiantes):
    for estudiante in estudiantes:
        print(f"Codigo: {estudiante['codigo']}, Nombre: {estudiante['nombre']}, "
              f"Nota 1: {estudiante['nota1']}, Nota 2: {estudiante['nota2']}, "
              f"Nota 3: {estudiante['nota3']}, Promedio: {estudiante['promedio']:.2f}")

def ingresar_nota(nota_num):
    while True:
        nota = float(input(f"Ingrese la nota {nota_num} (0 a 20): "))
        if 0 <= nota <= 20:
            return nota
        else:
            print("La nota debe estar entre 0 y 20. Intente de nuevo.")

def ordenar(estudiantes):
    return sorted(estudiantes, key=lambda x: x['promedio'], reverse=True)

def Datos():
    estudiantes = []
    n = int(input("Ingrese la cantidad de estudiantes: "))
    
    for _ in range(n):
        while True:
            codigo = input("Ingrese el codigo del estudiante (solo numeros): ")
            if codigo.isdigit():
                codigo = int(codigo)
                break
            else:
                print("El código debe ser un número. Intente de nuevo.")
        nombre = input("Ingrese el nombre del estudiante: ")
        nota1 = ingresar_nota(1)
        nota2 = ingresar_nota(2)
        nota3 = ingresar_nota(3)
        
        promedio = promedios(nota1, nota2, nota3)
        estudiante = {
            'codigo': codigo,
            'nombre': nombre,
            'nota1': nota1,
            'nota2': nota2,
            'nota3': nota3,
            'promedio': promedio
        }
        estudiantes.append(estudiante)
    
    desaprobados = sum(1 for estudiante in estudiantes if estudiante['promedio'] < 10.5)
    
    print("\nPromedios de los estudiantes:")
    mostrar(estudiantes)
    
    print(f"\nCantidad de estudiantes desaprobados: {desaprobados}")
    
    estudiantes_ordenados = ordenar(estudiantes)

    print("\nEstudiantes ordenados por promedio:")
    mostrar(estudiantes)

Datos()