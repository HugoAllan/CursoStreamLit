import streamlit as st
from charts import charts
from dataframes import dataframes
from tables import tables


with st.sidebar:
    st.title("Navigation")
    page = st.selectbox("Go to", ["DataFrames", "Charts", "Tables"])

if page == "DataFrames":
    dataframes()
elif page == "Charts":
    charts()
elif page == "Tables":
    tables()
