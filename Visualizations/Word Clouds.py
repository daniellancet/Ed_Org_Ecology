import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
codes = ['Parent-Teacher Groups', 'Scholarship', 'Fraternities', 'Education Services', 'Fundraising', 'Professional Association', 'Single Support Fundraising']
for code in codes: 
    df = pd.read_csv(rf'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 2\Data\{code} Bigrams.csv')

    df['Bigram'] = df['Bigram'].astype(str)
    df['Frequency'] = df['Frequency'].astype(int)

    bigram_dict = dict(zip(df['Bigram'], df['Frequency']))

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(bigram_dict)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    plt.savefig(rf'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 2\Word Clouds\{code} Wordcloud.png') ## then, save the figure we graphed
    plt.close() 