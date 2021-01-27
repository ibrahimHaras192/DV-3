import pandas as pd
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as px
import plotly.express as px
#which airline is the safest copmaring with seat km per week?
'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''
#username ='Ibrahim19'
#api_key = 'FV0hzcNOk1z9U8wXOvNy'

#chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")


df["fatalities"] = df['fatalities_85_99'] + df['fatalities_00_14']
#print(df[['incidents_85_99','incidents_00_14']].head())
#print(df['diff'].head())
#print(df.nsmallest(10,'diff', keep="all"))


fig = px.scatter(data_frame=df,x=df['airline'], y=df['avail_seat_km_per_week'], size=df['fatalities'], color= 'fatalities', title= '')

fig.update_layout(legend_traceorder="reversed")
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

fig.show()

#py.plot(fig, filename='which airline is the safest copmaring with seat km per week', auto_open=True)
