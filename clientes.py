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

    def eliminar_cliente(self,id_cliente):
        cliente= self.buscar_cliente(id_cliente)
        if cliente :
            self.clientes.remove(cliente)
                
        else:
            return "cliente no encontrado"
            
    def buscar_cliente_por_id(self,id_cliente):
        ''' busca el cliente con el id dado y lo retorna'''
        for cliente in self.clientes:
            if str(cliente.id) == str(id_cliente):
                return cliente
            else:
                return False
    def buscar_cliente(self,filtro):
        '''recibe un filtro y hace la busqueda sobre nombre'''
        lista=[]
        for cliente in self.clientes:
            if str(cliente.nombre)== str(filtro):
                lista.append(cliente)
        return lista
    

    
