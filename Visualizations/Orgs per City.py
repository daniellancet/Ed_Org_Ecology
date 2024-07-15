import pandas as pd ## import Pandas, Python's official data analysis software
import seaborn as sns
import matplotlib
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\Task 0 - Setup\New Data\2224 Edited.csv") ## store the 2019 educational nonprofit tax data in my computer file in "df"

df['f990_org_addr_city'] = df['f990_org_addr_city'].apply(lambda x: str(x).title()) ## standardize capitalization of cities, so that we can use groupby -- otherwise "California" and "california" will be in different groups
df['f990_org_addr_state'] = df['f990_org_addr_state'].apply(lambda x: str(x).upper()) ## capitalizes states column

df = df.groupby(['f990_org_addr_city', 'f990_org_addr_state']).size().reset_index(name = "Educational Nonprofits") ## group by city and state, counting instances of "CA" and "Los Angeles" appearing together for example

df = df.sort_values(by='Educational Nonprofits', ascending = False) ## sort locations by number of educational nonprofits within it

df['city'] = df['f990_org_addr_city'] + ', ' + df['f990_org_addr_state'] ## combine city and state names to make labels of graph, for example "Berkeley, CA"

df = df.head(30) ## keep only the top 30 rows for aesthetic reasons

solid_muted_palette = sns.color_palette('muted', n_colors=1) ## prevent there being a gradient in the graph from dark blue to white; only 1 color allowed
sns.barplot(x='Educational Nonprofits', y='city', data=df, orient='h', palette=solid_muted_palette) ## create barplot, orient horizontally, use palette created earlier
matplotlib.pyplot.tight_layout()
sns.despine(top=True, right=True)
matplotlib.pyplot.show() ## show the plot created

