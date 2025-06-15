import streamlit as st
import pandas as pd


def charts():
    st.title("Charts")
    st.write("This is the charts page.")
    
    # Example data for a chart
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 15, 25]
    }
    
    df = pd.DataFrame(data)
    
    # Display a bar chart
    st.bar_chart(df.set_index('Category'))
    
    # Display a line chart
    st.line_chart(df.set_index('Category'))
    
    # Display a pie chart
    st.pyplot(df.plot.pie(y='Values', labels=df['Category'], autopct='%1.1f%%').get_figure())