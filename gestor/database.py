import os
import platform
import re

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

class Clientes:
    lista = []

    @classmethod
    def crear(cls, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        cls.lista.append(cliente)
        return cliente

    @classmethod
    def buscar(cls, dni):
        for cliente in cls.lista:
            if cliente.dni == dni:
                return cliente
        return None

    @classmethod
    def modificar(cls, dni, nombre, apellido):
        cliente = cls.buscar(dni)
        if cliente:
            cliente.nombre = nombre
            cliente.apellido = apellido
        return cliente

    @classmethod
    def borrar(cls, dni):
        cliente = cls.buscar(dni)
        if cliente:
            cls.lista.remove(cliente)
        return cliente