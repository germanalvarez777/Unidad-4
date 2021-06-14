import requests

class Provincia(object):
    __nombre = None
    __capital = None
    __cantHab = None
    __cantDep = None

    temperatura = None
    ser_termica = None
    humedad = None

    def __init__(self, nombre, capital, cantHab, cantDep):
        self.__nombre = nombre
        self.__capital = capital
        self.__cantHab = cantHab
        self.__cantDep = cantDep

    def getNombreProv (self):
        return self.__nombre
    
    def getCapitalProv (self):
        return self.__capital

    def getCantHab (self):
        return self.__cantHab
    
    def getCantDep (self):
        return self.__cantDep
    
    def toJSON (self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.__nombre,
                capital = self.__capital,
                cantHab = self.__cantHab,
                cantDep = self.__cantDep
            )
        )
        return d

    def getTemperatura(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format(self.getNombreProv())

        response = requests.get(url)
        lista = response.json()
        #print(lista)
        i = 0
        temp = None
        if lista['cod'] == '404':           #buscamos la temperatura por la capital de la prov
            url2 = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format(self.getCapitalProv())
            response2 = requests.get(url2)
            lista2 = response2.json()
            #print(lista2)

            temp = lista2['main']['temp']   
        else:                                   
            temp = lista['main']['temp']

        return temp
    
    def getSensacionTermica (self):
        url = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format(self.getNombreProv())

        response = requests.get(url)
        lista = response.json()
        #print(lista)
        i = 0
        
        s_term = None
        if lista['cod'] == '404':           #buscamos la sensacion termica por la capital de la prov
            url2 = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format(self.getCapitalProv())
            response2 = requests.get(url2)
            lista2 = response2.json()
            s_term = lista2['main']['feels_like']
        else:                                   
            s_term = lista['main']['feels_like']

        return s_term

    def getHumedad (self):                  
        url = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format(self.getNombreProv())

        response = requests.get(url)
        lista = response.json()
        #print(lista)
        i = 0
        humedad = None

        if lista['cod'] == '404':           #buscamos la humedad por la capital de la prov
            url2 = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format(self.getCapitalProv())
            response2 = requests.get(url2)
            lista2 = response2.json()
            humedad = lista2['main']['humidity']
        else:                                   
            humedad = lista['main']['humidity']

        return humedad

"""
if __name__ == '__main__':
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format('San Juan')
    response = requests.get(url)
    lista = response.json()
    #print(lista)
    temp = None
    s_term = None
    humedad = None

    #if lista['sys']['country'] == 'AR':
    if lista['cod'] == '404':
        url2 = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=28f2a3d9e309905e3fe44052ae6d06ec'.format('Rawson')
        #if lista['sys']['country'] == 'AR':
        response2 = requests.get(url2)
        lista2 = response2.json()
        #print(lista2)

        temp = lista2['main']['temp']
        s_term = lista2['main']['feels_like']
        humedad = lista2['main']['humidity']
    else:
        temp = lista['main']['temp']
        s_term = lista['main']['feels_like']
        humedad = lista['main']['humidity']
        

    print("Temperatura: ºC", temp)
    print("Sensacion Termica: ºC", s_term)
    print("Humedad: %", humedad)                                """ 