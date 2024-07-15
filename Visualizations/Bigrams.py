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
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\Task 0 - Setup\New Data\2224 Edited.csv")
df['org_name_current'] = df['org_name_current'].astype(str)
df['org_name_sec'] = df['org_name_sec'].astype(str)

def combine_ordered_set(row):
    combined_list = []
    if pd.notnull(row['org_name_current']):
        combined_list += row['org_name_current'].split()
    if pd.notnull(row['org_name_sec']):
        combined_list += row['org_name_sec'].split()
    ordered_set = list(OrderedDict.fromkeys(combined_list))
    return ' '.join(ordered_set)

df['word cloud names'] = df.apply(combine_ordered_set, axis=1)

codes = ['Professional Association']
## ''  
##    'Professional Associations' 
##  , , 
##
## 'Single Support Fundraising' 'Parent-Teacher Groups' 'Scholarship' 'Fraternities' 'Education Services' 'Fundraising'

for code in codes:
    df2 = df[df['Main Category'] == code] ## filter rows with this code
    print(df2)

    def generate_bigrams(text):
        tokens = [word for word in word_tokenize(text) if word.lower() not in stop_words and word.isalpha()] ## turn strings into tokens, which can be read by nltk software
        bigrams = list(ngrams(tokens, 2)) ## make list of bigrams from created tokens
        return bigrams ## return this list

    def count_bigrams(text):
        bigrams = generate_bigrams(text) ## call the earlier function
        return Counter(bigrams) ## return a dictionary of counts for each word, something like ['Bunnies': 5, 'Carrots': 10]

    df2['bigram_counts'] = df2['word cloud names'].apply(lambda x: count_bigrams(x)) ## count bigrams for each row
    total_bigram_counts = sum(df2['bigram_counts'], Counter()) ## add the counts together for every row
    
    df2 = pd.DataFrame.from_dict(total_bigram_counts, orient='index').reset_index() ## turn count object into a pandas dataframe
    
    df2.columns = ['Bigram', 'Frequency'] ## set column names as 'bigram' and 'frequency'
    df2 = df2.sort_values(by='Frequency', ascending=False) ## sort by frequency
    df2['Bigram'] = df2['Bigram'].apply(lambda x: x[0] + ' ' + x[1]) ## only show the word, not "()"

    ## plt.figure(figsize=(7.4, 7.3)) ## expand the graph, so that labels are not clumped together

    sns.barplot(data=df2.head(30), x='Frequency', y='Bigram', orient='h', palette=sns.color_palette('muted', n_colors=1)) ## plot horizontal barplot of top 50 and bottom 50 bigrams

    plt.xlabel('Frequency') ## label the x axis as frequency
    plt.ylabel('Bigram') ## label the y axis as bigram

    plt.tight_layout() ## prevent labels being cut off

    sns.despine(top=True, right=True)

    df2.to_csv(rf'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 2\Data\{code} Bigrams.csv', index=False) ## first off, save the data to a csv file
    plt.savefig(rf'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 2\Graphs\{code} Bigrams.png') ## then, save the figure we graphed
    plt.close() 

