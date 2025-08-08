#Vamos a importa la libreria ramdon para poder generar numeros aleatorios
import random
def jugar(): #Aqui definimos la funcion principal del juego

     #Ahora pondremos un mensaje inicial para el usuario
     print("Hola humano, voy a tratar de adivinar el numero que estas pensando.\n")
     print("Piensa en un numero entre 1 y 100 ¿Listo?.\n")
     #Esperaremos que el usuario de enter para empezar..
     input("Presione enter para empezar...")

     #Aqui vamos a declarar las variables
     a = 1               #Limite inferior del rango
     b = 100              #Limite superior del rango
     intento = 0         #contador de intentos
     respuesta = ""     #variable para almacenar respuestas
     numero = ""        #Variable para determinar si el numero es mayor o menor
    
      #Aqui vamos a iniciar un ciclo que se repetira hasta que el intento sea menor a 5
     while intento < 5:
        aleatorio = random.randint(a , b) #Esto genera un numero aleatorio para empezar el juego
        #Se mostrara el numero generado y se preguntara si es el correcto
        print("Estoy tratando de adivinar tu numero...\n")
        print("¿Tu numero es... ? " +str(aleatorio))
        respuesta = input (" Escribe V si acerte o escribe F si falle: ").strip().upper() 
        #.strip() elimina espacios al inicio y final del texto y .upper()convierte el texto en mayusculas
        #input pide al usuario que ingrese algo por teclado
        #Si la respuesta llega a ser verdadera "V", la computadora mostrara un mensaje de logro 
        if respuesta == "V":
            print("GANE!! Acerte tu numero,vuelve prontoo\n")
            intento = 5
        #Si la respuesta llega a ser falsa "F", la computadora preguntara si el numero es mayor o menor
        elif respuesta == "F":
            print("¿Tu numero es mayor (M) o menor (N) al que pense?")
            numero = input ("Escribe M para mayor o N para menor: ").strip().upper()
            if numero == "M":
                a = aleatorio + 1  #Ajustamos el minimo
            elif numero == "N":
                b = aleatorio + -1 #Ajustamos el maximo
            else:
                print("Entrada invalidad. Solo puedes escribir M o N. Este intento no cuenta")
                continue #Volvemos al inicio del bucle
        else:
            print("Entrada invalidad. Solo puedes escribir V o F. Este intento no cuenta")
            continue #Volvemos al inicio del bucle
        #Si ya se hicieron los 5 intentos y el jugador nunca mostro que acerto(V)
        #se mostrara un mensaje de derrota por medio de != "V" (respuesta distinta)
        if intento == 4 and respuesta != "V":
            print("GANASTE!!. No logre adivinar tu numero en 5 intentos")
            print("Pero no pasa nada.... ¿REVANCHA?")
        intento = intento + 1 #Solo sumaremos intentos si la respuesta es valida
#Esto ayuda a que el juego solo se ejecute si se abre el archivo directamente y no cuando se
#importa desde otro
if __name__ == "__main__":
     jugar()
