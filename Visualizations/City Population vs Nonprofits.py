import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from adjustText import adjust_text

plt.figure(figsize=(5, 10))

df = pd.read_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 4\Figure D\Final Merge.csv')
df = df.head(25)

df['Log Population'] = df['POPESTIMATE2023'].apply(math.log)
df['Log Count'] = df['Educational Nonprofits'].apply(math.log)

sns.regplot(x='Log Population', y='Log Count', data=df, ci=None, scatter=False, line_kws={'color': 'grey'})

for i in range(len(df)):
    plt.annotate(df['NAME'][i], (df['Log Population'][i], df['Log Count'][i]), fontsize=15, ha='center', va='center')

plt.tight_layout()
sns.despine(top=True, right=True)

plt.show()