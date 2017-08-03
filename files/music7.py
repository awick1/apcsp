import plotly.plotly as py
import plotly.graph_objs as go
import plotly 

import pandas as pd

plotly.tools.set_credentials_file(username='awick', api_key='xcuX3RMuqa79nPq0HFTB')


az=25.0
ca=316.0
wi=67.0

import os.path

#get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'bigdatafile.xlsx')

df=pd.read_excel(filename, "Sheet1")
table = pd.crosstab(df.genre, df.state, margins=True)

y1 = table['AZ']
y2 = table['CA']
y3 = table['WI']


for i in range(13):
    y1[i]=(y1[i]/az)*100
    
for i in range(13):
    y2[i]=(y2[i]/ca)*100

for i in range(13):
    y3[i]=(y3[i]/wi)*100
    


trace1 = go.Bar(
    x=["classical","country","gospel","heavy metal", "jazz", "pop", 
        "punk rock", "rap/hip hop", "reggae", "rhythm and blues", 
        "rock and roll", "techno electronic", "other",],
    y=y1,
    name='Arizona'
)
trace2 = go.Bar(
    x=["classical","country","gospel","heavy metal", "jazz", "pop", 
        "punk rock", "rap/hip hop", "reggae", "rhythm and blues", 
        "rock and roll", "techno electronic", "other"],
    y=y2,
    name='California'
)
trace3 = go.Bar(
    x=["classical","country","gospel","heavy metal", "jazz", "pop", 
        "punk rock", "rap/hip hop", "reggae", "rhythm and blues", 
        "rock and roll", "techno electronic", "other"],
    y=y3,
    name='Wisconsin'
)



data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='group',
    title='Music Genre Preferences by State',
    xaxis=dict(
        title='Music Genres',
        zeroline = True),
    yaxis=dict(
        title='Percent of People',
        zeroline = True)
)

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='styling-names')
py.iplot(fig, filename='grouped-bar')
