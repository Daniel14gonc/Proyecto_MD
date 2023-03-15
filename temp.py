import pandas as pd

df_2019 = pd.read_csv("2019.csv")
df_2010 = pd.read_csv("2010.csv")
df_2011 = pd.read_csv("2011.csv")
df_2012 = pd.read_csv("2012.csv")
df_2013 = pd.read_csv("2013.csv")
df_2014 = pd.read_csv("2014.csv")
df_2015 = pd.read_csv("2015.csv")
df_2016 = pd.read_csv("2016.csv")
df_2017 = pd.read_csv("2017.csv")
df_2018 = pd.read_csv("2018.csv")

columnas_deseadas = ["DEPREG", "MUPREG", "MESREG", "AÑOREG", "DEPOCU", "MUPOCU", "SEXO", "DIAOCU", "MESOCU", "TIPAR", "CLAPAR", "VIAPAR", "SEMGES", "EDADM", "DEPREM", "MUPREM", "ESCIVM", "NACIOM", "ESCOLAM", "CAUDEF", "ASISREC", "SITIOOCU", "TOHITE", "TOHINM", "TOHIVI"]


df_2009 = df_2019[columnas_deseadas]
df_2010 = df_2010[columnas_deseadas]
df_2011 = df_2011[columnas_deseadas]
df_2012 = df_2012[columnas_deseadas]
df_2013 = df_2013[columnas_deseadas]
df_2014 = df_2014[columnas_deseadas]
df_2015 = df_2015[columnas_deseadas]
df_2016 = df_2016[columnas_deseadas]
df_2017 = df_2017[columnas_deseadas]
df_2018 = df_2018[columnas_deseadas]



df = pd.concat([df_2009, df_2010, df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018], ignore_index=True)

df.to_csv("defunciones_fetales.csv", index=False)
