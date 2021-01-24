import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objects as px
import plotly.express as px
#which airline is the safest copmaring with seat km per week?
'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''


df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")


labels = ['incident 1985-1999','incident 2000-2014']
values = [df['incidents_85_99'].sum(),df['incidents_00_14'].sum()]

# pull is given as a fraction of the pie radius
fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.2])])

fig.update_layout(title_text='Comparison of incident in periods from 1985 to 2014')
fig.show()

print(list(range(1,10)))
