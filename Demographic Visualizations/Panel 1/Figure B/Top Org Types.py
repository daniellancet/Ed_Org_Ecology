import pandas as pd
import seaborn as sns
import matplotlib
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")

matplotlib.pyplot.figure(figsize=(15, 8))
df = df.groupby('Main_Category').size().reset_index(name='Educational Nonprofits')
df = df.sort_values('Educational Nonprofits', ascending=False)

solid_muted_palette = sns.color_palette('muted', n_colors=1)
sns.barplot(x='Educational Nonprofits', y='Main_Category', data=df, palette=solid_muted_palette) 
sns.despine(right=True, top=True) 
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 1\Figure B\Main Category Distribution.png') ## show the plot created

