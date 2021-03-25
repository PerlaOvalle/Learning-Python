def saludar(nombre):
    print('Hola ' + str(nombre))



print('dime tu nombre...')
nombre = raw_input()
saludar(nombre)

def alCuadrado(numero):
    return numero * numero

numeroAlCuadrado = alCuadrado(5)
print(numeroAlCuadrado)