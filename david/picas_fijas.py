import random
import secrets

# Lo que se tiene que tener de cuenta es realizar el juego ademas establecer que tambien deve hacer la inversa del algoritmo osea que el cliente piensa un numero y la maquina se lo descubre 




#MENU 1
#almacenar el numero secreto por el sistema (el usuario no lo ve)


def generarNumeroSecreto(allow_leadign_zero=False)->str:
    digitos =list('0123456789')
    if allow_leadign_zero:
        seleccion = secrets.SystemRandom().sample(digitos, 4)
    else:
        primero = secrets.choice(digitos[1:])
        restante= secrets.SystemRandom(.sample([d for d in digitos if d != primero], 3))
        seleccion = [primero] + restante
    return ''.join(seleccion)










#programar solicitud de input de usuario 
numeroCliente= input("Digite un numero de 4 digitos para iniciar el juego: ")

#desarrollar registros de victorias y derrotas registradas



#almacenar el numero que el usuario digita para calcular el numero secreto 

#el numero entra a la secuencia de validacion para calcular si tiene fijas o picas 

#retorna una respuesta para ser vista por el usuario 


#MENU2 

#Generar un numero para que el usuari diga si tenemos una pica o una fija


# Validacion de cuantas picas y fijas tenemos

# descubrimos el numero al oponente

#registro de cuantos disparos se elaboraron para elaborar 






#la gracia es que todo este algoritmo este conectado entre si para que me adivine mi numero y yo le adivino el de el pero todo en un mismo esenario hasta que el primero gane 