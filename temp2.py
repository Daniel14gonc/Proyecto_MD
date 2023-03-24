import pandas as pd

# Leer los dos datasets
dataset1 = pd.read_csv('defunciones_fetales.csv')
dataset2 = pd.read_csv('defunciones_fetales3.csv')

# Crear un diccionario para almacenar los valores de SEMGES del primer dataset
semges_dict = dict(zip(dataset1.index, dataset1['SEMGES']))

# Crear una función para obtener el valor de SEMGES del diccionario o devolver 40 si no está disponible
def get_semgess_value(index):
    return semges_dict.get(index, 40)

# Aplicar la función a los índices del segundo dataset para obtener los valores de SEMGES
dataset2['SEMGES'] = dataset2.index.map(get_semgess_value)

# Establecer la columna 'Tipo' según las condiciones dadas
dataset2['Tipo'] = 'vivo'
dataset2.loc[:31227, 'Tipo'] = 'muerto'

# Guardar el dataset resultante en un nuevo archivo CSV
dataset2.to_csv('defun_nac.csv', index=False)
