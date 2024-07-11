import pandas as pd
import seaborn as sns
import matplotlib
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\2224 Edited.csv")

matplotlib.pyplot.figure(figsize=(15, 8))
df = df.groupby('Main Category').size().reset_index(name='Educational Nonprofits')
df = df.sort_values('Educational Nonprofits', ascending=False)

solid_muted_palette = sns.color_palette('muted', n_colors=1) ## prevent there being a gradient in the graph from dark blue to white; only 1 color allowed
sns.barplot(x='Educational Nonprofits', y='Main Category', data=df, palette=solid_muted_palette) ## create barplot, use palette created earlier
sns.despine(right=True, top=True) 
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 1\Figure B\Main Category Distribution.png') ## show the plot created

