#! /usr/bin/env python3
import datetime
from contacto import Contacto
from repositorio import Repositorio


class Clientes:
    '''Contiene una lista de clientes self.clientes, permite agregar o quitar'''
    def __init__(self):
        '''crea una lisata de clientes '''
        self.repositorio=Repositorio()
        self.clientes=[]
        try:
            self.clientes=self.repositorio.get_all_clientes()    
        except Exception as mensaje:
            raise
    def agregar_cliente(self,nombre,apellido,domicilio,telefono,mail):
        '''guarda un cliente nuevo'''
        cliente = Contacto(nombre,apellido,domicilio,telefono,mail)
        cliente.id=self.repositorio.guardar_cliente(cliente)
        self.clientes.append(cliente)
        print(cliente.id,cliente.nombre,cliente.mail)
        
        return cliente

    def eliminar_cliente(self,id_cliente):
        cliente= self.buscar_cliente_por_id(id_cliente)
        if cliente :
            self.clientes.remove(cliente)
            self.repositorio.eliminar(cliente)
                
        else:
            return "cliente no encontrado"
            
    def buscar_cliente_por_id(self,n_cliente):
        ''' busca el cliente con el id dado y lo retorna'''
        for contacto in self.clientes:
            if str(contacto.id) == str(n_cliente):
                return contacto
            
    def buscar_cliente(self,filtro):
        '''recibe un filtro y hace la busqueda sobre nombre'''
        lista=[]
        for cliente in self.clientes:
            print(cliente.id)
            if (str(cliente.nombre)== str(filtro)) or (str(cliente.apellido)== str(filtro)) or (str(cliente.mail)== str(filtro)):
                lista.append(cliente)
        return lista
    def modificar_cliente(self, id, nombre, apellido, domicilio, telefono, mail):
        cliente=self.buscar_cliente_por_id(id)
        print(id)
        if cliente:
            cliente.nombre=nombre
            cliente.apellido=apellido
            cliente.domicilio=domicilio
            cliente.telefono=telefono
            cliente.mail=mail
            self.repositorio.actualizar(cliente)
            return cliente
         
        
       
            
