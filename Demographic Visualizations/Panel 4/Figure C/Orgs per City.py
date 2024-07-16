import pandas as pd 
import seaborn as sns
import matplotlib
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv") 

df['city'] = df['city'].apply(lambda x: str(x).title()) 
df['state'] = df['state'].apply(lambda x: str(x).upper()) 

df = df.groupby(['city', 'state']).size().reset_index(name = "Educational Nonprofits") 

df = df.sort_values(by='Educational Nonprofits', ascending = False) 

df['city'] = df['city'] + ', ' + df['state'] 

df = df.head(30) 

solid_muted_palette = sns.color_palette('muted', n_colors=1) 
sns.barplot(x='Educational Nonprofits', y='city', data=df, orient='h', palette=solid_muted_palette) 
matplotlib.pyplot.tight_layout()
sns.despine(top=True, right=True)
matplotlib.pyplot.show() 
