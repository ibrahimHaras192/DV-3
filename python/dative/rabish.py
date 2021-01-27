import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''
labels = ['incident 1985-1999', 'fatal_accidents_85_99']
values = [df['incidents_85_99'].sum(),df['fatal_accidents_85_99'].sum()]

labels1 = ['incident 2000-2014', 'fatal_accidents_00_14']
values1 = [df['incidents_00_14'].sum(),df['fatal_accidents_00_14'].sum()]





fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['1985-1999', '2000-2014'])
fig.add_trace(go.Pie(labels=labels, values=values, scalegroup='one',
                     name="Airline safety"), 1, 1)
fig.add_trace(go.Pie(labels=labels1, values=values1, scalegroup='one',
                     name="Airline safety"), 1, 2)

fig.update_layout(title_text='number of fatal accidents comparing with ')
fig.show()