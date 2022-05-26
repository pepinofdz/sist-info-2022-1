from numpy import fix
import pandas as pd
from pathlib import Path 

#TABLA 2021

#Cargando bdd
data = pd.read_csv("Tablas Sin Editar/Candidaturas_2021.csv",sep=";")
data = pd.DataFrame(data)
#print(data.head())
#print(data.columns)


#Revisión
def mayus_minus_y_esp(palabra):
    if palabra[0] != " ":
        p = palabra[0].upper()
        arreglada = p
        i = 1
    continuar = True
    while continuar:
        if i == len(palabra):
            continuar = False
        else:
            if palabra[i] == " " and i != len(palabra - 1):
                mayus = palabra[i+1].upper()
                arreglada += palabra[i] + mayus
                i+=2
            else:
                if palabra[i] == " ":
                    continuar = False
                else:
                    arreglada += palabra[i]
                    i+=1
        return arreglada

#Agregar Ano
data.insert(loc = 0, column = 'Ano', value = 2021)


#Agregar ID tabla
data.insert(loc = 0, column = 'ID', value = 2)


#Eliminar valores vacíos
data.dropna(inplace=True)


#Droppear columnas innecesarias
data.pop("Nombre")
data.pop("Paterno")
data.pop("Materno")
data.pop("Rango")

#Cambiar Candidato(a) a Candidato (según pauta)
data.rename(columns={'Candidato(a)' : 'Candidato'}, inplace=True)


#Pasar Edad de float a int
data['Edad'] = data['Edad'].astype(int)

#print(data.head(10))
#print(data.columns)

#Tabla 2013-2017

#Cargando bdd
data2 = pd.read_csv("Tablas Sin Editar/Candidaturas_2013_2017.csv",sep=";")
data2 = pd.DataFrame(data2)
#print(data2.head())
#print(data2.columns)


#Revisión

##Repara espacios dobles
def fix_nombres(nombre: str):
    lista_nombre = nombre.split(" ")
    lista_aux_1 = []
    for elemento in lista_nombre:
        if elemento != "":
            lista_aux_1.append(elemento)
    return " ".join(lista_aux_1)


df_candidato = data2["Candidato"].copy()
i = 0

while i < len(data2["Candidato"]):
    df_candidato[i] = fix_nombres(data2["Candidato"][i])
    i += 1

data2["Candidato"] = df_candidato
del df_candidato

#Cambiar nans por 0 en columna id region
data2["ID Region"] = data2["ID Region"].fillna(0)

#Agregar ID tabla
data2.insert(loc = 0, column = 'ID', value = 2)



#Agregar Region
valores_region = {
    0.0: "NACIONAL",
    1.0: "DE TARAPACA",
    2.0: "DE ANTOFAGASTA",
    3.0: "DE ATACAMA",
    4.0: "DE COQUIMBO",
    5.0: "DE VALPARAISO",
    6.0: "DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS",
    7.0: "DEL MAULE",
    8.0: "DEL BIOBIO",
    9.0: "DE LA ARAUCANIA",
    10.0: "DE LOS LAGOS",
    11.0: "DE AYSEN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO",
    12.0: "DE MAGALLANES Y DE LA ANTARTICA CHILENA",
    13.0: "METROPOLITANA DE SANTIAGO",
    14.0: "DE LOS RIOS",
    15.0: "DE ARICA Y PARINACOTA",
    16.0: "DE ÑUBLE"
}


data2.insert(loc = 4, column = "Region", value = data2['ID Region'].map(valores_region))

#Reposicionar Partido
df_partido = data2.pop("Partido")

data2.insert(loc = 9, column = "Partido", value = df_partido)


#insertar ID Partido

#se asume comunes -> comunes,
#   ind comunes -> comunes
#   ind evolucion politica -> evopoli
# pues no hay especificacion

