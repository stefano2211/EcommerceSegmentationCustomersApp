import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import plotly.graph_objects as go
import random
import pandas as pd
from funtions.funtions import *

data = pd.read_csv('Dataset/DataCluster.csv')

numeric_columns = show_numeric_columns()
string_columns = show_string_columns()





cluster = st.selectbox(
    'Choose Cluster',
    ('0', '1', 'Combined'), key=3)


fill_cluster = filter_cluster(dataframe=data, cluster=cluster)
pie_cluster = PiePlotCategorical(dataframe=data, cluster=cluster)



col1, col2, col3 = st.columns(3)
col1.metric(label="Cash Amount", value=round(cardsCashAmount(dataframe=data, cluster=cluster),2))
col2.metric(label="Day Since Last Order", value=round(daysincelastorder(dataframe=data, cluster=cluster),2))
col3.metric(label="Order Count", value=round(OrderCount(dataframe=data, cluster=cluster),2))
style_metric_cards(background_color='#0E1117', border_color="#0E1117", border_left_color='#F6955F')

st.title('Cluster Scatter Plot')
c1, c2 =  st.columns((2))
with c1:
    X_axis = st.selectbox(
    'Choose X axis',
    numeric_columns)

    
with c2:
    Y_axis = st.selectbox(
    'Choose Y axis',
    numeric_columns)

               
fig = px.scatter(fill_cluster, x=fill_cluster[X_axis], y=fill_cluster[Y_axis], color=fill_cluster['Cluster'])
fig.update_traces(marker_size=10)
fig.update_layout(scattermode="group")
st.plotly_chart(fig, use_container_width=True)

st.title('Cluster Bar Plot')
X_axis = st.selectbox(
    'Choose Columns',
    string_columns, key=2)

bar_plot = BarPlotCategorical(dataframe=data, cluster=cluster, column=X_axis) 
fig = px.bar(bar_plot)
st.plotly_chart(fig, use_container_width=True)

st.title('Cluster Pie Plot')

fig = px.bar(pie_cluster)
st.plotly_chart(fig, use_container_width=True)








