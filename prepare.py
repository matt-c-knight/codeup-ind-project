import pandas as pd
from acquire import get_world_data
from sklearn.model_selection import train_test_split

def prep_world_data():
    df = get_world_data()
    #dropping null rows, only nulls are target variable and not going to impute mean
    df.dropna(inplace=True)
    #Creating a boolean column whether or not life exp is above or below 77
    df['highest_life_exp'] = df['lifeexpectancy'].apply(lambda x: 1 if x >= 77 else 0)
    #GNP is abbreviated. After doing calculations, I need to multiply gnp by a million to get actual figure. Will use this to determine gnp per capita.
    df['real_gnp'] = df.gnp * 1000000
    #Taking population and gnp to get more data
    df['gnp_per_capita'] = round(df.real_gnp / df.countrypopulation, 2)
    #Creating a column to determine how densly populated each country is to determine if that factors into life expectancy.
    df['population_density'] = df.countrypopulation / df.surfacearea
    
    train_validate, test = train_test_split(df, random_state=123, stratify=df.highest_life_exp)
    train, validate = train_test_split(train_validate, random_state=123, stratify=train_validate.highest_life_exp)
    return train, validate, test