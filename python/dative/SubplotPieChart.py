import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import chart_studio
import chart_studio
import chart_studio.plotly as py


username ='Ibrahim19'
api_key = 'FV0hzcNOk1z9U8wXOvNy'

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

# Read CSV
df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

# Lebals and value for the first pie chart
labels = ['incident 1985-1999', 'fatal_accidents_85_99']
values = [df['incidents_85_99'].sum(),df['fatal_accidents_85_99'].sum()]

# Lebals and value for the second pie chart
labels1 = ['incident 2000-2014', 'fatal_accidents_00_14']
values1 = [df['incidents_00_14'].sum(),df['fatal_accidents_00_14'].sum()]


fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['1985-1999', '2000-2014'])
fig.add_trace(go.Pie(labels=labels, values=values, scalegroup='one',
                     name="Airline safety"), 1, 1)
fig.add_trace(go.Pie(labels=labels1, values=values1, scalegroup='one',
                     name="Airline safety"), 1, 2)

fig.update_layout(title_text='number of fatal accidents comparing with number of incident')
fig.show()

py.plot(fig, filename='general Incidents compared to Fatal accidents by period', auto_open=True)