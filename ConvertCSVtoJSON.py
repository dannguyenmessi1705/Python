import pandas as pd

df = pd.read_csv('a.csv')
json_data = df.to_json(orient='records')
with open('f23.json', 'w') as f:
    f.write(json_data)
