import pandas as pd
import nltk
import seaborn as sns
import matplotlib.pyplot as plt
from nltk import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
from collections import OrderedDict
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
stop_words.add('nan')
stop_words.add('the')
stop_words.add('of')
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")
df['name'] = df['name'].astype(str)
df['org_name_sec'] = df['org_name_sec'].astype(str)

def combine_ordered_set(row):
    combined_list = []
    if pd.notnull(row['name']):
        combined_list += row['name'].split()
    if pd.notnull(row['org_name_sec']):
        combined_list += row['org_name_sec'].split()
    ordered_set = list(OrderedDict.fromkeys(combined_list))
    return ' '.join(ordered_set)

df['word cloud names'] = df.apply(combine_ordered_set, axis=1)

codes = ['Parent Teacher Groups', 'Scholarship', 'Fraternities', 'Education Services', 'Fundraising']

for code in codes:
    df2 = df[df['Main_Category'] == code]

    def generate_bigrams(text):
        tokens = [word for word in word_tokenize(text) if word.lower() not in stop_words and word.isalpha()] 
        bigrams = list(ngrams(tokens, 2)) 
        return bigrams 

    def count_bigrams(text):
        bigrams = generate_bigrams(text) 
        return Counter(bigrams) 
    
    df2['bigram_counts'] = df2['word cloud names'].apply(lambda x: count_bigrams(x)) 
    total_bigram_counts = sum(df2['bigram_counts'], Counter()) 
    
    df2 = pd.DataFrame.from_dict(total_bigram_counts, orient='index').reset_index() 
    
    df2.columns = ['Bigram', 'Frequency'] 
    df2 = df2.sort_values(by='Frequency', ascending=False) 
    df2['Bigram'] = df2['Bigram'].apply(lambda x: x[0] + ' ' + x[1]) 

   
    sns.barplot(data=df2.head(30), x='Frequency', y='Bigram', orient='h', palette=sns.color_palette('muted', n_colors=1)) 

    plt.xlabel('Frequency')
    plt.ylabel('Bigram') 

    plt.tight_layout() 

    sns.despine(top=True, right=True)

    df2.to_csv(rf'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 2\Data\{code} Bigrams.csv', index=False) ## first off, save the data to a csv file
    plt.savefig(rf'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 2\Bigrams\{code} Bigrams.png') ## then, save the figure we graphed
    plt.close() 

