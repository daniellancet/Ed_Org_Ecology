import pandas as pd 
import seaborn as sns
import matplotlib
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\2224 Edited.csv") 

df['f990_org_addr_state'] = df['f990_org_addr_state'].apply(lambda x: str(x).upper()) 

df = df.groupby(['f990_org_addr_state']).size().reset_index(name = "Educational Nonprofits") 

df = df.sort_values(by='Educational Nonprofits', ascending = False) 

df = df.head(51)

df['State'] = df['f990_org_addr_state']

matplotlib.pyplot.figure(figsize=(10, 8))

solid_muted_palette = sns.color_palette('muted', n_colors=1) 
sns.barplot(x='Educational Nonprofits', y='State', data=df, orient='h', palette=solid_muted_palette) 
sns.despine(top=True, right=True)
matplotlib.pyplot.savefig(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 2\Panel A\Nonprofits per State.png')
