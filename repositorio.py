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


    def guardar_cliente(self, contacto):
        '''Guarda el clontacto en la BD'''
        consulta = "INSERT INTO clientes (nombre, apellido, domicilio, telefono, mail) VALUES (?, ?, ?, ?, ?);"
        resultado = self.cursor.execute(consulta, [contacto.nombre, contacto.apellido, contacto.domicilio ,contacto.telefono ,contacto.mail])
        id_cliente = resultado.lastrowid
        self.bd.commit()
        return int(id_cliente)
        

    def actualizar(self, contacto):
        '''Actualiza el contacto en la BD'''
        consulta = "UPDATE clientes SET nombre = ?, apellido = ?,domicilio = ?,telefono = ?,mail = ? WHERE id = ?;"
        self.cursor.execute(consulta, [contacto.nombre, contacto.apellido, contacto.domicilio ,contacto.telefono ,contacto.mail,contacto.id])
        self.bd.commit()

    def eliminar(self, contacto):
        '''Elimina el cliente de la BD'''
        consulta = "DELETE FROM clientes WHERE id = ?;"
        self.cursor.execute(consulta, [contacto.id])
        self.bd.commit()
    def get_all_pedidos(self):
        ''' Retorna una lista de objetos Pedidos con todas los pedidos que haya
        guardadas en la BD'''
        lista_pedidos= []
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
