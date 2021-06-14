from claseVistaProvincias import VistaProvincia, NewProvincia
from ManejaProvincias import ManejaProvincias

class ControladorProvincia (object):

    #repo es la clase repositorio, que contiene el encoder y manejador
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())
    
    #comandos que se ejecutan a traves de la vista
    def crearProvincia (self):
        nuevaProv = NewProvincia (self.vista).show()
        if nuevaProv:
            provincia = self.repo.agregarProvincia (nuevaProv)
            self.provincias.append(provincia)

            #agrega la provincia desde la clase vistaProv
            self.vista.agregarProvincia (provincia)
    
    #los metodos modificarProvincia y borrarProvincia no se agregan
    #pues la app no lo requiere


    def start (self):
        for p in self.provincias:
            self.vista.agregarProvincia (p)

        self.vista.mainloop()

    def seleccionarProvincia (self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verProvinciaEnForm (provincia)

    #guarda los nuevos datos actualizados o agregados en el 
    #repositorio del json
    def salirGrabarDatos (self):
        self.repo.grabarDatos()

    