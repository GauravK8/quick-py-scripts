import pandas as pd

with open('~/in.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('~/csv-out/csvfile.csv', encoding='utf-8', index=False)
