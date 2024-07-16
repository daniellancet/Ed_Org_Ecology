import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")

listy = ['B94', 'B82', 'B11', 'B83', 'B90', 'Other']

df2 = pd.DataFrame()
max_length = 0

for item in listy:
    if item != 'Other':
        selected_df = df[df['ntee_irs'] == item]
    else:
        selected_df = df[~df['ntee_irs'].isin(listy[:-1])]
    max_length = max(max_length, len(selected_df))

for item in listy:
    if item != 'Other':
        selected_df = df[df['ntee_irs'] == item]
    else:
        selected_df = df[~df['ntee_irs'].isin(listy[:-1])]

    column = pd.Series([0] * max_length)

    column[:len(selected_df)] = selected_df['ruleyear'].values

    df2[f'{item}'] = column

df2 = df2.reset_index(drop=True)

start_year = int(df['ruleyear'].min())
end_year = int(df['ruleyear'].max())
colormap = plt.cm.colors.ListedColormap(sns.color_palette('deep'))
ax = df2.plot.hist(bins=list(range(1900, end_year+1)), stacked=True, colormap=colormap)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper left')
plt.xlabel('Year')
plt.ylabel('Educational Nonprofits')
sns.despine(top=True, right=True)
plt.show()