nombres =['Elena', 'Manuel', 'Erika', 'Jose', 'Leo', 1, False]

'''for nombre in nombres:
print(nombre)'''

print(nombres)
print(nombres[1])
print(nombres[-1]) # para imprimir de forma inversa- desde la ultima posicion
print('==============')
#imprimir rangos
print(nombres[1:3])
print(nombres[:3])
print(nombres[3:])

print('=============')

#setear valores
nombres[3]='Sofia'
print(nombres[3])

#Metodos de la lista

#contar la cantidad de elementos de la lista
print(len(nombres))
print("=================")

#agregar datos a la lista en la ultima posicion
nombres.append(True)
print(nombres)

#insertar elemento en un indice especifico
nombres.insert(2,5)
print(nombres)

#remover data por valor
nombres.remove(5)
print(nombres)

#remover el ultimo valor de la lista
nombres.pop()
print(nombres)
print("===================")

#remover un valor con indice especificado
del nombres[0]
print(nombres)

#limpiar todos los elementos de la lista
nombres.clear()
print(nombres)













