import pandas as pd

df = pd.read_csv(r"C:\Users\wlinc\Downloads\cleaned.csv")
df2 = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\Cleaned City Population Data.csv")
df = df.groupby(['city', 'state']).size().reset_index(name='Educational Nonprofits')

df = df[['city', 'state', 'Educational Nonprofits']]
df['city'] = df['city'].str.title()
df = df.sort_values('Educational Nonprofits', ascending=False)
print(df.head(5))
print(df2.head(5))
df = pd.merge(df, df2, left_on=['city', 'state'], right_on=['NAME', 'Abbreviation'], how='inner')
df = df.sort_values('POPESTIMATE2023', ascending=False)
print(df.head(30))
df = df[['NAME', 'STNAME', 'Abbreviation', 'POPESTIMATE2023', 'Educational Nonprofits']]
df = df.sort_values('Educational Nonprofits', ascending=False)
df.to_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\Nonprofit and Population Data Merged.csv')
