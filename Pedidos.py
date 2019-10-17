#! /usr/bin/env python3
from datetime import datetime
from contacto import Contacto
from clientes import Clientes
from pedido import Pedido

class Pedidos:
    ''' Almacena cada pedido de trabajo'''

    def __init__(self): 
        self.pedidos=[]

    def nuevo_pedido(self, id_cliente, descripcion, etiquetas=' ', fecha_prev=' ', fecha_entrega=' ',
                 id_estado=' ',precio=' ',pagado=' '):    
        obj=Pedido(id_cliente, descripcion, etiquetas, fecha_prev, fecha_entrega,
                 id_estado,precio,pagado)
        self.pedidos.append(obj)
        return obj
    def buscar_pedido(self,filtro):
        lista=[]
        for i in self.pedidos:
            if str(i.descripcion) == str(filtro) or str(i.etiquetas) == str(filtro) or str(i.id_pedido)==str(filtro):
                lista.append(i)
        return lista        
        
    def buscar_por_id(self,id_pedido):
        for pedido in self.pedidos:
            if str(pedido.id_pedido)==str(id_pedido):
                return pedido
    def entregar_pedidos(self,id_pedido):
        obj=buscar_por_id(self,id_pedido)
        obj.fecha_entrega = date.today()
        obj.estado_id = 25 (aca iria el numero de estado que corresponda a entregado)
