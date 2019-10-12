#! /usr/bin/env python3
import datetime

ultimo_id=1

class Contacto:
    '''Contiene una lista de clientes self.clientes, permite agregar o quitar'''
    def __init__(self,nombre,apellido,domicilio,telefono,mail):
        '''crea un objeto contacto con todos los datos del contacto'''
        
        
        self.nombre=nombre
        self.apellido=apellido
        self.domicilio=domicilio
        self.telefono=telefono
        self.mail=mail
        global ultimo_id
        self.id = ultimo_id
        ultimo_id+= 1
    

    def buscar(self,id):
        
        pass
    
