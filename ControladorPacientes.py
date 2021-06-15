from clasePaciente import Paciente
from claseVistaPacientes import VistaPacientes, NewPaciente,IMC
from claseManejaPacientes import ManejaPacientes

class ControladorPacientes(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())
    
    # comandos de que se ejecutan a través de la vista
    def crearPaciente(self):
        nuevoPaciente = NewPaciente(self.vista).show()
        if nuevoPaciente:
            paciente = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            
            #agrega al paciente desde la clase vistaPaciente
            self.vista.agregarPaciente(paciente)
    
    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)
    
    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        
        paciente = self.repo.modificarPaciente(detallesPaciente)
        
        self.pacientes[self.seleccion] = paciente
        
        self.vista.modificarPaciente(paciente, self.seleccion)
        self.seleccion=-1
    
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)

        self.pacientes.pop(self.seleccion)
        
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1
    
    def PacienteIMC(self):
        if self.seleccion!=-1:
            paciente = self.pacientes[self.seleccion]
            imc=IMC(self.vista,paciente).show()
        else:
            return

    def start(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()