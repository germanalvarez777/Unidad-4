from RepositorioProvincias import RepositorioProvincias
from claseVistaProvincias import VistaProvincia, ListaProvincia, FormularioProvincia, NewProvincia 
from ControladorProvincias import ControladorProvincia
from ObjetoEncoder import ObjectEncoder

def main():
    encoder = ObjectEncoder('provincias.json')
    repo = RepositorioProvincias(encoder)
    vista = VistaProvincia()
    controlador = ControladorProvincia (repo, vista)
    
    #actualizar datos
    vista.setControlador(controlador)
    controlador.start()

    #guarda los datos actualizados
    controlador.salirGrabarDatos()

if __name__ == '__main__':
    main ()