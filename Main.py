from RepositorioPacientes import RespositorioPacientes
from claseVistaPacientes import VistaPacientes
from ControladorPacientes import ControladorPacientes
from claseObjectEncoder import ObjectEncoder
def main():
    enc=ObjectEncoder('pacientes.json')
    repo=RespositorioPacientes(enc)
    vista=VistaPacientes()
    controlador=ControladorPacientes(repo, vista)

    #actualizar datos
    vista.setControlador(controlador)
    controlador.start()

    #guarda los datos actualizados    
    controlador.salirGrabarDatos()

if __name__ == "__main__":
    main()