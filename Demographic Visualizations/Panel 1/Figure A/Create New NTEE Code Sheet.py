import pandas as pd
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")

df = df[['ntee_irs', 'Main_Category', 'Broader Code', 'Broadest Code']]
grouped_df = df.groupby('ntee_irs').agg({
    'Main_Category': 'first',
    'Broader Code': 'first',
    'Broadest Code': 'first'
}).reset_index()

count_df = df.groupby('ntee_irs').size().reset_index(name='count')

final_df = pd.merge(grouped_df, count_df, on='ntee_irs', how='inner')

final_df = final_df.dropna()

final_df.to_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 1\Sankey\00 NTEE Codes - Sheet1.csv")