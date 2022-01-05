import pandas as pd
import plotly.express as px
df = pd.read_csv("Copy+of+data+-+data.csv")
#for linegraph
#fig = px.line(df,x="Population",y="InternetUsers",color="Country",title="Per capita income")
#for bar Graph
fig = px.bar(df,x = "country",y = "cases")
#for scatter Graph
#fig = px.scatter(df,x = "Year",y = "Per capita income",color="Country",title ="Per capita income")
fig.show()