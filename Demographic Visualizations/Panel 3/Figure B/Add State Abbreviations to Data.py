import pandas as pd
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 3\Panel B\State Population 2023.csv")
df2 = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\States, Abbreviations, Population, and Educational Nonprofit Count.csv")

df2 = df2[['State', 'Abbreviation']]
merged_df = pd.merge(df, df2, left_on='State', right_on='State', how='inner')

print(merged_df)

merged_df.to_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 3\Panel B\State Population 2023.csv")

