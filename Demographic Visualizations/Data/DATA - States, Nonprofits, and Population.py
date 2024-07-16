import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from adjustText import adjust_text

df = pd.read_csv(r"C:\Users\wlinc\Downloads\cleaned.csv")

df = df.groupby("state").size().reset_index(name="Educational Nonprofits")

df2 = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 3\Panel B\State Population 2023.csv")

df = pd.merge(df, df2, left_on="state", right_on="Abbreviation", how="inner")

df['Population'] = df['Population'].str.replace(',', '').astype(int)

df = df[['Abbreviation', 'Educational Nonprofits', 'Population']]

df = df.sort_values('Educational Nonprofits', ascending=False)

df.to_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 3\Panel B\DATA for State, Nonprofits, and Population.csv')