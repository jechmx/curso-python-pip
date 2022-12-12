from read_csv import read_csv
datos=read_csv('data.csv')
filtro=list(filter(lambda datos:datos['CCA3']=='COL',datos))
datos=filtro[0]
print(datos)
#print([columnas for key in filtro.keys])
