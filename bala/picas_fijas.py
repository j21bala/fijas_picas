#Le pido al usuaio el número
numero = input("Ingresa un número de 4 dígitos diferentes: ")
#Convierto numero de tipo STRING a tipo LIST
digitos = list(numero)
#Utilizo un set para comprobar que los números no sean iguales
cadena = set(digitos)
while len(digitos) == 4 and len(digitos) == len(cadena):

    #Definimos la primera función que establece la lógica de fijas y picas

    def comprobar_picas_fijas(cadena, suposicion):
        fijas = 0
        picas = 0
        for i in range (len(cadena)):
            if cadena[i] == suposicion[i]:
                fijas += 1
            elif suposicion[i] in cadena:
        
                picas +=1
                
        return fijas, picas

            








    


    





