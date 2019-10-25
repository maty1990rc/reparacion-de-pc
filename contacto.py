#! /usr/bin/env python3
import datetime

ultimo_id=1

class Contacto:
    '''Contiene una lista de clientes self.clientes, permite agregar o quitar'''
    def __init__(self,nombre,apellido,domicilio,telefono,mail,id=None):
        '''crea un objeto contacto '''
        
        
        self.nombre=nombre
        self.apellido=apellido
        self.domicilio=domicilio
        self.telefono=telefono
        self.mail=mail
        global ultimo_id
        self.id = id
        ultimo_id+= 1
    

    def buscar(self,id):
        
        pass
    
