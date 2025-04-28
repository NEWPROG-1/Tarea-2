
#importar modulo math

import math

#crear funcion para hallar volumen de una esfera


def volumen_esfera(r):
        return (4/3) * math.pi * r**3

print("El Volumen de la esfera es",volumen_esfera(3))

#crear funcion para hallar volumen de un cono

def vol_cono(r):
        return (1/3)  * math.pi * r**2 * 9/2

print("El Volumen del cono es", vol_cono(4))

# fin