from env import host, user, password

import pandas as pd
import numpy as np
import os

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def new_world_data():
    
    sql_query = 'SELECT Code, country.Name as countryname, Continent, Region, SurfaceArea, country.Population as countrypopulation, LifeExpectancy, GNP, city.name as cityname, city.population as citypopulation FROM country JOIN city on country.code = city.countrycode'
    df = pd.read_sql(sql_query, get_connection('world'))
    df.to_csv('country.csv')
    return df

def get_world_data(cached=False):
    
    if cached or os.path.isfile('country.csv') == False:
        df = new_world_data()
    else:
        df = pd.read_csv('country.csv', index_col=0)
    return df