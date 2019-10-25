#! /usr/bin/env python3
import sqlite3
from contacto import Contacto


class Repositorio:
    '''Consulta y guarda notas en la BD'''
    
    def __init__(self):
        self.bd = sqlite3.connect("base.db")
        self.cursor = self.bd.cursor()

    def get_all_clientes(self):
        ''' Retorna una lista de objetos Pedidos con todas los pedidos que haya
        guardadas en la BD'''
        lista_clientes = []
        consulta = "SELECT id, nombre, apellido,domicilio, telefono, mail FROM clientes;"
        try:
            self.cursor.execute(consulta)
            todos_los_clientes = self.cursor.fetchall()
            for id, nombre, apellido, domicilio, telefono, mail in todos_los_clientes:
                lista_clientes.append(Contacto(nombre,apellido,domicilio,telefono,mail,id))
            return lista_clientes                  
        except:
            print("Error al conectarse")
            raise Exception("Conexión errónea")

