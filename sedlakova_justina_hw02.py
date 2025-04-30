import pandas as pd

df = pd.read_csv('/Users/justinasedlakova/Desktop/datová analýza akademie/HW2/netflix_titles.tsv', sep='\t')
df = df[['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']]

def to_list(value):

    if pd.isna(value):
        return []
    raw_items = value.split(',')

    cleaned_items = []
    for item in raw_items:
        item = item.strip()
        if item:  
            cleaned_items.append(item)

    return cleaned_items

def calculate_decade(year):
    if year == '' or year is None:
        return None

    year = int(year)  
    decade = (year // 10) * 10  
    return decade


records = []
for index, row in df.iterrows():
    record = {
        "title": row['PRIMARYTITLE'],
        "directors": to_list(row['DIRECTOR']),
        "cast": to_list(row['CAST']),
        "genres": to_list(row['GENRES']),
        "decade": calculate_decade(row['STARTYEAR'])
    }
    records.append(record)
import json

with open('hw02_output.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
