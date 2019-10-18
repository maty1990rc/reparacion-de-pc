#! /usr/bin/env python3
from datetime import datetime
from contacto import Contacto
from clientes import Clientes


ultimoid=0
class Pedido:
    '''genera el pedido contodos sus campos'''
    def __init__(self, id_cliente, descripcion, etiquetas=' ', fecha_prev=' ',precio=' ',pagado=' '):
        self.descripcion=descripcion
        self.etiquetas=etiquetas
        self.fecha_recep=datetime.today()
        self.fecha_prev=fecha_prev
        self.fecha_entrega=0
        self.id_estado=0
        self.id_cliente=id_cliente
        self.precio=precio
        self.pagado=pagado
        global ultimoid
        ultimoid=ultimoid+1
        self.id_pedido=ultimoid
              
