import pandas as pd

dataset = pd.read_csv('defunciones_fetales2.csv')

dataset['Tipo'] =  'vivo'
dataset.loc[:31227,'Tipo'] = 'muerto'

dataset.to_csv('finito.csv', index=False)
