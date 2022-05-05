from fastapi import FastAPI
import pandas as pd
import json
import csv
import os
from pydantic import BaseModel

app = FastAPI()

MEDIA_ROOT = os.path.expanduser("C:/Users/angel/OneDrive/Escritorio/FastAPI/iris.csv")

@app.get("/")
async def root():
 # Retornar el mensaje bienvenido a FastAPI
    return {"message": "Welcome to FastAPI!!"}


@app.get("/get_iris/")
async def root():
 # Cargamos el dataset con ayuda de pandas:
    X_df = pd.read_csv(MEDIA_ROOT)
 # Lo transformamos a json:
    data = X_df.to_json(orient="index")
    data = json.loads(data)
 # Retornar el dataset
    return data


class Iris(BaseModel):
 sepal_length: float
 sepal_width: float
 petal_length: float
 petal_width: float
 species: str


@app.post("/post_Iris/")
async def insertData(item: Iris):
 # Leemos el archivo iris.csv e
 # insertamos en la última línea los campos a insertar
    with open(MEDIA_ROOT, 'a', newline='') as csvfile:
 # Nombres de los campos:
        fieldnames = ['sepal_length', 'sepal_width', 'petal_length',
                        'petal_width', 'species']
 # escribir en el csv
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 # insertar en la última fila:
        writer.writerow({'sepal_length': item.sepal_length,
                        'sepal_width': item.sepal_width,
                        'petal_length': item.petal_length,
                        'petal_width': item.petal_width,
                        'species': item.species})
    return item


@app.put("/put_Iris/")
async def updateData(item: Iris):
# Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOT)
# Modificamos el último dato con los valores que nos lleguen:
    nuevos_valores = [item.sepal_length, item.sepal_width, item.petal_length, item.petal_width, item.species]
    df[-1:] = nuevos_valores
 # convertir a csv
    df.to_csv(MEDIA_ROOT, index=False)
    df = df.to_json(orient="index")
    df = json.loads(df)
# Retornamos el id que hemos modificado y el dato en formato diccionario:
    return df


@app.delete("/delete_Data/")
async def deleteData():
 # Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOT)
 # Eliminar la última fila
    df.drop(df.index[-1], inplace=True)
 # convertir a csv
    df.to_csv(MEDIA_ROOT, index=False)
    return 'Eliminado'



MEDIA_ROOTT = os.path.expanduser("C:/Users/angel/OneDrive/Escritorio/FastAPI/id.csv")


@app.get("/get_id/")
async def root():
 # Cargamos el dataset con ayuda de pandas:
    X_df = pd.read_csv(MEDIA_ROOTT)
 # Lo transformamos a json:
    data = X_df.to_json(orient="index")
    data = json.loads(data)
 # Retornar el dataset
    return data


class Persona(BaseModel):  # Definir una clase como parámetro
    nombre: str
    edad: int
    altura: float
    id : int


@app.post("/post_id/")
async def insertData(item: Persona):  # artículo debe ser coherente con la definición del objeto de artículo
    with open(MEDIA_ROOTT, 'a', newline='') as csvfile:
 # Nombres de los campos:
        fieldnames = ['Nombre', 'Edad', 'Altura',
                        'id']
 # escribir en el csv
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 # insertar en la última fila:
        writer.writerow({'Nombre': item.nombre,
                        'Edad': item.edad,
                        'Altura': item.altura,
                        'id': item.id})
    return item



@app.put("/put_id/")
async def updateData(item: Persona):
# Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOTT)
# Modificamos el último dato con los valores que nos lleguen:
    nuevos_valores = [item.nombre, item.edad, item.altura, item.id]
    df[-1:] = nuevos_valores
 # convertir a csv
    df.to_csv(MEDIA_ROOTT, index=False)
    df = df.to_json(orient="index")
    df = json.loads(df)
# Retornamos el id que hemos modificado y el dato en formato diccionario:
    return df


@app.delete("/delete_id/")
async def deleteData():
 # Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOTT)
 # Eliminar la última fila
    df.drop(df.index[-1], inplace=True)
 # convertir a csv
    df.to_csv(MEDIA_ROOTT, index=False)
    return 'Eliminado'
