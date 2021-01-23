import pandas as pd
import plotly.graph_objects as go

#Which airline is developing and learning from mistakes?
#Which airline is safest?
'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''

df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

fig = go.Figure()

fig.add_trace(go.Scatter(x=df['airline'], y=df['incidents_85_99'],
                    mode='lines+markers',
                    name='incidents 1985-1999'))

fig.add_trace(go.Scatter(x=df['airline'], y=df['incidents_00_14'],
                    mode='lines+markers',
                    name='incidents 2000-2014'))

fig.update_layout(title='comparson incident',
                   xaxis_title='airline',
                   yaxis_title='incidents')
fig.show()
