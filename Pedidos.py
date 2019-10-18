#! /usr/bin/env python3
from datetime import datetime
from contacto import Contacto
from clientes import Clientes
from pedido import Pedido
from estados import Estados

class Pedidos:
    ''' Almacena cada pedido de trabajo'''

    def __init__(self): 
        self.pedidos=[]
        self.estados=()
    def nuevo_pedido(self, id_cliente, descripcion, etiquetas=' ', fecha_prev=' ',
                 precio=' ',pagado=' '):    
        obj=Pedido(id_cliente, descripcion, etiquetas, fecha_prev,precio,pagado)
        
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
    def entregar_pedido(self,id_pedido):
        pedido=self.buscar_por_id(id_pedido)
        if pedido:
            pedido.id_estado= 'Entregado'
            pedido.fecha_entrega=datetime.today()
            return pedido
        else:
            return 'Nose encontro pedido'
    def modificar_pedido(self,id_pedido, descripcion=' ', precio=' ',etiquetas='', pagado=''):
        pedido=self.buscar_por_id(id_pedido)
            
        if pedido:
            if descripcion:
                pedido.descripcion=descripcion
            if precio:
                pedido.precio=precio
            if etiquetas:
                pedido.etiquetas=etiquetas
            if pagado:
                pedido.pagado=pagado
        else:
            return 'pedido no encontrado'
