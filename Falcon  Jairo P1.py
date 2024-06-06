#https://github.com/Jaidenx3/2da-pc-de-Programaci-n
enfermedades = ["gripe","indigestión","catarro","resfriado común","mononucleosis","artritis","gastritis","apendicitis","fibromialgia","epilepsia"]
síntomas = ["fiebre","tos","dolor de garganta","nauseas","dolor abdominal","dolor en las articulaciones","sudoración excesiva","escalofríos","mareos","dolor de espalda"]
Sintomatologías = [[0,0,0,0,0,0,0,0,0,1],
                   [0,0,0,0,0,0,0,0,1,1],
                   [0,0,0,0,0,0,0,1,1,1],
                   [0,0,0,0,0,0,1,1,1,1],
                   [0,0,0,0,0,1,1,1,1,1],
                   [0,0,0,0,1,1,1,1,1,1],
                   [0,0,0,1,1,1,1,1,1,1],
                   [0,0,1,1,1,1,1,1,1,1],
                   [0,1,1,1,1,1,1,1,1,1],
                   [1,1,1,1,1,1,1,1,1,1]]

def Enfermedad():
    paciente = []

    print("Pon 1 si presenta o 0 sino presenta:")
    
    for i in range(10):
        while True:
            try:
                X = int(input(f"Ingrese si padece {síntomas[i]}: "))
                if X not in [0, 1]:
                    print("Error: opción no válida.")
                    continue
                break
            except ValueError:
                print("Error: opción no válida. Ingrese solo 0 o 1.")
        
        paciente.append(X)
    
    encontrado = False
    for i, sintomas in enumerate(Sintomatologías):
        if paciente == sintomas:
            print(f"Usted padece de {enfermedades[i]}")
            encontrado = True
            break
    
    if not encontrado:
        print("No existen coincidencias.")

Enfermedad()
