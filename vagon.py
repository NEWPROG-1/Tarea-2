


# pedir al usuario los datos necesarios para la funcion como: base, altura y radio


# uso de " if __name__ == "__main__" : " para evitar ejecutar todo el codigo al importar funciones

if __name__ == "__main__" :

    b = int(input("Ingrese la base del rectangulo: "))

    a = int(input("Ingrese la altura del rectangulo: "))

    r = float(input("Ingrese radio de la circunferencia: "))

# importar modulo math

import math

# definir funcion para hallar area del rectangulo 

def area_rect (b,a):
    return b * a

# definir funcion para hallar area de una circunferencia


def area_cir (r):
    return r**2 * math.pi

# imprimir la suma de las areas 

# uso de " if __name__ == "__main__" : " para evitar ejecutar todo el codigo al importar funciones
if __name__ == "__main__" :
    print ("El area lateral del vagon es:", area_cir(r) * 2 + area_rect(b,a)) 

# fin