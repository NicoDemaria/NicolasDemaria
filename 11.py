'''11.	Definir una función superposicion() que tome cadenas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. '''




def superposicion(word, word2):
    for caracter1 in word:
        print(caracter1)
        for caracter2 in word2:
            print(caracter2)
            if caracter1 == caracter2:
                return True
    return False


print(superposicion('abc','123'))