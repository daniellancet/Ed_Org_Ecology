import pandas as pd
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")

def label_row(row):
    if row['Main_Category'] in (['Advocacy', 'Research']):
        return 'Research/Advocacy'
    if row['Main_Category'] in (['Technical Assistance', 'Student Services', 'Education Services', 'Remedial Reading']):
        return 'School Support'
    if row['Main_Category'] in (['Professional Association', 'Fraternities', 'Alumni Association']):
        return 'Association'
    if row['Main_Category'] in (['Single Support Fundraising', 'Fundraising']):
        return 'Fundraising'
    if row['Main_Category'] in (['Support NEC', 'Not Elsewhere Classified']):
        return 'Not Elsewhere Classified'
    if row['Main_Category'] in (['K-12 Schools', 'Preschools', 'Elementary Schools', 'High Schools', 'Special Education', 'Charter Schools']):
        return 'P-12 Schools'
    if row['Main_Category'] in (['Vocational Schools', 'Higher Education', 'Two-Year Colleges', 'Undergraduate Colleges', 'Universities', 'Graduate and Professional Schools', 'Adult Education']):
        return 'Postsecondary'
    if row['Main_Category'] in (['Libraries']): 
        return 'Libraries'
    if row['Main_Category'] in (['Scholarship']): 
        return 'Scholarship'
    if row['Main_Category'] in (['Parent Teacher Groups']): 
        return 'Parent Teacher Groups'
    
df['Broader Code'] = df.apply(label_row, axis=1)
df.to_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\New Data\Daniels Data.csv")
