class Paciente(object):
    __nombre = None
    __apellido = None
    __telefono = None
    __alturaCM = None
    __pesoKG = None
    def __init__(self, nombre, apellido, telefono, alturaCM, pesoKG):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__alturaCM = alturaCM
        self.__pesoKG = pesoKG
    
    def getNombre (self):
        return self.__nombre
    
    def getApellido (self):
        return self.__apellido
    
    def getTelefono (self):
        return self.__telefono
    
    def getAlturaCM (self):
        return self.__alturaCM

    def getPesoKG (self):
        return self.__pesoKG
    
    def getIMC (self):
        altMetro = int(self.__alturaCM) * 0.01
        calculoIMC = int(self.__pesoKG) / (altMetro**2)
        return calculoIMC

    def getComposicionCorporal (self):
        peso = self.getIMC()
        composicion_corp = None
        if peso < 18.5:
            composicion_corp= "Peso inferior al normal"
                
        elif peso >= 18.5 and peso < 25:     #24.9     
            composicion_corp = "Peso Normal"
                
        elif peso >= 25 and peso < 30:         #29.9
            composicion_corp = "Peso superior al normal"
                
        elif peso >= 30:
            composicion_corp = "Obesidad"

        return composicion_corp

    def toJSON (self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.__nombre,
                apellido = self.__apellido, 
                telefono = self.__telefono,
                alturaCM = self.__alturaCM,
                pesoKG = self.__pesoKG
            )
        )
        return d