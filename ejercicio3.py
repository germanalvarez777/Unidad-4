from tkinter import *
from tkinter import ttk, font, messagebox

from datetime import date, datetime
import requests
import re


class Aplicacion3(object):
    __ventana = None
    def __init__ (self):
        self.__ventana = Tk()
        self.__ventana.title('Cotizaciones Dólar')
        self.__ventana.resizable(0,0)
        #self.__ventana.geometry('255x195')
        self.__ventana.config(padx=5, pady=5)
        fuente = font.Font(font='Verdana 10')

        self.monedaL = ttk.Label (self.__ventana, text='Moneda:')
        self.monedaL.configure(foreground='green')

        self.compraL = ttk.Label (self.__ventana, text='Compra:')
        self.compraL.configure(foreground='green')
        
        self.ventaL = ttk.Label (self.__ventana, text='Venta:')
        self.ventaL.configure(foreground='green')


        self.monedaL.grid(column=0, row=0, sticky=W)
        self.compraL.grid(column=5, row=0, sticky=W)
        self.ventaL.grid(column=8, row=0, sticky=W)

        self.Bottonactualizar = ttk.Button(self.__ventana, text="Actualizar", padding=(5,5), command=self.decifrarValores)
        
        
        #mas adelante colocamos el boton al final del listado
        self.Bottonactualizar.grid(column=0, row=12)           #insertamos el actualizar al final de la fila
        
    
        self.__ventana.mainloop()

    def decifrarValores (self):
        indice = 0
        url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

        response = requests.get(url)
            
        response_json = response.json()                 #se obtiene una lista de diccionarios, con info de bancos


        for i in range(len(response_json)):                                 #Diccionario de cada fila de la lista
            
            if re.search ('Dolar', response_json[i]['casa']['nombre']):
                
                if re.match ('^[0-9]', response_json[i]['casa']['compra']):
                    if re.match ('^[0-9]', response_json[i]['casa']['venta']):
                        dolar = str(response_json[i]['casa']['nombre'])
                        #print("Dolar: {}".format(dolar))

                        compra = float (response_json[i]['casa']['compra'].replace(',', '.'))
                        compra = round (compra,2)
                        compra = str(compra)

                        venta = float (response_json[i]['casa']['venta'].replace(',', '.'))
                        venta = round (venta, 2)
                        venta = str(venta)

                        #print("Compra: {}, Venta: {}\n".format(compra, venta))
                        

                        self.dolar = ttk.Label(self.__ventana, text= dolar)
                        self.compra = ttk.Label (self.__ventana, text= compra)
                        self.venta = ttk.Label (self.__ventana, text= venta)


                        #definimos las posiciones
                        self.dolar.grid(row = i+1, column=0, columnspan=2)
                        self.compra.grid (row = i+1, column=5, columnspan=2)
                        self.venta.grid (row = i+1, column=8, columnspan=2)

                        #para actualizarse cada vez que presionemos el boton, lo colocamos aqui
                        self.textoFecha = ttk.Label(self.__ventana, text= self.obtenerHora())
        
        #Para colocar la posicion del boton actualizar
        longitud = len(response_json)
        self.textoFecha.grid(column=4, row = longitud+3, sticky=W)             
        self.Bottonactualizar.grid(column=0, row=longitud+3)


    def obtenerHora (self):
        fecha = str(date.today())
        hora = str(datetime.now().hour)
        min = str(datetime.now().minute)
        f= str('Actualizado '+ fecha + ' '+ hora + ':'+ min)
        #print("Fecha es: ", f)
        return f
        

def testAPP ():
    app3 = Aplicacion3()

if __name__ == '__main__':
    testAPP()