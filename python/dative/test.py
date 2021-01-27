
#import packages
from plotly.subplots import make_subplots
import pandas as pd
import chart_studio
import chart_studio
import chart_studio.plotly as py

username ='Ibrahim19'
api_key = 'FV0hzcNOk1z9U8wXOvNy'

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

# Read CSV
df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

fig = make_subplots(rows=2, shared_yaxes=True)

# Stack two subplots vertically, and add a scatter trace to each
fig.add_scatter(x=df['incidents_85_99'], y=df['fatal_accidents_85_99'], row=1, col=1, mode="markers",name='1985-1999')

fig.add_scatter(x= df['incidents_00_14'], y=df['fatal_accidents_00_14'], row=2, col=1, mode="markers", name='2000-2014')

fig.update_layout(title_text='general Incidents compared to Fatal accidents by period')

fig.show()

py.plot(fig, filename='general Incidents compared to Fatal accidents by period', auto_open=True)

