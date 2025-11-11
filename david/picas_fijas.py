
import secrets
import getpass
from  collections import Counter
from typing import List,Tuple,Dict


# Lo que se tiene que tener de cuenta es realizar el juego ademas establecer que tambien deve hacer la inversa del algoritmo osea que el cliente piensa un numero y la maquina se lo descubre 




#MENU 1
#almacenar el numero secreto por el sistema (el usuario no lo ve)

# generar numero secreto rnd

rnd = secrets.SystemRandom()

def generar_numero_secreto(allow_leadign_zero: bool = False) -> str:
    #creamos la cadena de 4 numeros secretos sin repeticion etre ellos
    digits = list('0123456789')
    if allow_leadign_zero:
        seleccion = rnd.sample(digits,4)
    else:
        primero = rnd.choice(digits[1:])
        restante = rnd.sample([d for d in digits if d != primero],3)
        seleccion = [primero] + restante
    return ''.join(seleccion)
def generar_todas_posibilidades(allow_leadign_zero: bool = False)->List[str]:
    digits = list('0123456789')
    todas_posibilidades = []
    for d1 in digits:
        if not allow_leadign_zero and d1 == '0':
            continue
        for d2 in digits:
            if d2 == d1:
                continue
            for d3 in digits:
                if d3 in (d1,d2):
                    continue
                for d4 in digits:
                    if d4 in (d1,d2,d3):
                        continue
                    todas_posibilidades.append(d1+d2+d3+d4)
    return todas_posibilidades
# Validacion de cuantas picas y fijas tenemos
def calcular_picas_fijas(secret:str,guess:str)->Dict[str,int]:
    if len(secret) != len(guess):
        raise ValueError("Los numeros deben tener la misma longitud")
    fijas = sum(s==g for s,g in zip(secret,guess))
    c_secret = Counter(secret)
    c_guess = Counter(guess)
    coincidencias_totales = sum(min(c_secret[d],c_guess[d]) for d in c_secret)
    picas = coincidencias_totales -fijas
    return {'picas':picas,'fijas':fijas}


def pedir_numero_4_digitos(prompt:str,hide:bool=False,allow_repeats:bool=False)->str:
    while True:
        try:
            if hide:
                s = getpass.getpass(prompt).strip()
            else:
                s= input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada interrumpida . Saliendo del Algoritmo........")
            raise SystemExit
        if not s:
            print("Entrada vacia. Intenta de nuevo por favor.")
            continue
        if not s.isdigit():
            print("Solo se permiten numeros de 0-9 intenta de nuevo por favor.")
            continue
        if len(s) !=4:
            print("El numero debe tener exactamente 4 digitos. Intenta de nuevo por favor.")
            continue
        if (not allow_repeats) and len(set(s)) !=4:
            print("Los digitos no deben repetirse. Intenta de nuevo por favor.")
            continue
        return s
    

def pedir_picas_fijas_usuario()->Tuple[int,int]:
    #aca solicitamos al usuario que ingrese el numero de picas y fijas que salen mediante le numero que damos por consola
    while True:
        try:
            p = input("Ingresa el numero de Picas (0-4): ").strip()
            f = input("Ingresa el numero de Fijas (0-4): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada interrumpida. Saliendo del Algoritmo........")
            raise SystemExit
        if not (p.isdigit() and f.isdigit()):
            print("Solo se permiten numeros enteros. Intenta de nuevo por favor.")
            continue
        picas = int(p)
        fijas = int(f)
        if picas <0 or fijas <0 or picas >4 or fijas >4:
            print("Los numeros deben estar entre 0 y 4. Intenta de nuevo por favor.")
            continue
        if picas + fijas >4:
            print("La suma de picas y fijas no puede ser mayor a 4. Intenta de nuevo por favor.")
            continue
        return picas,fijas
    
def filtrar_candidatos(candidates:List[str],guess:str,feedback:Tuple[int,int])->List[str]:
    picas_esperadas, fijas_esperadas = feedback
    nuevos_candidatos = []
    for candidate in candidates:
        resultado = calcular_picas_fijas(candidate,guess)
        if resultado['picas'] == picas_esperadas and resultado['fijas'] == fijas_esperadas:
            nuevos_candidatos.append(candidate)
    return nuevos_candidatos

