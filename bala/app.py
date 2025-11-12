import sys

# Le pido al usuaio el número
numero = input("Ingresa un número de 4 dígitos diferentes: ")
# Convierto numero de tipo STRING a tipo LIST
digitos = list(numero)
# Utilizo un set para comprobar que los números no sean iguales
cadena_set = set(digitos)


while len(digitos) == 4 and len(digitos) == len(cadena_set):

    # Función para generar cada número del 0-9 y unirlos con el set en forma de lista 
    def generar_num():

        candidatos = []
        for d1 in range(10):
            for d2 in range(10):
                for d3 in range(10):
                    for d4 in range(10):
                        suposicion = str(d1) + str(d2) + str(d3) + str(d4)
                        if len(set(suposicion)) == 4:
                            # Ponemos la lista adentro del array de candidatos y lo retornamos
                            candidatos.append(suposicion)
        return candidatos


    # Integramos la lógica del juego con otra función
    def comprobar_picas_fijas(suposicion, candidato):
        fijas = 0
        picas = 0
        
        for i in range (4):
            if suposicion[i] == candidato[i]:
                fijas += 1
            elif candidato[i] in suposicion:
                picas += 1
                
        return fijas, picas
    
    
    def buscar_num():
        
        numero_candidato = generar_num()
        intentos = 0
        fijas = 0

        print("\n<----Juego de Picas y Fijas (El Programa Adivina)---->")
        print(f"Total de candidatos iniciales: {len(numero_candidato)}")

        while fijas != 4 and numero_candidato:
            intentos += 1

            numero_suposicion = numero_candidato[0]

            print(f"\nIntento #{intentos}, Mi suposición es: **{numero_suposicion}**")
            
            while True:
                try:
                    fijas = int(input(f"¿Cuantas fijas tiene {numero_suposicion}?: "))
                    picas = int(input(f"¿Cuantas picas tiene {numero_suposicion}?: "))

                    if 0 <= fijas <= 4 and 0 <= picas <= 4 and (fijas + picas) <= 4:
                        break
                    else:
                        print("La cantidad no puede exceder 4, intentalo de nuevo")

                except ValueError:
                    print("Ingresa un número entero válido")

            if fijas == 4:
                print(f"\n ¡Adiviné tu número! Es: {numero_suposicion} en {intentos} intentos.")
                return
            
            nueva_lista = []
            
            for candidato in numero_candidato:
                f, p = comprobar_picas_fijas(numero_suposicion, candidato)

                if f == fijas and p == picas:
                    nueva_lista.append(candidato)

            numero_candidato = nueva_lista
            
            print(f"Candidatos restantes: {len(numero_candidato)}")

        if not numero_candidato and fijas != 4:
            print("\n Error: No quedan candidatos válidos. Es probable que haya habido un error con las respuestas de fijas/picas.")

    
    buscar_num()
    break 

else:
    print("\n El juego no puede iniciar. El número ingresado debe ser de 4 dígitos diferentes.")