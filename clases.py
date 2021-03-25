class Auto:
    modelo = ''
    agencia = ''
    precio = 0
    transmision = ''

    def __init__(self, modelo, agencia, precio, transmision):
        self.modelo = modelo
        self.agencia = agencia
        self.precio = precio
        self.transmision = transmision

    def TraerModeloYAgencia(self):
        return 'Modelo ' + str(self.modelo) + ' Agencia ' + str(self.agencia) 

aveo = Auto('Aveo 2021', 'Chevrolet', 2500000, 'Auto')


class Humano:
    nombre = ''
    edad = 0
    estatura = 0
    sexo = ''

    def __init__(self, nombre, sexo):
        self.nombre = nombre
        self.sexo = sexo
    
    def SetEstatura(self, estatura):
        self.estatura = estatura

    def GetNombreSexoEstatura(self):
        return 'Nombre ' + str(self.nombre) + ' Sexo ' + str(self.sexo) + ' Estatura ' + str(self.estatura)


class Profesionista(Humano):
    carrera = ''

    def SetCarrera(self, carrera):
        self.carrera = carrera

    def GetCarrera(self):
        return 'Carrera ' + str(self.carrera)

Perla = Profesionista('Perla', 'fem')
Perla.SetEstatura(1.50)
Perla.SetCarrera('Ingeniero')
print(Perla.GetNombreSexoEstatura())
print(Perla.GetCarrera())



