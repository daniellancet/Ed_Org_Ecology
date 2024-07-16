import pandas as pd

df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\Task 0 - Setup\New Data\Daniels Data.csv")

df_all = df.groupby("ruleyear").size().reset_index(name="Nonprofits")

df_all = df_all.sort_values("ruleyear")

df_all = df_all[['ruleyear', 'Nonprofits']]


df_PTGs = df[df['Main Category'] == 'Parent-Teacher Groups']

df_PTGs = df_PTGs.groupby("ruleyear").size().reset_index(name="Parent-Teacher Groups")

df_PTGs = df_PTGs.sort_values("ruleyear")

df_PTGs = df_PTGs[['ruleyear', 'Parent-Teacher Groups']]



df_Scholarship = df[df['Main Category'] == 'Scholarship']

df_Scholarship = df_Scholarship.groupby("ruleyear").size().reset_index(name="Scholarship Orgs")

df_Scholarship = df_Scholarship.sort_values("ruleyear")

df_Scholarship = df_Scholarship[['ruleyear', 'Scholarship Orgs']]



df_single_support = df[df['Main Category'] == 'Single Support Fundraising']

df_single_support = df_single_support.groupby("ruleyear").size().reset_index(name="Single Support Fundraising Orgs")

df_single_support = df_single_support.sort_values("ruleyear")

df_single_support = df_single_support[['ruleyear', 'Single Support Fundraising Orgs']]


df_fraternities = df[df['Main Category'] == 'Fraternities']

df_fraternities = df_fraternities.groupby("ruleyear").size().reset_index(name="Fraternities")

df_fraternities = df_fraternities.sort_values("ruleyear")

df_fraternities = df_fraternities[['ruleyear', 'Fraternities']]


df_education_services = df[df['Main Category'] == 'Education Services']

df_education_services = df_education_services.groupby("ruleyear").size().reset_index(name="Education Service Orgs")

df_education_services = df_education_services.sort_values("ruleyear")

df_education_services = df_education_services[['ruleyear', 'Education Service Orgs']]


df_joined = pd.merge(left=df_all, right=df_PTGs, on='ruleyear', how='outer')

df_joined = pd.merge(left=df_joined, right=df_Scholarship, on='ruleyear', how='outer')

df_joined = pd.merge(left=df_joined, right=df_single_support, on='ruleyear', how='outer')

df_joined = pd.merge(left=df_joined, right=df_fraternities, on='ruleyear', how='outer')

df_joined = pd.merge(left=df_joined, right=df_education_services, on='ruleyear', how='outer')

df_joined = df_joined.fillna(0)

df_joined.to_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Data\Ruleyear and Nonprofits by Category.csv')