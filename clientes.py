#! /usr/bin/env python3
import datetime
from contacto import Contacto


class Clientes:
    '''Contiene una lista de clientes self.clientes, permite agregar o quitar'''
    def __init__(self):
        '''crea una lisata de clientes '''
        self.clientes=[]

    def agregar_cliente(self,nombre,apellido,domicilio,telefono,mail):
        '''guarda un cliente nuevo'''
        cliente = Contacto(nombre,apellido,domicilio,telefono,mail)
        self.clientes.append(cliente)
        return cliente

    