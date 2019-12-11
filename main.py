# Crea np_baseball (3 columnas)
np_baseball = np.array(baseball)
# Imprime la suma de np_baseball y updated
np_baseball = np.array(updated)
print(np_baseball)

# Crea un array numpy: conversion
conversion = np.array([0.0254,0.453592,1])

# Imprime el producto de np_baseball y conversion
print (np_baseball*conversion)

10.-
def e_f(string)
	string=string.split(' ')
	return string
	
a = 'Hola esto es una cadena'

e_f(a)

11.-
	

13.-
	B 
	import pandas as pd
	li=[100,200,300]
	lg=[10,20,30]
	def get_columns (lista1,lista2):
		dataframe = pd.DataFrame({
			'Ingresos': li,
			'Gastos  ': lg
		})
		return dataframe
	get_columns(lista1=li, lista2=lg)

	C
	import pandas as pd
	li=[100,200,300]
	lg=[10,20,30]
	def get_columns (lista1,lista2):
		dataframe['ingresos']=lista1
		dataframe['gastos  ']=lista2
		return dataframe

	get_columns(lista1=li, lista2=lg)

