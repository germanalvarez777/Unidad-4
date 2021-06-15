from clasePaciente import Paciente
from claseObjectEncoder import ObjectEncoder
from claseManejaPacientes import ManejaPacientes

class RespositorioPacientes (object):
    __encoder=None
    __manejador=None
    def __init__(self, conn):
        self.__encoder = conn
        diccionario=self.__encoder.leerJSONArchivo()
        self.__manejador=self.__encoder.decodificarDiccionario(diccionario)
    
    def to_values(self, paciente):
        return paciente.getNombre(), paciente.getApellido(), paciente.getTelefono(),paciente.getAlturaCM(),paciente.getPesoKG()
    
    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()
    
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    
    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente
    
    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)
    
    def grabarDatos(self):
        self.__encoder.guardarJSONArchivo(self.__manejador.toJSON())
