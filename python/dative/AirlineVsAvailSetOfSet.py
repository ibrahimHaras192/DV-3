import pandas as pd
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as px
#which airline has the large amount of set per km?
'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''
#username ='Ibrahim19'
#api_key = 'FV0hzcNOk1z9U8wXOvNy'

#chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")

df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")
df["diff"] = df['incidents_85_99'] + df['incidents_00_14']


plot = px.Figure(data=[px.Scatter(
	x= df['airline'],
	y=df['avail_seat_km_per_week'],
	mode='markers',
	#yaxis='airline',
	)
])

# Add dropdown
plot.update_layout(
	title='Explore the data',
	xaxis_title='airline',
	yaxis_title='avail seat km per week',
	updatemenus=[
		dict(
			buttons=list([
				dict(
					args=["type", "scatter"],
					label="Scatter Plot",
					method="restyle"
				),
				dict(
					args=["type", "bar"],
					label="Bar Chart",
					method="restyle"
				)
			]),
			direction="down",
		),
	]
)

plot.update_layout(
	updatemenus=[
		dict(
			buttons=list([
				dict(
					args=["type", "scatter"],
					label="Scatter Plot",
					method="restyle"
				),
				dict(
					args=["type", "bar"],
					label="Bar Chart",
					method="restyle"
				)
			]),
			direction="down",
		),
	]
)

plot.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
plot.show()

#py.plot(plot, filename='Airline vs avail seat km per week', auto_open=True)


