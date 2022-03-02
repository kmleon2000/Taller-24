import pandas as pd
import csv

# sirve para imprimir toda la información de las celdas del dataframe
# pd.set_option('display.max_colwidth', -1)

pdfile = pd.read_csv('serviciosurgenciasambulanciasagosto2020.csv', sep = ';', encoding='ISO-8859-1')

#punto 1
print('Lista de Empresas que prestan el servicio de ambulancia\n',pdfile.nombre_prestador.unique(),'\n\n')

#punto 2

csvfile = open('serviciosurgenciasambulanciasagosto2020.csv')
rows = [csv.reader(row, delimiter = ':') for row in csvfile]

print('Cantidad de registros ' + str(len(rows)),'\n\n')

for reg in csvfile:
    print(reg)

print(csvfile)

# punto 3
print('Primeras 5 filas del Dataframe\n',pdfile.head(5), '\n\n')

# punto 4
print('Direcciones de la sede SUBRED INTEGRADA DE SERVICIOS DE SALUD SUR E.S.E.\n',pdfile[pdfile['nombre_prestador'] == 'SUBRED INTEGRADA DE SERVICIOS DE SALUD SUR E.S.E.'].direccion.unique(),'\n\n')

# punto 5
print('Registros que contienen la palabra salud\n',pdfile[pdfile['nombre_prestador'].str.contains('salud', case = False)])