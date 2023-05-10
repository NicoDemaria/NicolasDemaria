'''
8.	Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
'''


def inversa(car):
    invertida = ''
    for item in reversed(car):
        invertida += item


    return invertida



car = 'estoy probando'
print(inversa(car))


    
    
    