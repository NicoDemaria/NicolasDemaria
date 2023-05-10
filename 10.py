'''10.	Definir una función que calcule la longitud de una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.'''


def long(car):
    contador = 0
    for i in car:
        contador += 1
    return contador
        
    
    
    

print(long('hola'))