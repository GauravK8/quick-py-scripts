import json
import pandas as pd

# Load via context manager and read_json() method
with open('~/in.json', 'r')as file:
    # load JSON data and parse into Dictionary object
    data = json.load(file)
# Load JSON as DataFrame 
df = pd.json_normalize(data)

print(df)

df.to_csv('~/csv-out/out.csv', encoding='utf-8', index=False)
