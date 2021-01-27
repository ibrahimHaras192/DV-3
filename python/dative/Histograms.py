import plotly.express as px
import pandas as pd

df = pd.read_csv("/Users/ibrahimharas/Documents/DV-3/dataset/airline-safety/airline-safety.csv")
fig = px.histogram(df, x="total_bill")
fig.show()