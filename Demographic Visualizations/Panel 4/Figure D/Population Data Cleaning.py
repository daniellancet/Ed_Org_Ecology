import pandas as pd
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\sub-est2023.csv", encoding='cp1252')
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df2 = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\States, Abbreviations, Population, and Educational Nonprofit Count.csv")
df2 = df2.applymap(lambda x: x.strip() if isinstance(x, str) else x)
def remove_last_word(text):
    return ' '.join(text.split()[:-1])


df['NAME'] = df['NAME'].str.title() 
df['STNAME'] = df['STNAME']
df = df[~df['NAME'].str.contains(r'\(.*?\)', regex=True)]
df = df[df['NAME'].str.contains('|'.join(['village', 'town', 'city']), case=False, na=False)] 

df['NAME'] = df['NAME'].apply(lambda x: remove_last_word(x) if any(word in x.lower() for word in ['village', 'town', 'city']) else x) 
df = df[['NAME', 'STNAME', 'POPESTIMATE2023']] 
df = df.sort_values('POPESTIMATE2023', ascending=False)
df = df.groupby(['NAME', 'STNAME']).first().reset_index() 
df2 = df2[['State', 'Abbreviation']] 

merged_df = pd.merge(df, df2, left_on='STNAME', right_on='State', how='inner')
merged_df = merged_df.sort_values("POPESTIMATE2023", ascending=False) 

merged_df = merged_df[['NAME', 'STNAME', 'Abbreviation', 'POPESTIMATE2023']] 
df_temp = merged_df[merged_df['NAME'].str.contains('New York', case=False)]
df_temp = df_temp[['NAME', 'STNAME', 'POPESTIMATE2023']]
print(df_temp)
merged_df.to_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\Cleaned City Population Data.csv")
