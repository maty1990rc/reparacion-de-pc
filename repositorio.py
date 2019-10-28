#! /usr/bin/env python3
import sqlite3
from contacto import Contacto
from pedido import Pedido


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
        consulta = "SELECT id, descripcion, etiquetas, fecharecepcion, fechaprevista, fechaentrega, estado, precio, pagado, idcliente FROM pedidos;"
        try:
            self.cursor.execute(consulta)
            todos_los_pedidos = self.cursor.fetchall()
            for id, descripcion, etiquetas, fecharecepcion,fechaprevista, fechaentrega ,estado ,precio,pagado,idcliente in todos_los_pedidos:
                lista_pedidos.append(Pedido(idcliente, descripcion, etiquetas, fechaprevista, precio,pagado,fechaentrega,estado,id))
            return lista_pedidos                  
        except:
            print("Error al conectarse")
            raise Exception("Conexión errónea")
    def guardar_pedido(self, pedido):
        '''Guarda el clontacto en la BD'''
        consulta = "INSERT INTO pedidos (descripcion, etiquetas, fecharecepcion, fechaprevista, fechaentrega, estado, precio, pagado, idcliente) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
        resultado = self.cursor.execute(consulta, [pedido.descripcion,pedido.etiquetas,pedido.fecha_recep,pedido.fecha_prev,pedido.fecha_entrega,pedido.id_estado,pedido.precio,pedido.pagado,pedido.id_cliente])
        id_pedido = resultado.lastrowid
        self.bd.commit()
        return int(id_pedido)
    def actualizar_pedido(self, pedido):
        '''Actualiza el pedido en la BD'''
        consulta = "UPDATE pedidos SET descripcion = ?, precio = ?,etiquetas = ?,pagado = ?,estado= ? WHERE id = ?;"
        self.cursor.execute(consulta, [pedido.descripcion, pedido.precio, pedido.etiquetas ,pedido.pagado,pedido.id_estado ,pedido.id_pedido])
        self.bd.commit()
    def eliminar_pedido_bd(self, pedido):
        '''Elimina el pedido de la BD'''
        consulta = "DELETE FROM pedidos WHERE id = ?;"
        self.cursor.execute(consulta, [pedido.id_pedido])
        self.bd.commit()
