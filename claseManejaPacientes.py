from clasePaciente import Paciente

class ManejaPacientes:
    indice=0
    __listaPacientes=None
    def __init__(self):
        self.__listaPacientes=[]
    def agregarPaciente(self, paciente):
        #indice es variable de clase, que se incrementa por cada
        #provincia agregada

        paciente.rowid=ManejaPacientes.indice
        ManejaPacientes.indice+=1
        self.__listaPacientes.append(paciente)
    
    def getListaPacientes(self):
        return self.__listaPacientes
    
    def deletePaciente(self, paciente):
        indice=self.obtenerIndicePaciente(paciente)
        self.__listaPacientes.pop(indice)
    
    def updatePaciente(self, paciente):
        indice=self.obtenerIndicePaciente(paciente)
        self.__listaPacientes[indice]=paciente
    
    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i=0
        while not bandera and i < len(self.__listaPacientes):
            if self.__listaPacientes[i].rowid == paciente.rowid:
                bandera=True
            else:
                i+=1
        return i

    def toJSON(self):
        d = dict(
                __class__= self.__class__.__name__,
                pacientes=[paciente.toJSON() for paciente in self.__listaPacientes]
                )
        return d
