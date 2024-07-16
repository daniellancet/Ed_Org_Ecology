import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from adjustText import adjust_text

df = pd.read_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\Nonprofit and Population Data Merged.csv')
df = df.head(25)

df['Log Population'] = df['POPESTIMATE2023'].apply(math.log)
df['Log Count'] = df['Educational Nonprofits'].apply(math.log)

plt.figure(figsize=(15, 10))

sns.regplot(x='Log Population', y='Log Count', data=df, ci=None, line_kws={'color': 'grey'})

texts = []
for i in range(len(df)):
    texts.append(plt.text(df['Log Population'][i], df['Log Count'][i], df['NAME'][i], fontsize=15))

adjust_text(texts, 
            arrowprops=dict(arrowstyle='-', color='gray', lw=0.5),
            only_move={'points': 'xy', 'texts': 'xy'},  
            autoalign='xy',
            force_text=3.0,  
            lim=100)  

plt.tight_layout()
sns.despine(top=True, right=True)

plt.show()