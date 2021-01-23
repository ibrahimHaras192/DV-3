import pandas as pd
import plotly.graph_objects as px
#which airline has the large amount of set per km?
'''
'airline', 'avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14'
       '''


df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")
df["diff"] = df['incidents_85_99'] + df['incidents_00_14']


plot = px.Figure(data=[px.Scatter(
	x= df['airline'],
	y=df['avail_seat_km_per_week'],
	mode='markers',
	#yaxis='airline',
	marker_color=df['diff'])
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
