'''

2.	Definir una función resta() que tome como argumento dos números diferentes y devuelva el resultado de la resta del mayor de ellos menos el menor.
'''


def resta(a, b):
    if a > b:
        return a - b
    else:
        return b - a