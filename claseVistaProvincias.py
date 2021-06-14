import tkinter as tk
from tkinter import messagebox
from claseProvincia import Provincia

#creamos el list box, listado de provincias, con el scrollbar
#scrollbar es la barra que se utiliza para observar el listado
class ListaProvincia (tk.Frame):        

    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar (self, provincia, index=tk.END):
        text = "{}".format(provincia.getNombreProv())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)
    
    def modificar(self, provincia, index):
        self.borrar(index)
        self.insertar(provincia, index)
    
    #evento si hago doble click izq en una provincia del listado
    #me la selecciona con un marcado
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

#widget labelFrame, donde ingresaremos los datos de cada provincia
class FormularioProvincia (tk.LabelFrame):

    
    #fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de Dptos/Partidos",
    #"Temperatura", "Sensacion Termica", "Humedad")
    
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de Dptos/Partidos")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        #realiza un mapeo, donde crear cada entry y label por cada elemento de la tupla
        #convierte el mapeo en lista, agrega todo los widgets dentro del frame

        self.frame.pack()       #se inserta por defecto

    #field es cada elemento de la tupla fields
    #trae su posicion y texto para agregarlo en el label y entry
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        
        return entry        #retorna el widget entry, para ingresar un texto
    
    def mostrarEstadoProvinciaEnFormulario (self, provincia):
        # a partir de una provincia, obtiene el estado
        # y establece en los valores en el formulario de entrada
        
        """
        values = (provincia.getNombreProv(), provincia.getCapitalProv(),
        provincia.getCantHab(), provincia.getCantDep(),
        provincia.getTemperatura(), provincia.getSensacionTermica(), provincia.getHumedad())       """
            
        values = (provincia.getNombreProv(), provincia.getCapitalProv(),
        provincia.getCantHab(), provincia.getCantDep())

        #para cada entry, elimina su widget, e inserta uno con un valor
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearProvinciaDesdeFormulario (self):
        #obtiene los valores de los campos del formulario
        #para crear una nueva provincia
        values = [e.get() for e in self.entries]
        provincia=None

        #para validar que los datos no esten vacios
        for e in self.entries:
            if e.get() == '':
                #parent=self en messagebox me permite no cerrar la ventana al saltar el error
                raise Exception(messagebox.showerror("Error de ingreso de datos", message='Debe ingresar un valor no vacio', parent=self))
        try:
            provincia = Provincia (*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia
    
    #elimina los datos que se colocaban en cada entry de los datos de las provincias
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

#salta nueva ventana para cargar los datos de la provincia
class NewProvincia (tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        #es necesario agregar este self.provincia?
        self.provincia = None

        self.form = FormularioProvincia (self)
        
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    
    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        
        #una vez creada la prov, se destruye la ventana modal
        if self.provincia:
            self.destroy()
    
    #espera una respuesta de la nueva ventana abierta
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

#clase que usaremos para mostrar toda la info de cada provincia, incluyendo 
#su temperatura, esta clase no sera utilizada para crear nueva provincia
class UpdateProvinciaFormConTemp (tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de Dptos/Partidos",
    "Temperatura", "Sensacion Termica", "Humedad")
    
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))

        self.frame.pack()      

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        
        return entry        #retorna el widget entry, para ingresar un texto
    
    def mostrarEstadoProvinciaEnFormulario (self, provincia):
        # a partir de una provincia, obtiene el estado
        # y establece en los valores en el formulario de entrada
        
        values = (provincia.getNombreProv(), provincia.getCapitalProv(),
        provincia.getCantHab(), provincia.getCantDep(),
        provincia.getTemperatura(), provincia.getSensacionTermica(), provincia.getHumedad())       
            

        #para cada entry, elimina su widget, e inserta uno con un valor
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    #elimina los datos que se colocaban en cada entry de los datos de las provincias
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
    
    

#ventana principal, que contiene la list box y el formulario de provincia(labelFrame)
#con labels y entry
class VistaProvincia (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        
        #creo el list box con scroller
        self.list = ListaProvincia (self, height=15)

        #utilizamos este formulario, para mostrar los datos con la informacion metedeologica
        self.form = UpdateProvinciaFormConTemp (self)

        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)

        self.form.pack(padx=10, pady=10)
       
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    
    #metodo que se ejecuta desde la clase controlador, para crear 
    #o seleccionar prov
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
        
        #self.form.bind_save(ctrl.modificarProvincia)
        #self.form.bind_delete(ctrl.borrarContacto)
    
    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)
    
    def verProvinciaEnForm (self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)
    
    def obtenerDetalles (self):
        return self.form.crearProvinciaDesdeFormulario()
