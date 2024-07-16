import pandas as pd
df = pd.read_csv(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 1\Sankey\00 NTEE Codes - Sheet1.csv")

df_Main_Category = df.groupby("Main_Category").agg({'count': 'sum', 'Broader Code': 'first', 'Broadest Code': 'first'}).reset_index()
df_Broader_Code = df.groupby("Broader Code").agg({'count': 'sum', 'Main_Category': 'first', 'Broadest Code': 'first'}).reset_index()
df_Broadest_Code = df.groupby("Broadest Code").agg({'count': 'sum', 'Main_Category': 'first', 'Broader Code': 'first'}).reset_index()

scholarship_index = df_Main_Category[df_Main_Category['Main_Category'] == 'Scholarship'].index[0]
fundraising_index = df_Main_Category[df_Main_Category['Main_Category'] == 'Fundraising'].index[0]

df_Main_Category.iloc[scholarship_index], df_Main_Category.iloc[fundraising_index] = df_Main_Category.iloc[fundraising_index].copy(), df_Main_Category.iloc[scholarship_index].copy()
labels = list(df_Main_Category['Main_Category'])
labels.extend(df_Broader_Code['Broader Code'])
labels.extend(df_Broadest_Code['Broadest Code'])

source = list(range(0, len(df_Main_Category['Main_Category']) + len(df_Broader_Code['Broader Code'])))

target_names = list(df_Main_Category['Main_Category'])
target_names.extend(df_Broader_Code['Broader Code'])
target_names.extend(df_Broadest_Code['Broadest Code'])

def find_index_main_categories(row): 
    for i in range(len(df_Main_Category['Main_Category']), len(df_Main_Category['Main_Category']) + len(df_Broader_Code['Broader Code'])):
        if target_names[i] == row['Broader Code']:
            return i 

df_Main_Category['target_main'] = df_Main_Category.apply(find_index_main_categories, axis=1)

def find_index_broader_categories(row): 
    for i in range(len(df_Main_Category['Main_Category']) + len(df_Broader_Code['Broader Code']), len(target_names)):
        if target_names[i] == row['Broadest Code']:
            return i 

df_Broader_Code['target_broader'] = df_Broader_Code.apply(find_index_broader_categories, axis=1)

values = list(df_Main_Category['count'])
values.extend(df_Broader_Code['count'])
target = list(df_Main_Category['target_main']) + list(df_Broader_Code['target_broader'])
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 10,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels
    ),
    link = dict(
      source = source, 
      target = target,
      value = values
  ))])

fig.update_layout(
    title_text="Educational Nonprofits Flowmap", 
    font_size=10,
    width=800,  
    height=800  
)

fig.write_html(r"C:\2024-2025 Berkeley\Extracurriculars\Ed&Orgs Lab\Summer\CSAE Figures Code\Panel 1\Sankey\sankey_diagram_Main_Categories.html")