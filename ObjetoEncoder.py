import json
from pathlib import Path
from ManejaProvincias import ManejaProvincias
from claseProvincia import Provincia

class ObjectEncoder(object):
    __nombreArchivo=None
    def __init__(self, pathArchivo):
        self.__nombreArchivo = pathArchivo
    
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_= eval(class_name)
            if class_name=='ManejaProvincias':
                provincias = d['provincias']
                manejador=class_()
                for i in range(len(provincias)):
                    dProvincia = provincias[i]
                    class_name = dProvincia.pop('__class__')
                    class_=eval(class_name)
                    atributos = dProvincia['__atributos__']
                    unaProv = class_(**atributos)
                    manejador.agregarProvincia(unaProv)
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