import pandas as pd

df = pd.read_csv(r'~/csv-files/test.csv', sep=',', low_memory=False) # .count()

df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
# df['created_at'].groupby([df['created_at'].dt.year, df['created_at'].dt.month]).agg('count')

grouped = df.groupby(df["created_at"].dt.strftime("%Y-%m")).agg('count')
print(grouped)

grouped.to_csv(r'~/csv-out/test.csv', encoding='utf-8')


# df.groupby(df["created_at"].dt.strftime("%Y-%m")).agg('count').to_csv(r'~/csv-out/test.csv', encoding='utf-8', index=False)

# df.to_csv(r'~/csv-out/test.csv', encoding='utf-8', index=False)
# print(df['created_at'].groupby([df['created_at'].dt.year, df['created_at'].dt.month]).agg('count'))
# print(df)
# df.to_csv(r'~/csv-out/test.csv', encoding='utf-8', index=False)
