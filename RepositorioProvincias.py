from ManejaProvincias import ManejaProvincias
from claseProvincia import Provincia
from ObjetoEncoder import ObjectEncoder

class RepositorioProvincias (object):
    __encoder=None
    __manejador=None
    def __init__(self, conn):
        self.__encoder = conn
        diccionario=self.__encoder.leerJSONArchivo()
        self.__manejador=self.__encoder.decodificarDiccionario(diccionario)
    
    def obtenerListaProvincias (self):
        return self.__manejador.getListaProvincias()
    
    def agregarProvincia (self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    
    """
    def modificarProvincia(self, provincia):
        self.__manejador.updateProvincia(provincia)
        return provincia        
    
    def borrarProvincia (self, provincia):
        self.__manejador.deleteProvincia (provincia)    """
    
    def grabarDatos(self):
        self.__encoder.guardarJSONArchivo(self.__manejador.toJSON()) 