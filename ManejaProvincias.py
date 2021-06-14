from claseProvincia import Provincia

class ManejaProvincias (object):
    indice = 0
    __listaProvincias = None
    def __init__(self):
        self.__listaProvincias = []

    def agregarProvincia (self, provincia):
        #indice es variable de clase, que se incrementa por cada
        #provincia agregada

        provincia.rowid = ManejaProvincias.indice
        ManejaProvincias.indice += 1
        self.__listaProvincias.append(provincia)

    def getListaProvincias (self):
        return self.__listaProvincias
    
    """
    def updateProvincia (self, provincia):
        indice = self.obtenerIndiceProvincia (provincia)
        self.__listaProvincias[indice] = provincia
    
    def obtenerIndiceProvincia (self, provincia):
        bandera = False
        i = 0
        while ((i < len(self.__listaProvincias)) and (bandera == False)):
            if self.__listaProvincias[i].rowid == provincia.rowid:
                bandera = True
            else:
                i += 1
        return i            """

    def toJSON (self):
        d = dict(
            __class__ = self.__class__.__name__,
            provincias = [provincia.toJSON() for provincia in self.__listaProvincias]
        )
        return d