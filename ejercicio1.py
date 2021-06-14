from tkinter import *
from tkinter import ttk, font, messagebox

class Aplicacion(object):
    __ventana = None
    __altura = None
    __peso = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de IMC")
        #self.__ventana.geometry('400x200')                 #si fuera geometria place

        self.__ventana.resizable(0,0)               #no se puede expandir

        self.marco = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10,10))

        fuente = font.Font(weight='bold')

        #ancho del borde en pixeles (borderwidth)
        #relief el tipo de borde- groove (), raised (espaciado en 3d)
        #padding espacio interno en el objeto dentro de la ventana, en ancho y alto, diez pixeles en este caso

        self.alturaLbl = ttk.Label(self.marco, text="Altura: ", font= fuente, padding=(5,5))
        self.pesoLbl = ttk.Label(self.marco, text="Peso: ", font = fuente, padding=(5,5))

        self.altcmLbl = ttk.Label(self.marco, text="cm", font= fuente, padding=(5,5))       #para mostrar como ultima columna, 1era fila el cm
        self.pesokgLbl = ttk.Label(self.marco, text="kg", font = fuente, padding=(5,5))     #para mostrar como ultima columna, 2era fila el kg    

        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__mensaje = StringVar()
        self.__mensaje2 = StringVar()

        #no es necesario inicializarlo
        self.__altura.set('')
        self.__peso.set('')
        self.__mensaje.set('')
        self.__mensaje2.set('')

        #para mostrar el mensaje de la interfaz
        self.mostrarMsj = ttk.Label (self.marco, textvariable=self.__mensaje, font = fuente, foreground="green", padding=(5,5))

        self.mostrarMsj2 = ttk.Label (self.marco, textvariable=self.__mensaje2, font = fuente, foreground="green", padding=(5,5))

        self.ctext1 = ttk.Entry(self.marco, textvariable = self.__altura, width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable = self.__peso, width=30)
        
        self.separador = ttk.Separator(self.marco, orient=HORIZONTAL)           #separador no tiene valor

        self.boton1 = ttk.Button(self.marco, text="Calcular", padding=(5,5), command=self.calcular)

        self.boton2 = ttk.Button(self.marco, text="Limpiar", padding=(5,5),command=self.limpiar)

        #colocamos las posiciones como si fueran de geometria grid

        #self.marco.grid(column=0, row=0)           hay ventana, no marco

        self.marco.grid(column=0, row=0)

        self.alturaLbl.grid(column=0, row=0)

        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.altcmLbl.grid(column = 3, row=0)

        self.pesoLbl.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.pesokgLbl.grid(column=3, row=1)

        self.separador.grid(column=0, row=3, columnspan=3)
        
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)

        self.mostrarMsj.grid(column = 0, row = 5, columnspan=3)

        self.mostrarMsj2.grid(column=0, row=6, columnspan=3)

        self.ctext1.focus_set()                 #establece el foco en la caja de entrada, altura
        self.__ventana.mainloop()
    
    def calcular(self):
        try: 
            if self.__altura.get() != None and self.__peso.get() != None:
                alt_m = float(self.__altura.get()) * 0.01
                calculo = float(float(self.__peso.get()) / (float(alt_m **2)))
                if calculo < 18.5:
                    composicion_corp= "Peso inferior al normal"
                
                elif calculo >= 18.5 and calculo < 25:     #24.9     
                    composicion_corp = "Peso Normal"
                
                elif calculo >= 25 and calculo < 30:         #29.9
                    composicion_corp = "Peso superior al normal"
                
                elif calculo >= 30:
                    composicion_corp = "Obesidad"

                self.mostrarMsj.configure(foreground='green')
                
                calculo = round(calculo, 2)         #redondeo de 2 valores flotantes
                self.__mensaje.set("(IMC) es "+ str(calculo)+"Kg/m2\n")
                
                self.__mensaje2.set(composicion_corp)

                print("Tu Indice de Masa Corporal(IMC) es "+str(calculo) + "Kg/m2\n" + composicion_corp)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')

    def limpiar(self):
        self.__altura.set("")
        self.__peso.set("")
        self.__mensaje.set("")
        self.__mensaje2.set("")

def testAPP():
    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()