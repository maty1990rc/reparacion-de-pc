#! /usr/bin/env python3
import datetime
from contacto import Contacto
from clientes import Clientes
import tkinter
from tkinter import ttk
from tkinter import messagebox
from Pedidos import Pedidos
from pedido import Pedido
from estados import Estados

class Gui:
    '''interface grafica del sistema'''

    
    def __init__(self):
        '''inicializa la ventana principal del programa'''
        self.raiz_sistema=tkinter.Tk()
        self.raiz_sistema.title("Reparacion de PC")
        self.clientes=Clientes()
        self.pedidos=Pedidos()
        self.estados=Estados()

        botonAgregar_pedido=tkinter.Button(self.raiz_sistema,text="Ingresar pedido",
                    command = self.agregar_pedido).grid(row=0, column=0)
        botonclientes=tkinter.Button(self.raiz_sistema,text="Clientes",
                    command = self.contactos).grid(row=0, column=5)
        botonpedidos_avencer=tkinter.Button(self.raiz_sistema,text="Pedidos por  vencer",
                    command = self.pedidos_proximos).grid(row=0, column=3)
        botonpedidos_vencidos=tkinter.Button(self.raiz_sistema,text="Pedidos vencidos",
                    command = self.vencidos).grid(row=1, column=3)
        
        botoncerrar_pedido=tkinter.Button(self.raiz_sistema,text="Etregar pedido",
                    command = self.cerrar_pedido).grid(row=0, column=1)
        tkinter.Label(self.raiz_sistema,text="Buscar pedido").grid(row=1,column=0)
        self.cajaBuscar_pedido = tkinter.Entry(self.raiz_sistema)
        self.cajaBuscar_pedido.grid(row=1, column=1)
        botonBuscar_pedido = tkinter.Button(self.raiz_sistema, text="Buscar",
                    command = self.buscar_pedido).grid(row=1, column=2)

        self.treeview = ttk.Treeview(self.raiz_sistema, 
                    columns=("descripcion","etiquetas","fecha_prev","precio","pagado"))
        self.treeview.heading("#0",text="id")
        self.treeview.column("#0",minwidth=0, width=40)
        self.treeview.heading("descripcion",text="Descripcion")
        self.treeview.heading("etiquetas",text="Etiquetas")
        self.treeview.heading("fecha_prev",text="Fecha Prevista")
        self.treeview.heading("precio",text="Precio")
        self.treeview.heading("pagado",text="Estada de pago")
        self.treeview.grid(row=2, columnspan=6)
        botonSalir = tkinter.Button(self.raiz_sistema, text = "Salir",
                    command = self.raiz_sistema.destroy)
        botonSalir.grid(row=3, column=1)
        
    def agregar_pedido(self):
        '''ventana para ingresar datos de pedido'''
        self.raiz_nuevopedido=tkinter.Toplevel()
        self.raiz_nuevopedido.title("agregar pedido")
        self.raiz_nuevopedido.geometry("400x250+0+0")

        self.caja_descripcion=tkinter.Entry(self.raiz_nuevopedido)
        self.caja_descripcion.grid(row=0,column=1)
        self.caja_etiquetas=tkinter.Entry(self.raiz_nuevopedido)
        self.caja_etiquetas.grid(row=1,column=1)
        self.caja_fecha_prev=tkinter.Entry(self.raiz_nuevopedido)
        self.caja_fecha_prev.grid(row=2,column=1)
        self.caja_precio=tkinter.Entry(self.raiz_nuevopedido)
        self.caja_precio.grid(row=3,column=1)
        self.caja_pagado=tkinter.Entry(self.raiz_nuevopedido)
        self.caja_pagado.grid(row=4,column=1)
        self.caja_idcliente=tkinter.Entry(self.raiz_nuevopedido)
        self.caja_idcliente.grid(row=6,column=1)

        tkinter.Label(self.raiz_nuevopedido,text="Descripcion").grid(row=0,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Etiquetas").grid(row=1,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Fecha previstas").grid(row=2,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Precio").grid(row=3,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Pagado").grid(row=4,column=0)

        boton_salir=tkinter.Button(self.raiz_nuevopedido,text="Salir",
                                   command= self.raiz_nuevopedido.destroy).grid(row=5,column=1)
        boton_guardar=tkinter.Button(self.raiz_nuevopedido,text="Guardar",
                                   command= self.guardar_pedido).grid(row=5,column=0)
        boton_clientes=tkinter.Button(self.raiz_nuevopedido,text="Cliente",
                                   command= self.insertar_cliente).grid(row=5,column=2)
        
        self.raiz_nuevopedido.grab_set()
        self.raiz_sistema.wait_window(self.raiz_nuevopedido)


       
        
    
    def cerrar_pedido(self):
        '''marca el pedido como entregado y lo muestra'''
        i = self.treeview.selection()
        id = self.treeview.item(i)['text']
        print (id)
        clt=self.pedidos.entregar_pedido(id)

         # Vaciar el treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)
            
        self.treeview.insert("",tkinter.END, text=clt.id_pedido,
                values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.id_estado, clt.pagado ))
        


    def buscar_pedido(self):
        '''captura el contenido de la caja buscar y se la envia a pedido-buscar peddido,busca en descripcion y etiquetas'''
        filtro=self.cajaBuscar_pedido.get()
        resultado=self.pedidos.buscar_pedido(filtro)

         # Vaciar el treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for clt in resultado:    
            self.treeview.insert("",tkinter.END, text=clt.id_pedido,
                    values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.id_estado, clt.pagado ))
        
            

    def guardar_pedido(self):
        '''guarda los datos ingresados en la ventana de nuevo pedido'''
        clt= self.pedidos.nuevo_pedido(self.caja_idcliente.get(),self.caja_descripcion.get(), self.caja_etiquetas.get(), self.caja_fecha_prev.get(), self.caja_precio.get(), self.caja_pagado.get())
        self.raiz_nuevopedido.destroy()


        

        self.treeview.insert("",tkinter.END, text=clt.id_pedido,
                values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.precio, clt.pagado ))




    def insertar_cliente(self):
        '''ventana para seleccionar el cliente del nuevo pedido'''
        self.raiz_ac = tkinter.Toplevel()
        self.raiz_ac.title("Insertar Cliente")

        botonAgregar_cliente=tkinter.Button(self.raiz_ac,text="Nuevo cliente",
                    command = self.insertrar_nuevo_cliente).grid(row=0, column=0)
        botonInsertar_cliente=tkinter.Button(self.raiz_ac,text="Cargar cliente",
                    command = self.insertar_cliente_pedido).grid(row=0, column=3)
       
        tkinter.Label(self.raiz_ac,text="Buscar cliente").grid(row=1,column=0)
        self.cajaBuscar = tkinter.Entry(self.raiz_ac)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.raiz_ac, text="Buscar",
                    command = self.buscar_en_insert).grid(row=1, column=2)

        self.treeview2 = ttk.Treeview(self.raiz_ac, 
                    columns=("nombre","apellido","domicilio","telefono","mail"))
        self.treeview2.heading("#0",text="id")
        self.treeview2.column("#0",minwidth=0, width=40)
        self.treeview2.heading("nombre",text="Nombre")
        self.treeview2.heading("apellido",text="Apellido")
        self.treeview2.heading("domicilio",text="Domicilio")
        self.treeview2.heading("telefono",text="Telefono")
        self.treeview2.heading("mail",text="E-Mail")
        self.treeview2.grid(row=2, columnspan=6)
        botonSalir = tkinter.Button(self.raiz_ac, text = "Salir",
                    command = self.raiz_ac.destroy)
        botonSalir.grid(row=3, column=1)



        self.raiz_ac.grab_set()
        self.raiz_nuevopedido.wait_window(self.raiz_ac)
        pass

    def insertar_nuevo_cliente(self):
        '''permite ingresar un nuevo cliente en la etapa de seleccionar cliente del pedido'''
        self.raiz_insertrar_nuevo_cliente=tkinter.Toplevel()
        self.raiz_insertrar_nuevo_cliente.title("Nuevo cliente")
        self.raiz_insertrar_nuevo_cliente.geometry("400x250+0+0")
        
        self.caja_nombre=tkinter.Entry(self.raiz_insertrar_nuevo_cliente)
        self.caja_nombre.grid(row=0,column=1)
        self.caja_apellido=tkinter.Entry(self.raiz_insertrar_nuevo_cliente)
        self.caja_apellido.grid(row=1,column=1)
        self.caja_domicilio=tkinter.Entry(self.raiz_insertrar_nuevo_cliente)
        self.caja_domicilio.grid(row=2,column=1)
        self.caja_telefono=tkinter.Entry(self.raiz_insertrar_nuevo_cliente)
        self.caja_telefono.grid(row=3,column=1)
        self.caja_mail=tkinter.Entry(self.raiz_insertrar_nuevo_cliente)
        self.caja_mail.grid(row=4,column=1)

        

        tkinter.Label(self.raiz_insertrar_nuevo_cliente,text="Nombre").grid(row=0,column=0)
        tkinter.Label(self.raiz_insertrar_nuevo_cliente,text="Apellido").grid(row=1,column=0)
        tkinter.Label(self.raiz_insertrar_nuevo_cliente,text="domicilio").grid(row=2,column=0)
        tkinter.Label(self.raiz_insertrar_nuevo_cliente,text="Telefono").grid(row=3,column=0)
        tkinter.Label(self.raiz_insertrar_nuevo_cliente,text="E-mail").grid(row=4,column=0)

        boton_guardar=tkinter.Button(self.raiz_insertrar_nuevo_cliente,text="Guardar",
                    command = self.guardar_nuevocliente_insertado).grid(row=5, column=0)
        boton_salir=tkinter.Button(self.raiz_insertrar_nuevo_cliente,text="salir",
                    command = self.raiz_insertrar_nuevo_cliente.destroy).grid(row=5, column=1)

        

        self.raiz_insertrar_nuevo_cliente.grab_set()
        self.raiz_ac.wait_window(self.raiz_insertrar_nuevo_cliente)


        
    def guardar_nuevocliente_insertado(self):
        ''' guarda los datos del nuevo cliente'''
        
        clt= self.clientes.agregar_cliente(self.caja_nombre.get(), self.caja_apellido.get(), self.caja_domicilio.get(), self.caja_telefono.get(), self.caja_mail.get())
        self.raiz_insertrar_nuevo_cliente.destroy()


         # Vaciar el treeview
        for i in self.treeview2.get_children():
            self.treeview2.delete(i)
            
        self.treeview2.insert("",tkinter.END, text=clt.id,
                values=(clt.nombre, clt.apellido, clt.domicilio, clt.telefono, clt.mail ))