def juego_consola():
    print("==== PICAS Y FIJAS: Esta pc VS Tu(vago) ====")
    print("Reglas: números de 4 dígitos sin dígitos repetidos, no empiezan con 0.")
    print("Primero el usuario dispara (intenta adivinar el número de la máquina).")
    print("Luego la máquina dispara y el usuario da la respuesta (picas y fijas).")
    print("Gana el que consiga 4 fijas primero.\n")

    maquina_numero = generar_numero_secreto()
    usuario_sercreto= pedir_numero_4_digitos("Piensa un numero de 4 digitos sin repetir (la maquina no vera este numero cofia en ti): ",hide=True)
    candidates=generar_todas_posibilidades()
    user_shots = 0
    machine_shots = 0

    turno = 0
    while True:
        # Turno usuario
        print("\n-- Tu turno --")
        intento = pedir_numero_4_digitos("Tu intento: ", hide=False)
        user_shots += 1
        resultado = calcular_picas_fijas(maquina_numero, intento)
        print(f"Resultado: Fijas = {resultado['fijas']}, Picas = {resultado['picas']}")
        if resultado['fijas'] == 4:
            print("\n¡GENIAL! ERES EL GANADOR.")
            print(f"Intentos del usuario: {user_shots}")
            print(f"Intentos de la máquina: {machine_shots}")
            break
        # Turno máquina
        print("\n-- Turno de la máquina --")
        if not candidates:
            # Si por alguna razón la lista se quedó vacía, regeneramos todas las posibilidades
            print("Advertencia: la lista de candidatos se ha quedado vacía (posible feedback inconsistente).")
            print("La máquina seleccionará una suposición aleatoria entre todas las posibilidades.")
            candidates = generar_todas_posibilidades()
        machine_guess = rnd.choice(candidates)
        print(f"La máquina propone: {machine_guess}")
        print("Por favor, responde cuántas Picas y cuántas Fijas tiene esa propuesta respecto a TU número secreto.")
        # Pedir feedback al usuario
        while True:
            p_i, f_i = pedir_picas_fijas_usuario()
            machine_shots += 1
            if f_i == 4:
                print("\nLa máquina ha adivinado tu número. ¡La máquina gana!")
                print(f"Intentos del usuario: {user_shots}")
                print(f"Intentos de la máquina: {machine_shots}")
                return
            # Intentamos filtrar candidatos con ese feedback
            nuevos = filtrar_candidatos(candidates, machine_guess, (p_i, f_i))
            if not nuevos:
                # feedback inconsistente con candidatos actuales (posible error del usuario)
                print("El feedback ingresado deja 0 candidatos posibles (inconsistente con su feedback previo).")
                print("Por favor verifica que ingresaste correctamente picas y fijas para la propuesta.")
                # Preguntar si desea reingresar feedback o forzar continuar
                opcion = input("Reingresar feedback? (s/n): ").strip().lower()
                if opcion in ('s','si','y','yes',''):
                    # repetir pedir picas/fijas (no aumentar máquina_shots aquí, ya aumentó antes)
                    continue
                else:
                    # Forzamos no filtrar (para seguir jugando), o regeneramos todas las posibilidades
                    print("La máquina regenerará el conjunto completo de candidatos y continuará.")
                    candidates = generar_todas_posibilidades()
                    break
            else:
                candidates = nuevos
                print(f"Candidatos restantes para la máquina: {len(candidates)}")
                break


if __name__ == "__main__":
    try:
        juego_consola()
    except SystemExit:
        pass
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")  










#programar solicitud de input de usuario 


#desarrollar registros de victorias y derrotas registradas



#almacenar el numero que el usuario digita para calcular el numero secreto 

#el numero entra a la secuencia de validacion para calcular si tiene fijas o picas 

#retorna una respuesta para ser vista por el usuario 


#MENU2 

#Generar un numero para que el usuari diga si tenemos una pica o una fija




# descubrimos el numero al oponente

#registro de cuantos disparos se elaboraron para elaborar 






#la gracia es que todo este algoritmo este conectado entre si para que me adivine mi numero y yo le adivino el de el pero todo en un mismo esenario hasta que el primero gane 