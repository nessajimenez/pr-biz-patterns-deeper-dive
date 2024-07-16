#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# these are the functions used to clean our data set

def made_df(file_name, year):
    try:
        df = pd.read_csv(file_name)
        df.columns = df.columns.str.strip().str.lower()
        df['year']= year
        return df
    
    except FileNotFoundError:
        print("File not found")
        
        
def combined_df(file_names, year):
    dataframes = []
    for file_name in file_names:
        try:
            df = pd.read_csv(file_name)
            df.columns = df.columns.str.strip().str.lower()
            df['year'] = year
            dataframes.append(df)
        except FileNotFoundError:
            print(f"File not found: {file_name}")
    
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df
        

def replace_naics(naics_code):
    # Dictionary mapping NAICS codes to industry names
    naics_dict = {
    "11": "11","21": "21","22": "22","23": "23","31": "31","32": "32","33": "33","42": "42","44": "44","45": "45",
    "48": "48","49": "49","51": "51","52": "52","53": "53","54": "54","55": "55","56": "56","61": "61","62": "62","71":"71",
    "72": "72","81": "81","92": "92"
}
    
    industry_code = naics_code[:2]  # Extract first two digits of NAICS code
    return naics_dict.get(industry_code, "00")


def replace_town_with_region(df,column):
    
    puerto_rico_regions = {
    "1": "Mountain","3": "Western","5": "Western","7": "Metro Area","9": "Mountain","11": "Western","13": "Northern",
    "15": "Southern","17": "Northern","19": "Mountain","21": "Metro Area","23": "Western","25": "Metro Area","27": "Northern","29": "Eastern",
    "31": "Metro Area","33": "Metro Area","35": "Mountain","37": "Eastern","39": "Mountain","41": "Mountain","43": "Southern",
    "45": "Mountain","47": "Mountain","49": "Eastern","51": "Northern","53": "Eastern","54":"Northern","55": "Western","57": "Southern",
    "59": "Southern","61": "Metro Area","63": "Metro Area","65": "Northern","67": "Western","69": "Eastern","71": "Western",
    "73": "Mountain","75": "Southern","77": "Eastern","79": "Western","81": "Western","83": "Eastern","85": "Eastern",
    "87": "Eastern","89": "Eastern","91": "Northern","93": "Western","95": "Eastern","97": "Western","99": "Western",
    "101": "Mountain","103": "Eastern","105": "Mountain","107": "Mountain","109": "Southern","111": "Southern","113": "Southern",
    "115": "Western","117": "Western","119": "Eastern","121": "Western","123": "Southern","125": "Western","127": "Metro Area",
    "129": "Eastern","131": "Western","133": "Southern","135": "Northern","137": "Northern","139": "Metro Area","141": "Mountain",
    "143": "Northern","145": "Northern","147": "Eastern","149": "Southern","151": "Eastern","153": "Western",
}

    # Replace the town with its corresponding region
    return df[column].map(lambda x: puerto_rico_regions.get(str(x), x))


def replace_code_with_town(df, column):

    pr_towns = {
    '1': 'Adjuntas', '3': 'Aguada', '5': 'Aguadilla', '7': 'Aguas Buenas', '9': 'Aibonito',
    '11': 'Anasco', '13': 'Arecibo', '15': 'Arroyo', '17': 'Barceloneta', '19': 'Barranquitas',
    '21': 'Bayamon', '23': 'Cabo Rojo', '25': 'Caguas', '27': 'Camuy', '29': 'Canovanas',
    '31': 'Carolina', '33': 'Catano', '35': 'Cayey', '37': 'Ceiba', '39': 'Ciales',
    '41': 'Cidra', '43': 'Coamo', '45': 'Comerio', '47': 'Corozal', '49': 'Culebra',
    '51': 'Dorado', '53': 'Fajardo', '54': 'Florida', '55': 'Guanica', '57': 'Guayama',
    '59': 'Guayanilla', '61': 'Guaynabo', '63': 'Gurabo', '65': 'Hatillo', '67': 'Hormigueros',
    '69': 'Humacao', '71': 'Isabela', '73': 'Jayuya', '75': 'Juana Diaz', '77': 'Juncos',
    '79': 'Lajas', '81': 'Lares', '83': 'Las Marias', '85': 'Las Piedras', '87': 'Loiza',
    '89': 'Luquillo', '91': 'Manati', '93': 'Maricao', '95': 'Maunabo', '97': 'Mayaguez',
    '99': 'Moca', '101': 'Morovis', '103': 'Naguabo', '105': 'Naranjito', '107': 'Orocovis',
    '109': 'Patillas', '111': 'Penuelas', '113': 'Ponce', '115': 'Quebradillas', '117': 'Rincon',
    '119': 'Rio Grande', '121': 'Sabana Grande', '123': 'Salinas', '125': 'San German', '127': 'San Juan',
    '129': 'San Lorenzo', '131': 'San Sebastian', '133': 'Santa Isabel', '135': 'Toa Alta', '137': 'Toa Baja',
    '139': 'Trujillo Alto', '141': 'Utuado', '143': 'Vega Alta', '145': 'Vega Baja', '147': 'Vieques',
    '149': 'Villaba', '151': 'Yabucoa', '153': 'Yauco', '999': 'Statewide'
    }


    # Replace the code with its corresponding town
    return df[column].map(lambda x: puerto_rico_regions.get(str(x), x))


