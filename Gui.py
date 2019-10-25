#! /usr/bin/env python3
import datetime
from contacto import Contacto
from clientes import Clientes
import tkinter
from tkinter import ttk
from tkinter import messagebox
from Pedidos import Pedidos
from pedido import Pedido


class Gui:
    '''interface grafica del sistema'''

    
    def __init__(self):
        '''inicializa la ventana principal del programa'''
        self.raiz_sistema=tkinter.Tk()
        self.raiz_sistema.title("Reparacion de PC")
        self.raiz_sistema.config(bg="ivory4",bd=2)
        self.clientes=Clientes()
        self.pedidos=Pedidos()
        

        botonAgregar_pedido=tkinter.Button(self.raiz_sistema,text="Ingresar pedido",
                    command = self.agregar_pedido).grid(row=0, column=0)
        botonclientes=tkinter.Button(self.raiz_sistema,text="Clientes",
                    command = self.contactos,bg="grey").grid(row=0, column=5)
        botonpedidos_avencer=tkinter.Button(self.raiz_sistema,text="Pedidos por  vencer",
                    command = self.pedidos_proximos,bg="grey").grid(row=0, column=3)
        botonpedidos_vencidos=tkinter.Button(self.raiz_sistema,text="Pedidos vencidos",
                    command = self.vencidos,bg="grey").grid(row=1, column=3)
        
        botoncerrar_pedido=tkinter.Button(self.raiz_sistema,text="Etregar pedido",
                    command = self.cerrar_pedido,bg="grey").grid(row=0, column=1)
        tkinter.Label(self.raiz_sistema,text="Buscar pedido",bg="ivory4").grid(row=1,column=0)
        self.cajaBuscar_pedido = tkinter.Entry(self.raiz_sistema)
        self.cajaBuscar_pedido.grid(row=1, column=1)
        botonBuscar_pedido = tkinter.Button(self.raiz_sistema, text="Buscar",
                    command = self.buscar_pedido,bg="grey").grid(row=1, column=2)
        botonModificar_pedido = tkinter.Button(self.raiz_sistema, text="Modificar",
                    command = self.modificar_pedido,bg="grey").grid(row=0, column=2)

        
        self.treeview = ttk.Treeview(self.raiz_sistema, 
                    columns=("descripcion","etiquetas","fecha_prev","precio","pagado","estado"))
        self.treeview.heading("#0",text="id")
        self.treeview.column("#0",minwidth=0, width=40)
        self.treeview.heading("descripcion",text="Descripcion")
        self.treeview.heading("etiquetas",text="Etiquetas")
        self.treeview.heading("fecha_prev",text="Fecha Prevista")
        self.treeview.heading("precio",text="Precio")
        self.treeview.heading("pagado",text="Pagado")
        self.treeview.heading("estado",text="Estado")
        
        self.treeview.grid(row=2, columnspan=6)
        botonSalir = tkinter.Button(self.raiz_sistema, text = "Salir",
                    command = self.raiz_sistema.destroy,bg="grey")
        botonSalir.grid(row=4, column=2)






    def agregar_pedido(self):
        '''ventana para ingresar datos de pedido'''
        self.raiz_nuevopedido=tkinter.Toplevel()
        self.raiz_nuevopedido.title("agregar pedido")
        self.raiz_nuevopedido.config(bg="green",bd=2)

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

        tkinter.Label(self.raiz_nuevopedido,text="Descripcion",bg="green").grid(row=0,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Etiquetas",bg="green").grid(row=1,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Fecha previstas",bg="green").grid(row=2,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Precio",bg="green").grid(row=3,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="Pagado",bg="green").grid(row=4,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="ID CLiente",bg="green").grid(row=6,column=0)
        tkinter.Label(self.raiz_nuevopedido,text="dd/mm/aaaa",bg="green").grid(row=2,column=2)
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
                values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.precio, clt.pagado, clt.id_estado ))
        


    def buscar_pedido(self):
        '''captura el contenido de la caja buscar y se la envia a pedido-buscar peddido,busca en descripcion y etiquetas'''
        filtro=self.cajaBuscar_pedido.get()
        resultado=self.pedidos.buscar_pedido(filtro)

         # Vaciar el treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for clt in resultado:    
            self.treeview.insert("",tkinter.END, text=clt.id_pedido,
                    values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.precio, clt.pagado, clt.id_estado  ))
        
            

    def guardar_pedido(self):
        '''guarda los datos ingresados en la ventana de nuevo pedido'''
        clt= self.pedidos.nuevo_pedido(self.caja_idcliente.get(),self.caja_descripcion.get(), self.caja_etiquetas.get(), self.caja_fecha_prev.get(), self.caja_precio.get(), self.caja_pagado.get())
        self.raiz_nuevopedido.destroy()


        

        self.treeview.insert("",tkinter.END, text=clt.id_pedido,
                values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.precio, clt.pagado, clt.id_estado  ))    


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

    def insertrar_nuevo_cliente(self):
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


    def insertar_cliente_pedido(self):
        '''carga los datos del cliente en el pedido mediante el id'''
        i = self.treeview2.selection()
        print(i)
        id = self.treeview2.item(i)['text']
        self.caja_idcliente.insert(0,id)
        self.raiz_ac.destroy()

    def buscar_en_insert(self):
        '''permite buscar clientes en la  seccion nuevo pedido-clientes'''
        resultado=self.clientes.buscar_cliente(self.cajaBuscar.get())

        if resultado:
             # Vaciar el treeview
            for i in self.treeview2.get_children():
                self.treeview2.delete(i)

            for cliente in resultado:
                 self.treeview2.insert("",tkinter.END, text=cliente.id,
                                      values=(cliente.nombre, cliente.apellido, cliente.domicilio, cliente.telefono, cliente.mail))       
        else:
            # Vaciar el treeview
            for i in self.treeview2.get_children():
                self.treeview2.delete(i)
            for cliente in self.clientes.clientes:
                 self.treeview2.insert("",tkinter.END, text=cliente.id,
                                      values=(cliente.nombre, cliente.apellido, cliente.domicilio, cliente.telefono, cliente.mail))

    
    def contactos(self):
        '''interface de adminstracion de clientes, permite agregar, eliminar,modificar,buscar'''

        self.raiz = tkinter.Toplevel()
        self.raiz.title("Clientes")

        botonAgregar_cliente=tkinter.Button(self.raiz,text="Nuevo cliente",
                    command = self.agregar_cliente).grid(row=0, column=0)
        botonModificar_cliente=tkinter.Button(self.raiz,text="Modificar cliente",
                    command = self.modificar_cliente).grid(row=0, column=1)
        botonEliminar=tkinter.Button(self.raiz,text="Eliminar",
                    command = self.eliminar_cliente).grid(row=0, column=2)
        tkinter.Label(self.raiz,text="Buscar cliente").grid(row=1,column=0)
        self.cajaBuscar = tkinter.Entry(self.raiz)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.raiz, text="Buscar",
                    command = self.buscar_cliente).grid(row=1, column=2)

        self.treeview3 = ttk.Treeview(self.raiz, 
                    columns=("nombre","apellido","domicilio","telefono","mail"))
        self.treeview3.heading("#0",text="id")
        self.treeview3.column("#0",minwidth=0, width=40)
        self.treeview3.heading("nombre",text="Nombre")
        self.treeview3.heading("apellido",text="Apellido")
        self.treeview3.heading("domicilio",text="Domicilio")
        self.treeview3.heading("telefono",text="Telefono")
        self.treeview3.heading("mail",text="E-Mail")
        self.treeview3.grid(row=2, columnspan=6)
        botonSalir = tkinter.Button(self.raiz, text = "Salir",
                    command = self.raiz.destroy)
        botonSalir.grid(row=3, column=1)



        self.raiz.grab_set()
        self.raiz_sistema.wait_window(self.raiz)
        pass
    def modificar_cliente(self):
        '''permite modificar los datos del cliente seleccionado en el treeview'''
        i = self.treeview3.selection()
        id = self.treeview3.item(i)['text']
        print(id)

        cliente=self.clientes.buscar_cliente_por_id(id)

        if cliente:
            self.dialogo_modificar=tkinter.Toplevel()
            self.dialogo_modificar.title("Modificar")

            self.caja_nombre=tkinter.Entry(self.dialogo_modificar)
            self.caja_nombre.grid(row=0,column=1)
            self.caja_nombre.insert(0,cliente.nombre)
            self.caja_apellido=tkinter.Entry(self.dialogo_modificar)
            self.caja_apellido.grid(row=1,column=1)
            self.caja_apellido.insert(0,cliente.apellido)
            self.caja_domicilio=tkinter.Entry(self.dialogo_modificar)
            self.caja_domicilio.grid(row=2,column=1)
            self.caja_domicilio.insert(0,cliente.domicilio)
            self.caja_telefono=tkinter.Entry(self.dialogo_modificar)
            self.caja_telefono.grid(row=3,column=1)
            self.caja_telefono.insert(0,cliente.telefono)
            self.caja_mail=tkinter.Entry(self.dialogo_modificar)
            self.caja_mail.grid(row=4,column=1)
            self.caja_mail.insert(0,cliente.mail)

            tkinter.Label(self.dialogo_modificar,text="Nombre").grid(row=0,column=0)
            tkinter.Label(self.dialogo_modificar,text="Apellido").grid(row=1,column=0)
            tkinter.Label(self.dialogo_modificar,text="domicilio").grid(row=2,column=0)
            tkinter.Label(self.dialogo_modificar,text="Telefono").grid(row=3,column=0)
            tkinter.Label(self.dialogo_modificar,text="E-mail").grid(row=4,column=0)

            boton_guardar=tkinter.Button(self.dialogo_modificar,text="Guardar",
                        command = self.modificar_ok).grid(row=5, column=0)
            boton_salir=tkinter.Button(self.dialogo_modificar,text="salir",
                        command = self.dialogo_modificar.destroy).grid(row=5, column=1)

            

            self.dialogo_modificar.grab_set()
            self.raiz.wait_window(self.dialogo_modificar)
        
        

            
        
        pass
    def modificar_ok(self):
        '''guarda las modificaciones hechas en el cliente'''
        i = self.treeview3.selection()
        id = self.treeview3.item(i)['text']
        
        clt=self.clientes.modificar_cliente(id, self.caja_nombre.get(), self.caja_apellido.get(), self.caja_domicilio.get(), self.caja_telefono.get(), self.caja_mail.get())
            

         # Vaciar el treeview
        for i in self.treeview3.get_children():
            self.treeview3.delete(i)
            
        self.treeview3.insert("",tkinter.END, text=clt.id,
                values=(clt.nombre, clt.apellido, clt.domicilio, clt.telefono, clt.mail ))
        self.dialogo_modificar.destroy()

    def eliminar_cliente(self):
        '''elimiena cliente seleccionado'''
        
        i = self.treeview3.selection()
        id = self.treeview3.item(i)['text']

        a=self.clientes.eliminar_cliente(id)

         # Vaciar el treeview
        for i in self.treeview3.get_children():
            self.treeview3.delete(i)
            
        messagebox.showwarning("ADMINISTRADOR DE CLIENTES","CLIENTE ELIMINADO")    
   
        pass
    def buscar_cliente(self):
        '''permite buscar cliente utilizando un filtro'''
        resultado=self.clientes.buscar_cliente(self.cajaBuscar.get())

        if resultado:
             # Vaciar el treeview
            for i in self.treeview3.get_children():
                self.treeview3.delete(i)

            for cliente in resultado:
                 self.treeview3.insert("",tkinter.END, text=cliente.id,
                                      values=(cliente.nombre, cliente.apellido, cliente.domicilio, cliente.telefono, cliente.mail))       
        else:
            # Vaciar el treeview
            for i in self.treeview3.get_children():
                self.treeview3.delete(i)
            for cliente in self.clientes.clientes:
                 self.treeview3.insert("",tkinter.END, text=cliente.id,
                                      values=(cliente.nombre, cliente.apellido, cliente.domicilio, cliente.telefono, cliente.mail)) 

 
    
    def agregar_cliente(self):
        '''formulario de ingreso de datos de cliente'''
        self.raiz_agregar=tkinter.Toplevel()
        self.raiz_agregar.title("Nuevo cliente")
        self.raiz_agregar.geometry("400x250+0+0")
        
        self.caja_nombre=tkinter.Entry(self.raiz_agregar)
        self.caja_nombre.grid(row=0,column=1)
        self.caja_apellido=tkinter.Entry(self.raiz_agregar)
        self.caja_apellido.grid(row=1,column=1)
        self.caja_domicilio=tkinter.Entry(self.raiz_agregar)
        self.caja_domicilio.grid(row=2,column=1)
        self.caja_telefono=tkinter.Entry(self.raiz_agregar)
        self.caja_telefono.grid(row=3,column=1)
        self.caja_mail=tkinter.Entry(self.raiz_agregar)
        self.caja_mail.grid(row=4,column=1)

        

        tkinter.Label(self.raiz_agregar,text="Nombre").grid(row=0,column=0)
        tkinter.Label(self.raiz_agregar,text="Apellido").grid(row=1,column=0)
        tkinter.Label(self.raiz_agregar,text="domicilio").grid(row=2,column=0)
        tkinter.Label(self.raiz_agregar,text="Telefono").grid(row=3,column=0)
        tkinter.Label(self.raiz_agregar,text="E-mail").grid(row=4,column=0)

        boton_guardar=tkinter.Button(self.raiz_agregar,text="Guardar",
                    command = self.nuevo_cliente).grid(row=5, column=0)
        boton_salir=tkinter.Button(self.raiz_agregar,text="salir",
                    command = self.raiz_agregar.destroy).grid(row=5, column=1)

        

        self.raiz_agregar.grab_set()
        self.raiz.wait_window(self.raiz_agregar)
        
        pass
    def nuevo_cliente(self):
        '''guarda los datos del nuevo cliente'''
        clt= self.clientes.agregar_cliente(self.caja_nombre.get(), self.caja_apellido.get(), self.caja_domicilio.get(), self.caja_telefono.get(), self.caja_mail.get())
        self.raiz_agregar.destroy()


         # Vaciar el treeview
        for i in self.treeview3.get_children():
            self.treeview3.delete(i)
            
        self.treeview3.insert("",tkinter.END, text=clt.id,
                values=(clt.nombre, clt.apellido, clt.domicilio, clt.telefono, clt.mail ))
        
        pass
    def pedidos_proximos(self):
        lista=self.pedidos.pedidos_por_vencer()

        # Vaciar el treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for clt in lista:
            self.treeview.insert("",tkinter.END, text=clt.id_pedido,
                    values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.precio, clt.pagado ))
            

    def vencidos(self):
        
        lista=self.pedidos.pedidos_vencidos() 

        # Vaciar el treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for clt in lista:
            self.treeview.insert("",tkinter.END, text=clt.id_pedido,
                    values=(clt.descripcion, clt.etiquetas, clt.fecha_prev, clt.precio, clt.pagado ))
    def modificar_pedido(self):
        
        '''permite modificar los datos del pedido seleccionado en el treeview'''
        i = self.treeview.selection()
        id = self.treeview.item(i)['text']

        pedido=self.pedidos.buscar_por_id(id)

        if pedido:
            self.root_modificar_pedido=tkinter.Toplevel()
            self.root_modificar_pedido.title("Modificar Pedido")

            self.caja_descripcion=tkinter.Entry(self.root_modificar_pedido)
            self.caja_descripcion.grid(row=0,column=1)
            self.caja_descripcion.insert(0,pedido.descripcion)
            self.caja_etiquetas=tkinter.Entry(self.root_modificar_pedido)
            self.caja_etiquetas.grid(row=1,column=1)
            self.caja_etiquetas.insert(0,pedido.etiquetas)
            self.caja_precio=tkinter.Entry(self.root_modificar_pedido)
            self.caja_precio.grid(row=2,column=1)
            self.caja_precio.insert(0,pedido.precio)
            self.caja_pagado=tkinter.Entry(self.root_modificar_pedido)
            self.caja_pagado.grid(row=3,column=1)
            self.caja_pagado.insert(0,pedido.pagado)
            

            tkinter.Label(self.root_modificar_pedido,text="Descripcion").grid(row=0,column=0)
            tkinter.Label(self.root_modificar_pedido,text="Etiquetas").grid(row=1,column=0)
            tkinter.Label(self.root_modificar_pedido,text="Precio").grid(row=2,column=0)
            tkinter.Label(self.root_modificar_pedido,text="Pagado").grid(row=3,column=0)
            

            boton_guardar=tkinter.Button(self.root_modificar_pedido,text="Guardar",
                        command = self.modificar_pedido_ok).grid(row=5, column=0)
            boton_salir=tkinter.Button(self.root_modificar_pedido,text="salir",
                        command = self.root_modificar_pedido.destroy).grid(row=5, column=1)

            

            self.root_modificar_pedido.grab_set()
            self.raiz_sistema.wait_window(self.root_modificar_pedido)
        
    def modificar_pedido_ok(self):
        i = self.treeview.selection()
        id = self.treeview.item(i)['text']
        print(id)

        clt=self.pedidos.modificar_pedido(id,self.caja_descripcion.get(),self.caja_precio.get(),self.caja_etiquetas.get(),self.caja_pagado.get())

         # Vaciar el treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)
    
        self.root_modificar_pedido.destroy()
        
       
       
            
if __name__ == "__main__":
    g = Gui()
      

