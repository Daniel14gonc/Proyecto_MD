import pandas as pd
from unidecode import unidecode

def remove_accents(text):
    return unidecode(text)

def prepare_dicts():
    departamentos = {}
    municipios = {}
    meses = {}
    civil = {}
    sitio = {}
    esc = {}
    with open('dep.txt') as f:
        for line in f:
            key, value = line.strip().split(',')
            departamentos[value] = key
    
    with open('mun.txt') as f:
        for line in f:
            key, value = line.strip().split(',')
            municipios[value] = key

    with open('meses.txt') as f:
        for line in f:
            key, value = line.strip().split(',')
            meses[value] = key
    
    with open('civil.txt') as f:
        for line in f:
            key, value = line.strip().split(',')
            civil[value] = key

    with open('sitio.txt') as f:
        for line in f:
            key, value = line.strip().split(',')
            sitio[value] = key

    with open('esc.txt') as f:
        for line in f:
            key, value = line.strip().split(',')
            esc[value] = key

    return departamentos, municipios, meses, civil, sitio, esc

departamentos, municipios, meses, civil, sitio, esc = prepare_dicts()
print(sitio)
sexo = {"Hombre": 1, "Mujer": 2, "Ignorado": 9}
tipo = {"Simple": 1, "Doble": 2, "Triple": 3}
asis = {'Medico': 1, 'Personal de Enfermeria': 6, 'Paramedico': 2, 'Comadrona': 3, 'Empirico': 4, 'Ninguno': 5, 'Ignorado': 9}

def replace_encoding(df):
    df['DEPREG'] =  df['DEPREG'].replace(departamentos)
    df['DEPOCU'] = df['DEPOCU'].replace(departamentos)
    df['DEPREM'] = df['DEPREM'].replace(departamentos)

    df['SEXO'] = df['SEXO'].replace(sexo)

    df['MUPREG'] = df['MUPREG'].replace(municipios)
    df['MUPOCU'] = df['MUPOCU'].replace(municipios)
    df['MUPREM'] = df['MUPREM'].replace(municipios)

    df['SITIOOCU'] = df['SITIOOCU'].replace(sitio)

    df['ESCIVM'] = df['ESCIVM'].replace(civil)

    df['MESREG'] = df['MESREG'].replace(meses)
    df['MESOCU'] = df['MESOCU'].replace(meses)

    df['TIPAR'] = df['TIPAR'].replace(tipo)

    df['ASISREC'] = df['ASISREC'].replace(asis)

    df['ESCOLAM'] = df['ESCOLAM'].replace(esc)


# # df_2010 = pd.read_csv("2010.csv")
# # df_2011 = pd.read_csv("2011.csv")
# # df_2012 = pd.read_csv("2012.csv")
# # df_2013 = pd.read_csv("2013.csv")
# # df_2014 = pd.read_csv("2014.csv")
# # df_2015 = pd.read_csv("2015.csv")
# # df_2016 = pd.read_csv("2016.csv")
# # df_2017 = pd.read_csv("2017.csv")
# # df_2018 = pd.read_csv("2018.csv")
# # df_2019 = pd.read_csv("2019.csv")
# # df_2020 = pd.read_csv("2020.csv")
# # df_2021 = pd.read_csv("2021.csv")

# # columnas_deseadas = ["DEPREG", "MUPREG", "MESREG", "AÑOREG", "DEPOCU", "MUPOCU", "SEXO", "DIAOCU", "MESOCU", "TIPAR", "CLAPAR", "VIAPAR", "SEMGES", "EDADM", "DEPREM", "MUPREM", "ESCIVM", "NACIOM", "ESCOLAM", "CAUDEF", "ASISREC", "SITIOOCU", "TOHITE", "TOHINM", "TOHIVI"]

otras = ['DEPREG', 'MUPREG', 'MESREG', 'AÑOREG', 'DEPOCU', 'MUPOCU', 'DIAOCU', 'MESOCU', 'SEXO', 'TIPAR', 'EDADM', 'DEPREM', 'MUPREM', 'ESCIVM', 'ASISREC', 'SITIOOCU', 'TOHITE', 'TOHINM', 'TOHIVI', 'ESCOLAM']

# # df_2010 = df_2010[columnas_deseadas]
# # df_2011 = df_2011[columnas_deseadas]
# # df_2012 = df_2012[columnas_deseadas]
# # df_2013 = df_2013[columnas_deseadas]
# # df_2014 = df_2014[columnas_deseadas]
# # df_2015 = df_2015[columnas_deseadas]
# # df_2016 = df_2016[columnas_deseadas]
# # df_2017 = df_2017[columnas_deseadas]
# # df_2018 = df_2018[columnas_deseadas]
# # df_2019 = df_2019[columnas_deseadas]
# # df_2020 = df_2020[columnas_deseadas]
# # df_2021 = df_2021[columnas_deseadas]


years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

defunc = []
born = []

for year in years:
    df_defunction = pd.read_csv(year+".csv")
    df_defunction = df_defunction[otras]
    defunc.append(df_defunction)
    df_born = pd.read_csv(year+"_nac.csv")
    df_born = df_born[otras]
    born.append(df_born)

df_defunc = pd.concat(defunc, ignore_index=True)
df_born = pd.concat(born, ignore_index=True)

df_born = df_born.sample(n=df_defunc.shape[0], random_state=123)

df_born = df_born.applymap(lambda x: remove_accents(x) if isinstance(x, str) else x)

replace_encoding(df_born)

df = pd.concat([df_defunc, df_born], ignore_index=True)

print(df_defunc.shape[0])

df_born.to_csv("defunciones_fetales3.csv", index=False)
