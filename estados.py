#! /usr/bin/env python3
from datetime import datetime,timedelta
from contacto import Contacto
from clientes import Clientes
from pedido import Pedido
from Pedidos import Pedidos
class Estados():
    def __init__(self):
        self.estados=["Recibido","Presupuestado","Reparado","Entregado","Demorado"]
    def pedidos_por_vencer(self,pedidos):
            '''recibe un número "n" como parámetro, y retorna una lista de
                los contactos que cumplen años en los próximos "n" días.'''
            lista=[]
            contador=0
            formato=("%d/%m/%Y")
            n=int(5)
            fecha_busqueda=datetime.today()
            while contador < n:
                contador +=1   
                for xx in pedidos:
                    x=xx.fecha_prev
                    x=datetime.strptime(xx.fecha_prev,formato)
                    resultado=x-fecha_busqueda
                    print(x)
                    print(resultado)
                    if (int(resultado.days) < 5) and (int(resultado.days) > 0):
                        lista.append(xx)
                    pedidos.remove(xx)
                fecha_busqueda = fecha_busqueda + timedelta(days=1)
                print(fecha_busqueda)
                
            return lista
    def pedidos_vencidos(self,pedidos):
            lista=[]
            contador=0
            formato=("%d/%m/%Y")
            n=int(5)
            fecha_busqueda=datetime.today()
            
            for xx in pedidos:
                x=xx.fecha_prev
                x=datetime.strptime(x,formato)
                print(x)
                resultado=x-fecha_busqueda
                if int(resultado.days)<0:
                    lista.append(xx)
                pedidos.remove(xx)
            return lista    
                
                
        
        
                #for x in self.contactos:
                 #   if x.nacimiento.month == fecha_busqueda.month:
                  #      if x.nacimiento.day == fecha_busqueda.day:
                   #         lista.append(x)
                #nacimiento=fecha_busqueda
        
                #formato=("%d,%m,%Y")
                #nacimiento=datetime.strptime(nacimiento,formato)
                #self.nacimiento=nacimiento
