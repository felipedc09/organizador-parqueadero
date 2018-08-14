#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Estudiantes
#
# Created:     14/08/2018
# Copyright:   (c) Estudiantes 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------i
from cola import Cola
from entidades import Estudiante, Moto, Horario

def main():
    cupos = 4
    parqueaderos = Cola()

    horarios = [
        Horario(1, 6, 13),
        Horario(2, 6, 15),
        Horario(3, 8, 12),
        Horario(4, 9, 16)
    ]
    motos =[
        Moto("EPF123", "verde", 3),
        Moto("EXF123", "azul", 3),
        Moto("EPQ123", "negra", 3),
        Moto("QEF123", "blanca", 3),
        Moto("LHJ123", "rosada", 3),
        Moto("POI123", "gris", 3)
    ]
    estudiantes = [
        Estudiante(20112020005, "Felipe Duitama", 1, 1),
        Estudiante(20112020005, "Felipe Duitama", 2, 2),
        Estudiante(20112020005, "Felipe Duitama", 3, 3),
        Estudiante(20112020005, "Felipe Duitama", 4, 4),
        Estudiante(20112020005, "Felipe Duitama", 1, 5),
        ]
    for i in estudiantes:
         print(parqueaderos.items.count)
##        if parqueaderos.items.count < cupos:
##            parqueaderos.encolar(i)

    print(parqueaderos.items)

if __name__ == '__main__':
    main()
