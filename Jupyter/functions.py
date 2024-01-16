import pandas as pd
import numpy as np
from datetime import datetime
def tipo_dato(df):
    ''' 
    Realiza el analisis de los tipos de dato del dataframe

    La funcion recibe un DataFrame (df) y devuelve un resumen de su contenido incluyendo infomracion sobre los tipos de datos de cada columna.


    Parameters:
    df(pandas.Dataframe):El DataFrame que se busca analizar.

    Returns: 
        pandas.DataFrame :Un Dataframe con el resumen de cada columna lo cual incluye:

            * nombre_campo: Nombre de columna
            *tipo_dato: Tipo de dato en cada columna
            *nulo: Cantidad de valores nuleos en cada columna
            *no_nulo%: Porcentaje de vaolores no nulos
            *nulo%: Porcentaje de valores Nulos

    '''

    titulos = {"nombre_campo":[], "tipo_dato":[], "nulo":[], "no_nulo%":[], "nulo%":[]}

    for columna in df.columns:
        no_nulos_porc = (df[columna].count()/ len(df)) * 100
        titulos["nombre_campo"].append(columna)
        titulos["tipo_dato"].append(df[columna].apply(type).unique())
        titulos["no_nulo%"].append(round(no_nulos_porc,2))
        titulos["nulo%"].append(round(100-no_nulos_porc,2))
        titulos["nulo"].append(df[columna].isnull().sum())
        
            
    df_info = pd.DataFrame(titulos)

    return df_info



def duplicados(df,column):
    '''
    Revisa y muestra la fila cuyos valores de la columna se reppiten.

    Recibe un dataframe y el nombre de la columna donde se desee revisar si hay datos duplicados.

    parameters:
        df(pandas.DataFrame): El DataFrame en el que se buscaran filas duplicadas.
        column (str): El nombre de la columna donde se buscara los datos duplicados

    returns:
        pandas.Dataframe or str: Un dataframe con las filas duplicadas. En caso de no haber duplicados devuelve el mensaje "No se encontrar duplicados"


    '''

    rows_duplicated = df[df.duplicated(column, False)]

    if rows_duplicated.empty:
        return "No se encontraron duplicados"
    
    return rows_duplicated.sort_values(by=column)


def time(x):
    '''
    Convierte un valor a un objeto de tiempo si es posible.

    Esta función acepta diferentes tipos de entrada y trata de convertirlos en objetos de tiempo (time) de Python.
    Si la conversión no es posible, devuelve None.

    parameters:
        x (str, datetime, or any): El valor que se desea convertir a un objeto de tiempo (time).

    returns:
        datetime.time or None: Un objeto de tiempo si la conversión es exitosa,
        o None si no es posible realizar la conversión.
    '''
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    return x


def cohen (g1,g2):
    '''
    Calcula la estadistica de Cohen para dos grupos.
    
    parameters:
        g1: grupo 1
        g2: grupo 2
    returns:
        d : el tamaño de la estadistica de cohen. 
            
    '''

    dif = g1.mean() - g2.mean()
    var1 =g1.var()
    var2 = g2.var()
    n1= len(g1)
    n2= len(g2)
    d =dif / np.sqrt((n1* var1 + n2 * var2) / (n1+n2))

    return d