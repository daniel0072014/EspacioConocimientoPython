#diaSemana={'lunes', 'martes', 'miercoles'}
#print(siaSemana)


#Dict

target={
    'Name':'Jhon',
    'LastName':'Doe',
    'Contact':{
        'Phone':3500000,
        'e-mail':'daniel@gmail.com'
    },
    'Management Team':False
}


#longitud
print(len(target))

#busqueda de dato por key
print(target['Contact'])
print(target.get('Management Team'))

#Modificar un dato
target['Management Team'] = True
print(target['Management Team'])

target['Contact']={
    'Phone':3521455,
    'e-mail':'djddjh@gmail.com'
}
print(target['Contact'])


#recorrido del diccionario
for key, value in target.items():
    print(key,': ', value)

for key in target.keys():
    print(key)

for value in target.values():
    print(value)


#validar existencia de un elemento
print('Contact' in target)

#agregar un nueva dato
target['Contact']['Address'] = 'Av siempre viva 742'
for key, value in target.items():
    print(key,': ', value)

#No es posible duplicar llaves

#Eliminar un dato por medio de la key
target.pop('LastName')
for key, value in target.items():
    print(key,': ', value)

#limpiar todr el diccionario
target.clear()

#borrar diccionario
del target
print(target)