valores_partido = {
    "CIUDADANOS": "CIUDADANOS",
    "COMUNES": "COMUNES",
    "CONVERGENCIA SOCIAL": "CONVERGENCIA",
    "EVOLUCION POLITICA": "EVOPOLI",
    "FEDERACION REGIONALISTA VERDE SOCIAL": "FREVS",
    "IGUALDAD": "IGUALDAD",
    "IND CIUDADANOS": "IND",
    "IND COMUNES": "COMUNES",
    "IND CONVERGENCIA SOCIAL": "IND",
    "IND EVOLUCION POLITICA": "EVOPOLI",
    "IND FEDERACION REGIONALISTA VERDE SOCIAL": "IND",
    "IND IGUALDAD": "IND",
    "IND PARTIDO COMUNISTA DE CHILE": "IND",
    "IND PARTIDO CONSERVADOR CRISTIANO": "IND",
    "IND PARTIDO DEMOCRATA CRISTIANO": "IND",
    "IND PARTIDO ECOLOGISTA VERDE": "IND",
    "IND PARTIDO HUMANISTA": "IND",
    "IND PARTIDO LIBERAL DE CHILE": "IND",
    "IND PARTIDO POR LA DEMOCRACIA": "IND",
    "IND PARTIDO PROGRESISTA DE CHILE": "IND",
    "IND PARTIDO RADICAL DE CHILE": "IND",
    "IND PARTIDO REGIONALISTA INDEPENDIENTE DEMOCRATA": "IND",
    "IND PARTIDO REPUBLICANO DE CHILE": "IND",
    "IND PARTIDO SOCIALISTA DE CHILE": "IND",
    "IND RENOVACION NACIONAL": "IND",
    "IND REVOLUCION DEMOCRATICA": "IND",
    "IND UNION DEMOCRATA INDEPENDIENTE": "IND",
    "INDEPENDIENTE": "IND",
    "INDEPENDIENTES": "IND",
    "NUEVO TIEMPO": "NT",
    "PARTIDO COMUNISTA DE CHILE": "PCCH",
    "PARTIDO CONSERVADOR CRISTIANO": "PCC",
    "PARTIDO DEMOCRATA CRISTIANO": "PDC",
    "PARTIDO ECOLOGISTA VERDE": "PEV",
    "PARTIDO HUMANISTA": "PH",
    "PARTIDO LIBERAL DE CHILE": "PL",
    "PARTIDO NACIONAL CIUDADANO": "PNC",
    "PARTIDO POR LA DEMOCRACIA": "PPD",
    "PARTIDO PROGRESISTA DE CHILE": "PRO",
    "PARTIDO RADICAL DE CHILE": "PR",
    "PARTIDO REGIONALISTA INDEPENDIENTE DEMOCRATA": "PRI",
    "PARTIDO REPUBLICANO DE CHILE": "REPUBLICANO",
    "PARTIDO SOCIALISTA DE CHILE": "PS",
    "PARTIDO TRABAJADORES REVOLUCIONARIOS": "PTI",
    "PARTIDO UNION PATRIOTICA": "UPA",
    "RENOVACION NACIONAL": "RN",
    "REVOLUCION DEMOCRATICA": "RD",
    "UNION DEMOCRATA INDEPENDIENTE": "UDI",
    "UNION PATRIOTICA": "UPA"
}

# Asignar ID "OTROS" a partidos sin id

data2.insert(loc = 9, column = "ID Partido", value = data2['Partido'].map(valores_partido))

data2["ID Partido"] = data2["ID Partido"].fillna("OTROS")

#print(data2.head(10))
#print(data2.columns)


print(data.columns)
print(data2.columns)

data_completo = pd.concat([data2, data])

data_completo["ID Region"] = data_completo["ID Region"].astype(int)

print(data_completo)

#Pasar a .csv
filepath = Path("Tablas Editadas/Candidaturas_2013_2017_2021.csv")
data_completo.to_csv(filepath, index = False, sep=";")

