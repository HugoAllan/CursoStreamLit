import streamlit as st
import pandas as pd


def dataframes():
    st.title("DataFrames")
    st.write("This is the DataFrames page.")
    
    # Example DataFrame
    data = {
        'Column 1': [1, 2, 3],
        'Column 2': ['A', 'B', 'C'],
        'Column 3': [True, False, True]
    }
    
    df = pd.DataFrame(data)
    
    st.dataframe(df)  # Display the DataFrame