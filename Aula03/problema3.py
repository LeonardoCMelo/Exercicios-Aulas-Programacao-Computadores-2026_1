def verifica_triangulo(x,y,z):
    return z < (x + y) and y < (x + z) and x < (y + z)

def tipo_triangulo(a,b,c):
    if a == b and a == c:
        return "Equilátero"
    elif a==b or a==c or b==c:
        return "Isósceles"
    else:
        return "Escaleno"
