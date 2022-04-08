class operaciones:

    listanumeros = [0,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,7,8,9]

    def esprimo (x):
        if x > 1:
            for num in range(2,x):
                if (x % num) == 0:
                    return False
            return True
        else:
            return False
    
    def valor_modal(lista):
        lista_unicos = []
        lista_repeticiones = []
        if len(lista) == 0:
            return None
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def convertirtemp(valor,origen,destino):
        if origen == 'celcius':
            if destino == 'farenheit':
                resultado = (valor*9/5)+32
            elif destino == 'kelvin':
                resultado = (valor+273.15)
            elif destino == 'celcius':
                resultado = valor
            else:
                print('destino no valido')
        elif origen == 'farenheit':
            if destino == 'celcius':
                resultado = ((valor-32)*5)/9
            elif destino == 'kelvin':
                resultado = (((valor-32)*5)/9)+273.15
            elif destino == 'farenheit':
                resultado = valor
            else:
                print('destino no valido')
        elif origen == 'kelvin':
            if destino == 'celcius':
                resultado = valor-273.15
            elif destino == 'farenheit':
                resultado = ((valor-273.15)*9/5)+32
            elif destino == 'kelvin':
                resultado = valor
            else:
                print('destino no valido')
        else:
            print('el valor de origen no es valido')
        return resultado
    def factorial (x):
        resultado = x
        if type(x) == int and x >= 0:
            if x == 0:
                resultado = 1
                return resultado
            else:
                for i in reversed(range(1,x)):
                    resultado = resultado*i
                return resultado