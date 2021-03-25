age = 17

if age >= 18:
    print('puedes votar')
else:
    print('No puedes votar')



lista = ['rojo', 'azul', 'amarillo']
color = 'rosa'
if color not in lista:
    print('no esta el color ' + str(color) + ' en la lista')


if age >= 18:
    print('Puedes votar')
elif age < 18 and age > 16:
    print('no puedes votar, pero puedes conducir')  