import pandas as pd
import plotly.express as px

df = pd.read_csv("Class 103 Project data.csv")
fig = px.scatter(df, x = "date", y = "cases", color = "country")
fig.show()