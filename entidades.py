# -*- coding: utf-8 -*-
class Estudiante:

    def __init__(self, codigo, nombre, horario, moto):
        self.codigo = codigo
        self.nombre = nombre
        self.horario = horario
        self.moto =  moto

    def solicitarTurno(self, x):
        pass

class Moto:

    def __init__(self, id, placa, color):
        self.id = id
        self.placa = placa
        self.color = color

    def solicitarTurno(self, x):
        pass

class Horario:

    def __init__(self, id, entrada, salida):
        self.id = id
        self.entrada = entrada
        self.salida = salida

    def solicitarTurno(self, x):
        pass

