#! /usr/bin/env python3
from datetime import datetime


class Pedido:
    '''genera el pedido contodos sus campos'''
    def __init__(self, id_cliente, descripcion, etiquetas=' ', fecha_prev=' ', precio=' ',pagado=' ',fecha_entrega=' ',id_estado=' ',id_pedido=None):
        self.descripcion=descripcion
        self.etiquetas=etiquetas
        self.fecha_recep=datetime.today()
        self.fecha_prev=fecha_prev
        self.fecha_entrega=fecha_entrega
        self.id_estado=id_estado
        self.id_cliente=id_cliente
        self.precio=precio
        self.pagado=pagado
        self.id_pedido=id_pedido
       

       
