class Fraccion(object):
    __numerador = None
    __denominador = None
    __fraccion = None
    def __init__(self, priOperador=None, segOperador=None):
        self.__numerador = priOperador
        self.__denominador = segOperador
        self.__fraccion = str(str(self.__numerador) + '/' +str(self.__denominador))
    
    def getNum(self):
        return self.__numerador

    def getDenom (self):
        return self.__denominador

    def obtenerFraccionSTR (self):
        return self.__fraccion

    def __add__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            num1 = (self.__numerador * otraFraccion.getDenom()) + (self.__denominador * otraFraccion.getNum())
            den1 = self.__denominador * otraFraccion.getDenom()

            unaFraccion = Fraccion (num1, den1)                                  
        

        return unaFraccion
        
    
    def __radd__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            num1 = (self.__numerador * otraFraccion.getDenom()) + (self.__denominador * otraFraccion.getNum())
            den1 = self.__denominador * otraFraccion.getDenom()

            unaFraccion = Fraccion (num1, den1)                                  
        

        return unaFraccion

    def __sub__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            num1 = (self.__numerador * otraFraccion.getDenom()) - (self.__denominador * otraFraccion.getNum())
            den1 = self.__denominador * otraFraccion.getDenom()

            unaFraccion = Fraccion (num1, den1)                                  
        

        return unaFraccion

    def __rsub__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            num1 = (self.__numerador * otraFraccion.getDenom()) - (self.__denominador * otraFraccion.getNum())
            den1 = self.__denominador * otraFraccion.getDenom()

            unaFraccion = Fraccion (num1, den1)                                  
        
        
        return unaFraccion

    def __div__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            num1 = (self.__numerador * otraFraccion.getDenom())
            den1 = (self.__denominador * otraFraccion.getNum())

            unaFraccion = Fraccion (num1, den1)                                  
        

        return unaFraccion

    def __truediv__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            #num1 = (otraFraccion.getNum() * self.__denominador) 
            
            #den1 = (otraFraccion.getDenom() * self.__numerador)

            num1 = (self.__numerador * otraFraccion.getDenom())
            den1 = (self.__denominador * otraFraccion.getNum())

            unaFraccion = Fraccion (num1, den1)                                  
        

        return unaFraccion

    def __mul__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            num1 = (self.__numerador * otraFraccion.getNum())
            den1 = (self.__denominador * otraFraccion.getDenom())

            unaFraccion = Fraccion (num1, den1)                                  
        

        return unaFraccion

    def __rmul__ (self, otraFraccion):
        num1 = 0
        den1 = 0
        unaFraccion = None
        if type(self) == type(otraFraccion):
            num1 = (otraFraccion.getNum() * self.__numerador)
            den1 = (otraFraccion.getDenom() * self.__denominador)

            unaFraccion = Fraccion (num1, den1)                                  
        
        return unaFraccion


    def simplificar (self):
        s = self.__numerador/self.__denominador
        s = round(s,2)          #redondeamos con dos valores fraccionarios
        return s

if __name__ == '__main__':
    unafrac = Fraccion(3,2)
    otrafrac = Fraccion(4,5)
    print("Fraccion1: ", unafrac.obtenerFraccionSTR())
    print("Fraccion2: ", otrafrac.obtenerFraccionSTR())

    suma = 3 + unafrac
    print("Suma: ", suma.obtenerFraccionSTR())
    print("Suma simplificada: ", suma.simplificar())

    resta = otrafrac - unafrac
    print("Resta: ", resta.obtenerFraccionSTR())
    print("Resta simplificada: ", resta.simplificar())

    prod = 3 * unafrac
    print("Prod: ", prod.obtenerFraccionSTR())
    print("Prod simplificada: ", prod.simplificar())

    div = 3 / unafrac
    print("Division: ", div.obtenerFraccionSTR())
    print("Division simplificada: ", div.simplificar())