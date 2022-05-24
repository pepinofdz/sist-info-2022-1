import pandas as pd
from pathlib import Path 

#Cargando bdd
data = pd.read_csv("Tablas Sin Editar/Candidaturas_2021.csv",sep=";")
data = pd.DataFrame(data)
print(data.head())
print(data.columns)


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



columnas = "ID Eleccion;ID Region;Region;Territorio;Candidato(a);Nombre;Paterno;Materno;Sexo;Edad;Rango;ID Partido;Partido".split(';')
#for j in columnas:
    #data[j] = data[j].apply(mayus_minus_y_esp)

#Agregar ID tabla
data.insert(loc = 0, column = 'ID', value = 0)
print(data)

data.dropna(inplace=True)

data.pop("Nombre")
data.pop("Paterno")
data.pop("Materno")
print(data.columns)

print(data.loc[:,"Partido"])


'''
#Pasar a .csv
filepath = Path("Tablas\ Editadas/Candidaturas_2020.csv")
data.to_csv(filepath, index = False)

'''