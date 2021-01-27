from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objects as go
# Stack two subplots vertically, and add a scatter trace to each
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import chart_studio
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.graph_objects as px
import plotly.express as px
'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''

username ='Ibrahim19'
api_key = 'FV0hzcNOk1z9U8wXOvNy'

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

fig = make_subplots(rows=2, shared_yaxes=True)

fig.add_scatter(x=df['incidents_85_99'], y=df['fatal_accidents_85_99'], row=1, col=1, mode="markers",name='1985-1999')

fig.add_scatter(x= df['incidents_00_14'], y=df['fatal_accidents_00_14'], row=2, col=1, mode="markers", name='2000-2014')

fig.update_layout(title_text='general Incidents compared to Fatal accidents by period')

fig.show()

py.plot(fig, filename='general Incidents compared to Fatal accidents by period', auto_open=True)

