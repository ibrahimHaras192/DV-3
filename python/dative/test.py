from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objects as go
# Stack two subplots vertically, and add a scatter trace to each
from plotly.subplots import make_subplots
import plotly.graph_objects as go
'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''


df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")
'''
fig = make_subplots(rows=2, shared_yaxes=True)

fig.add_scatter(x=df['incidents_85_99'], y=df['fatal_accidents_85_99'], row=1, col=1, mode="markers",name='1985-1999',labels={
                     'incidents_85_99': "Sepal Length (cm)",
                     'fatal_accidents_85_99': "Sepal Width (cm)"})

fig.add_scatter(x= df['incidents_00_14'], y=df['fatal_accidents_00_14'], row=2, col=1, mode="markers", name='2000-2014')

fig.show()
'''
# two subplots, each in a row, forming one column
fig = make_subplots(rows=2, cols=1) # sharing the x axis.

fig.append_trace(go.Scatter(x = df['incidents_85_99'], y=df['fatal_accidents_85_99'], name='1985-1999',mode="markers",
                            labels=dict(incidents_85_99="Total Bill ($)")), 1,1)
fig.append_trace(go.Scatter(x =df['incidents_00_14'], y = df['fatal_accidents_00_14'], name='2000-2014',mode="markers"), 2, 1)
fig.update_layout(title='Styled Scatter',xaxis=dict(title="X Label"),yaxis=dict(title="Y label"),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.show()