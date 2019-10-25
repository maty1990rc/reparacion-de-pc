#! /usr/bin/env python3
from datetime import datetime
from contacto import Contacto
from clientes import Clientes


ultimoid=0
class Pedido:
    '''genera el pedido contodos sus campos'''
    def __init__(self, id_cliente, descripcion, etiquetas=' ', fecha_prev=' ', precio=' ',pagado=' ',fecha_entrega=' ',id_estado=' '):
        self.descripcion=descripcion
        self.etiquetas=etiquetas
        self.fecha_recep=datetime.today()
        self.fecha_prev=fecha_prev
        self.fecha_entrega=fecha_entrega
        self.id_estado=id_estado
        self.id_cliente=id_cliente
        self.precio=precio
        self.pagado=pagado
        global ultimoid
        ultimoid=ultimoid+1
        self.id_pedido=ultimoid
              
