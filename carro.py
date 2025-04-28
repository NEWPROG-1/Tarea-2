

# Pedir al usuario los datos para hallar el area lateral del carro

# datos primer rectangulo

b1 = int(input("Ingrese la base del primer rectangulo: ")) 

a1 = int(input("Ingrese la altura del primer rectangulo: "))

# datos segundo rectangulo

b2 = int(input("Ingrese la base del segundo rectangulo: "))

a2 = int(input("Ingrese la altura del segundo rectangulo: "))

# datos primera circunferencia 

r1 = float(input("Ingrese el radio de la primera circunferencia: "))

# datos segunda circunferencia

r2 = float(input("Ingrese el radio de la segunda circunferencia: "))

# importar funciones de vagon

from vagon import(area_cir,area_rect)

# imprimir area lateral del carro

print("El area lateral del carro es:", area_rect(b1,a1) + area_rect(b2,a2) + area_cir(r1) + area_cir(r2) )

# fin
