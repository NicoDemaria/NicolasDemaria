'''
6.	Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 
'''


def max_de_tres(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b 
    else:
        return c
    
print(max_de_tres(0,0,0))