import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from adjustText import adjust_text

df = pd.read_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\Final Merge.csv')
df = df[['NAME', 'Abbreviation', 'Educational Nonprofits', 'POPESTIMATE2023']]
df = df.sort_values('Educational Nonprofits', ascending=False)
df.to_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\City, Nonprofits, and Population.csv')