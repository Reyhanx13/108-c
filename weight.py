import plotly.figure_factory as ff
import pandas as pd
import csv 

df=pd.read_csv("master.csv")

fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["weight"],show_hist=False)
fig.show()