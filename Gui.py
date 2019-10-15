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




