import pandas as pd

df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\Task 0 - Setup\New Data\Daniels Data.csv")

df = df.groupby('Main_Category').size().reset_index(name='Number of Nonprofits')

df = df[['Main_Category', 'Number of Nonprofits']]

df = df.sort_values('Number of Nonprofits', ascending=False)

df.to_csv(r'C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Data\Number of Nonprofits per Category.csv')