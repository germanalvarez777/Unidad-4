import json
from pathlib import Path
from claseManejaPacientes import ManejaPacientes
from clasePaciente import Paciente

class ObjectEncoder(object):
    __nombreArchivo=None
    def __init__(self, pathArchivo):
        self.__nombreArchivo=pathArchivo
    
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ManejaPacientes':
                pacientes=d['pacientes']
                manejador=class_()
                
                for i in range(len(pacientes)):
                    dPaciente=pacientes[i]
                    
                    class_name=dPaciente.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPaciente['__atributos__']
                    unPaciente=class_(**atributos)
                    manejador.agregarPaciente(unPaciente)
            
            return manejador
    
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__nombreArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    
    def leerJSONArchivo(self):
        with Path(self.__nombreArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario