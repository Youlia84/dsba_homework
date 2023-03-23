import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

data = pd.read_csv('calories_detail.csv')
st.title('Adjusted Food Availability in the Unites States 1970-2018')
st.sidebar.header("Pick a level of detail")

years = list(data['year'].drop_duplicates())
year_filter = st.sidebar.multiselect(
    'Choose year:', years, default=1970)

data = data[data['year'].isin(year_filter)]


food_dd = st.sidebar.selectbox("Select a food category:", data.select_dtypes(exclude=np.number).columns.tolist())
aggr_dd = st.sidebar.selectbox("Select an aggregation", ("Average","Total"))


graph = alt.Chart(data).mark_bar().encode(
    x=alt.X('mean(avg_per_capita_calories)',title='Average Per Capita Calories'),
    y=alt.Y(food_dd,title="Food",sort='-x')
)

graph2 = alt.Chart(data).mark_bar().encode(
    x=alt.X('sum(avg_per_capita_calories)',title='Total Per Capita Calories'),
    y=alt.Y(food_dd,title="Food",sort='-x')
)

if 'Average' in aggr_dd:
    st.altair_chart(graph, use_container_width=True) 
else: st.altair_chart(graph2, use_container_width=True) 



