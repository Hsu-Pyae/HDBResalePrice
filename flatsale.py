import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('HDDclean.csv')
st.set_page_config(page_title='HDB Resale Price Dashboard',page_icon=':bar_chart:',layout='wide')
st.sidebar.header('Please Filter Here')
flat_type = st.sidebar.multiselect(
    'Select Flat Types',
    options = df['flat_type'].unique(),
    default = df['flat_type'].unique()[:5]
)
town_name = st.sidebar.multiselect(
    'Select Town',
    options = df['town'].unique(),
    default = df['town'].unique()[:5]
)
year_name = st.sidebar.multiselect(
    'Select Year',
    options = df['year'].unique(),
    default = df['year'].unique()[:5]
)

st.subheader(':bar_chart: HDB Resale Price Dashboard')
st.markdown('##')
lowest = df['resale_price'].min()
highest = df['resale_price'].max()
median = df['resale_price'].median()
col1,col2,col3 = st.columns(3)
with col1:
    st.subheader('Lowest Price')
    st.subheader(f'SG $ {lowest}')
with col2:
    st.subheader('Highest Price')
    st.subheader(f' SG $ {highest}')
with col3:
    st.subheader('Median Price')
    st.subheader(f'SG $ {median}')

df_select = df.query('flat_type == @flat_type and town == @town_name and year == @year_name')

aa = df_select.groupby('flat_type')['resale_price'].mean().sort_values()
fig_resaleprice_by_flattype = px.bar(
    aa,
    x=aa.values,
    y=aa.index,
    title = 'Resale Prices by Flat Type '
)
a,b, = st.columns(2)
a.plotly_chart(fig_resaleprice_by_flattype,use_container_width=True)

bb = df_select.groupby('town')['resale_price'].mean().sort_values()
fig_resale_price_by_town = px.line(
    bb,
    x=bb.values,
    y=bb.index,
    title = 'Resale Prices by Town'
)
b.plotly_chart(fig_resale_price_by_town,use_container_width=True)

c,d= st.columns(2)
fig_resale_price_by_town_and_flattype = px.density_heatmap(
    df_select,
    x='town',
    y='flat_type',
    z='resale_price',
    histfunc='avg',
    title = 'Resale Prices by Town and Flat Type'
)
c.plotly_chart(fig_resale_price_by_town_and_flattype,use_container_width=True)

fig_resale_price_by_town_and_year = px.density_heatmap(
    df_select,
    x='town',
    y='year',
    z='resale_price',
    histfunc='avg',
    title = 'Resale Prices by Town and Year'
)
d.plotly_chart(fig_resale_price_by_town_and_year,use_container_width=True)