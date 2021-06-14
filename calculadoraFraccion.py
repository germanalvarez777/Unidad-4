from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
import re

from claseFraccion import Fraccion

class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None

    numerador = None
    denominador = None

    unaFraccion = None
    otraFraccion = None

    evaluarFraccion = False

    valorSET = 0

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))

        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)

        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        
        #asigno un operador por defecto, para indicar que separo el numerador del denominador
        ttk.Button(mainframe, text='/', command=self.separarFraccion).grid(column=2, row=8, sticky=W)

        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        
        ttk.Button(mainframe, text='Limpiar', command=self.limpiar).grid(column=3, row=8, sticky=W)

        self.__panel.set('0')
        print("typo del panel: ", type(self.__panel.get()))
        #if self.__panel.get() == type(Fraccion):
        if re.match ('^[0-9]+/[0-9]$', self.__panel.get()):
            self.__panel.set('0')
            print("cambio su valor")

        panelEntry.focus()
        self.__ventana.mainloop()
    def ponerNUMERO(self, numero):
        if self.__operadorAux==None:
            self.__panel.set(self.valorSET)
            print("valor.set: ", self.__panel.get(), "tipo: ", type(self.__panel.get()))

            valor = self.__panel.get()
            self.__panel.set(valor+numero)          #esta concatenando los operandos              

            #print("PONER NUMERO- valor: {}, numero: {}".format(valor, numero))
            #print("PONER NUMERO1-Self.panel: ", self.__panel.get(), "\n")
        else:
            #print("PONER NUMERO-Operador aux: ", self.__operadorAux, "\n")
            
            valor=self.__panel.get()            #asigna el valor que contiene al primer operando
            self.__primerOperando=int(valor)
            #print("PONER NUMERO- 1er Operando: ", self.__primerOperando, "\n")
            self.__panel.set(numero)
            #print("PONER NUMERO2-Self.panel: ", self.__panel.get(), "\n")        

            #if self.__operadorAux == '&':
            #    self.__segundoOperando = self.__panel.get()
            
            self.__operadorAux=None

    def borrarPanel(self):
        self.__panel.set('0')
        #print("Se borro el panel\n")

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='/':                          
                        try:
                            resultado=operando1/operando2
                        except ZeroDivisionError:
                            messagebox.showerror(title='Division por cero', message='No se permite denominador nulo!!')

        if type(operando1) == Fraccion or type(operando2) == Fraccion:
            #print("Operando1: ", operando1.obtenerFraccionSTR(), "operando2: ", operando2.obtenerFraccionSTR(), "operador: ", operacion)
            #print("resultado: ", resultado.obtenerFraccionSTR())
            
            #self.__panel.set(str(resultado.simplificar()))                        #me mostrara el resultado en el panel
            self.__panel.set(str(resultado.obtenerFraccionSTR())) 
        else:
            self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        
        if op=='=':
            operacion=self.__operador.get()
            self.__segundoOperando=int(self.__panel.get())

            if self.evaluarFraccion == True:
                self.denominador = int (self.__panel.get())
                self.otraFraccion = Fraccion(self.numerador, self.denominador)

                #print("2-numerador: {}, Denom: {}".format(self.numerador, self.denominador))

                #print("Fraccion1: ", self.unaFraccion.obtenerFraccionSTR())
                #print("1eer Operando: ", self.__primerOperando, "2do Operando: ", self.__segundoOperando)
                
                #print("Fraccion2: ", self.otraFraccion.obtenerFraccionSTR())
                if self.unaFraccion != None: 
                    if self.otraFraccion != None:
                            self.resolverOperacion(self.unaFraccion, operacion, self.otraFraccion)
                    else:
                        self.resolverOperacion(self.unaFraccion, operacion, self.__segundoOperando)
                else:
                    if self.otraFraccion != None:
                        self.resolverOperacion(self.__primerOperando, operacion, self.otraFraccion)
            
            else:    

                #print("CASO 1:1er Operando: {}, 2do Operando: {}, Operacion: {}\n".format(self.__primerOperando, self.__segundoOperando, operacion))
                    
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                
                if self.evaluarFraccion == True:
                    self.denominador = int (self.__panel.get())
                    self.unaFraccion = Fraccion(self.numerador, self.denominador)

                    self.valorSET = self.__panel.get()
                    self.__panel.set(self.unaFraccion.obtenerFraccionSTR())
                    
                    #print("1-numerador: {}, Denom: {}".format(self.numerador, self.denominador))
                    #print("1)Fraccion1: ", self.unaFraccion.obtenerFraccionSTR())
                    
                #self.__panel.set('0')
                self.__operador.set(op)
                self.__operadorAux=op
                #print("Oper antes estaba en vacio, ahora: ", self.__operador.get(), "y oper Aux: ", self.__operadorAux)

                

            else:
                operacion=self.__operador.get()
                self.__segundoOperando=int(self.__panel.get())
                
                if self.__operadorAux == '&' or self.evaluarFraccion == True:
                    self.denominador = int (self.__panel.get())
                    self.unaFraccion = Fraccion(self.numerador, self.denominador)

                    #print("1-numerador: {}, Denom: {}".format(self.numerador, self.denominador))
                    #print("1)Fraccion1: ", self.unaFraccion.obtenerFraccionSTR())

                #print("Fraccion2: ", otraFraccion.obtenerFraccionSTR())

                #print("CASO 2:1er Operando: {}, 2do Operando: {}, Operacion: {}\n".format(self.__primerOperando, self.__segundoOperando, operacion))

                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux=op
    
    def limpiar (self):
        self.__operadorAux = None
        self.__operador.set('')
        self.borrarPanel()
        self.__primerOperando = None
        self.__segundoOperando = None
        self.evaluarFraccion = False
        self.numerador = None
        self.denominador = None
        self.unaFraccion = None
        self.otraFraccion = None

    def separarFraccion (self):
        self.numerador = int(self.__panel.get())

        self.__operadorAux = '&'

        self.evaluarFraccion = True


def main():
    calculadora=Calculadora()
    
if __name__=='__main__':
    main()