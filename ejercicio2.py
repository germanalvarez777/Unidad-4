from tkinter import *
from tkinter import ttk, font, messagebox
import requests

#conversor de dolar a pesos, sin usar boton de calcular (utilizacion de trace)
class Aplicacion2 (object):
    __ventana = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Conversor de moneda")
        self.__ventana.geometry('290x115')
        fuente = font.Font(weight='bold')               #weight peso, width = ancho-largo

        self.__ventana.resizable(0,0)

        framePrincipal = ttk.Frame(self.__ventana, padding="5 5 12 5")
        framePrincipal.grid(column=0, row=0, sticky=(N, W, E, S))           #en este caso fijamos en el centro por sticky
        
        #fijar para sacarlo
        framePrincipal.columnconfigure(0, weight=1)
        framePrincipal.rowconfigure(0, weight=1)

        framePrincipal['borderwidth'] = 2               #ancho del borde
        framePrincipal['relief'] = 'sunken'             #tipo de borde

        self.dolaresLbl = ttk.Label(framePrincipal, text="Dólares", font=fuente)
        self.pesosLbl = ttk.Label(framePrincipal, text="Pesos", font=fuente)

        self.__dolar = StringVar()
        self.__pesos = StringVar()

        self.__dolar.trace('w',self.calcular)               #detecta cambios en el valor ingresado, y ejecuta metodo calcular

        self.textoDolar = ttk.Entry(framePrincipal, textvariable = self.__dolar, width=7)

        self.valorPeso = ttk.Label(framePrincipal, textvariable = self.__pesos)            #label para mostrar el valor del resultado
        
        self.botonSalir = ttk.Button(framePrincipal, text="Salir", command=self.__ventana.destroy)


        self.texto1 = ttk.Label(framePrincipal, text="es equivalente a")
        self.texto1.grid(column=1, row=2, sticky=E)           #label con orientacio hacia el este


        self.textoDolar.grid(column=2, row=1, sticky=(W, E))                  #lo coloca en el medio el sticky

        self.dolaresLbl.grid(column=3, row=1, sticky=W)         #orientacion hacia el norte
        
        self.pesosLbl.grid(column=3, row=2, sticky=W)
        
        self.valorPeso.grid(column=2, row=2, sticky=(W, E))         #orientacion hacia el noreste


        self.botonSalir.grid(column=3, row=3, sticky=W)                     #sticky es orientacion hacia el norte

        for child in framePrincipal.winfo_children():
            child.grid_configure(padx=5, pady=5)            #margenes externos a cada elemento dentro del frame

        self.textoDolar.focus_set()                     #se asigna el foco a texto dolar para empezar a escribir directamente 
        
        self.__ventana.mainloop()

    def obtenerPrecioXApi (self):
        indice = 0
        url = 'https://www.dolarsi.com/api/api.php?type=dolar'

        #args = {"casa":{"nombre":"Oficial","compra":"94,370","venta":"100,370"}}
        #response = requests.get(url, params = args)
        response = requests.get(url)

        #print(response.url)                        #muestra la direccion de enlace

        #link del video que lo explica: https://www.youtube.com/watch?v=12NPmrdoKKs&list=PLpOqH6AE0tNguX5SG8HpcD3lfmzWrIn9n&index=2

        #fijarme para sacar este if
        #if response.status_code == 200:         #evaluo si el codigo de estatus del servidor, es igual a 200

        response_json = response.json()                 #se obtiene una lista de diccionarios, con info de bancos

        """for i in range(len(response_json)):             #mostramos el diccionario de cada fila de la lista
            print("=".center(40, "="))
            print(response_json[i])    """             

        while ((indice < len(response_json)) and (response_json[indice]['casa']['nombre'] != 'Oficial')):
            indice += 1
            
        if indice < len(response_json):
            precioOficial = response_json[indice]['casa']['venta']
            precioOficial = float(precioOficial.replace(',', '.'))
            #print("Precio es: {}".format(precioOficial))

        return precioOficial

    def calcular (self, *arg):                          #se agrega *arg por trace
        
        precioD = self.obtenerPrecioXApi()

        if self.textoDolar.get() != '':                 #no le coloco != None, pues me tomara error de tipo 
            try:
                valorD = float(self.textoDolar.get())

                operacion = valorD * precioD
                operacion = round (operacion, 2)                #para redondear el calculo, con 2 digitos fraccionarios
                self.__pesos.set(operacion)
            except:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor de dólar correcto')
                self.__dolar.set('')
                self.textoDolar.focus()
        else:
            self.__pesos.set('')

def testAPP ():
    app = Aplicacion2()

if __name__ == '__main__':
    testAPP()