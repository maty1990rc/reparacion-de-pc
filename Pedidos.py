#! /usr/bin/env python3
from datetime import datetime, timedelta
from contacto import Contacto
from clientes import Clientes
from pedido import Pedido
from repositorio import Repositorio

class Pedidos:
    ''' Almacena cada pedido de trabajo'''

    def __init__(self): 
        self.repositorio=Repositorio()
        self.pedidos=[]
        self.estados=["Recibido","Presupuestado","Reparado","Entregado","Pagado"]
        try:
            self.pedidos=self.repositorio.get_all_pedidos()    
        except Exception as mensaje:
            raise
    def nuevo_pedido(self, id_cliente, descripcion, etiquetas=' ', fecha_prev=' ', fecha_entrega=' ',
                 id_estado=' ',precio=' ',pagado=' '):    
        obj=Pedido(id_cliente, descripcion, etiquetas, fecha_prev, fecha_entrega,
                 id_estado,precio,pagado)
        ret=self.pegar_estado(obj)
        id=self.repositorio.guardar_pedido(ret)
        ret.id_pedido=id
        self.pedidos.append(ret)
        
        return ret
    def buscar_pedido(self,filtro):
        lista=[]
        for i in self.pedidos:
            if ( str(filtro) in str(i.descripcion)) or (str(i.etiquetas) == str(filtro)) or (str(i.id_pedido)==str(filtro)):
                lista.append(i)
        return lista        
        
    def buscar_por_id(self,id_pedido):
        for pedido in self.pedidos:
            if str(pedido.id_pedido)==str(id_pedido):
                return pedido
    def entregar_pedido(self,id_pedido):
        pedido=self.buscar_por_id(id_pedido)
        if pedido:
            pedido.id_estado=self.estados[3]
            pedido.fecha_entrega=datetime.today()
            self.repositorio.actualizar_pedido(pedido)
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
            self.pegar_estado(pedido)
            self.repositorio.actualizar_pedido(pedido)
        else:
            return 'pedido no encontrado'

    def pedidos_por_vencer(self):
            '''recibe un nÃºmero "n" como parÃ¡metro, y retorna una lista de
                los contactos que cumplen aÃ±os en los prÃ³ximos "n" dÃ­as.'''
            lista=[]
            pedidos=[]
            for y in self.pedidos:
                pedidos.append(y)
            contador=0
            formato=("%d/%m/%Y")
            n=int(5)
            fecha_busqueda=datetime.today()
            while contador < n:
                contador +=1   
                for xx in pedidos:
                    x=xx.fecha_prev
                    x=datetime.strptime(xx.fecha_prev,formato)
                    resultado=x-fecha_busqueda
                    print(x)
                    print(resultado)
                    if (int(resultado.days) < 5) and (int(resultado.days) > 0):
                        lista.append(xx)
                    pedidos.remove(xx)
                fecha_busqueda = fecha_busqueda + timedelta(days=1)
                print(fecha_busqueda)
                
            return lista
    def pedidos_vencidos(self):
            lista=[]
            pedidos=[]
            for y in self.pedidos:
                pedidos.append(y)
            contador=0
            formato=("%d/%m/%Y")
            n=int(5)
            fecha_busqueda=datetime.today()
            
            for xx in pedidos:
                x=xx.fecha_prev
                x=datetime.strptime(x,formato)
                print(x)
                resultado=x-fecha_busqueda
                if int(resultado.days)<0:
                    lista.append(xx)
                pedidos.remove(xx)
            return lista
    def pegar_estado(self,pedido):
        if pedido:
            pedido.id_estado=self.estados[0]
        if pedido.precio:   
            if int(pedido.precio) > 0:
                pedido.id_estado=self.estados[1]
        if pedido.precio == pedido.pagado:
            pedido.id_estado=self.estados[4]
        return pedido
    def eliminar_elpedido(self,id_pedido):
        pedido=self.buscar_por_id(id_pedido)
        if pedido:
            self.pedidos.remove(pedido)
            self.repositorio.eliminar_pedido_bd(pedido)
            
