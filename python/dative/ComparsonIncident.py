#import packages
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
import pandas as pd
import plotly.graph_objects as go



#Which airline is developing and learning from mistakes?
#Which airline is safer?
#comperson incident 85 99

# user name and password for plotly account
#username ='Ibrahim19'
#api_key = 'FV0hzcNOk1z9U8wXOvNy'

#chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

#read CSV
df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

fig = go.Figure()

fig.add_trace(go.Scatter(x=df['airline'], y=df['incidents_85_99'],
                    mode='lines+markers',
                    name='incidents 1985-1999',
                         fill='tonexty'))

fig.add_trace(go.Scatter(x=df['airline'], y=df['incidents_00_14'],
                    mode='lines+markers',
                    name='incidents 2000-2014',
                         fill='tozeroy'))

fig.update_layout(title='comparson incident',
                   xaxis_title='airline',
                   yaxis_title='incidents')
fig.show()

#py.plot(fig, filename='Comperson incident', auto_open=True)
