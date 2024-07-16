import pandas as pd
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")

print(df.shape)
def label_row(row):
    if row['Broader Code'] in (['Research/Advocacy', 'School Support', 'Fundraising', 'Scholarship']):
        return 'School Improvement Org'
    if row['Broader Code'] in (['Association', 'Parent Teacher Groups']):
        return 'Associational Org'
    if row['Broader Code'] in (['Not Elsewhere Classified']):
        return 'Not Elsewhere Classified'
    if row['Broader Code'] in (['P-12 Schools', 'Postsecondary', 'Libraries']):
        return 'Educational Institutions'
    
df['Broadest Code'] = df.apply(label_row, axis=1)
print(df[df['Broadest Code'].isnull()])
print(df.shape)
df.to_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")