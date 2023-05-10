'''

9.	Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
'''


def es_palindromo(car):
    car = car.lower()
    invertida = ''
    for item in reversed(car):
        invertida += item

    if invertida == car:
        return True
    else:
        return False
    
    
print(es_palindromo('radaR') )