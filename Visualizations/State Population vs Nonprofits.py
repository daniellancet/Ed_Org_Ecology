import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from adjustText import adjust_text


df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\Task 0 - Setup\New Data\2224 Edited.csv")

df = df.groupby("f990_org_addr_state").size().reset_index(name="Educational Nonprofits")

print(df)
df2 = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 3\Panel B\State Population 2023.csv")

df = pd.merge(df, df2, left_on="f990_org_addr_state", right_on="Abbreviation", how="inner")

df['Population'] = df['Population'].str.replace(',', '').astype(int)

df['Log Population'] = df['Population'].apply(math.log)
df['Log Count'] = df['Educational Nonprofits'].apply(math.log)

df.sort_values('Log Population', ascending=False)

plt.figure(figsize=(10, 7.6))
df = df.head(30)


sns.regplot(x='Log Population', y='Log Count', data=df, ci=None, line_kws={'color': 'grey'})


texts = []
for i in range(len(df)):
    texts.append(plt.text(df['Log Population'][i], df['Log Count'][i], df['Abbreviation'][i], fontsize=15))

adjust_text(texts, 
            arrowprops=dict(arrowstyle='-', color='gray', lw=0.5),
            only_move={'points': 'y', 'texts': 'y'},
            autoalign='y',
            force_text=0.05,  
            lim=2) 

plt.tight_layout()
sns.despine(top=True, right=True)


plt.show()