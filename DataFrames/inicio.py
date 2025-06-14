import streamlit as st

# configuración de la página
st.set_page_config(
    page_title="Curso de Streamlit",
    page_icon=":guardsman:",
    # layout="wide",
    initial_sidebar_state="expanded"
)
# st.set_page_config(layout="wide")


st.title("Sección para el Manejo de Datos")

import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")

# Filtros interactivos
dias = st.multiselect("Selecciona los días", options=df["day"].unique(), default=df["day"].unique())

df_filtrado = df[df["day"].isin(dias)]

# Gráfico con tooltips (hover)
fig = px.box(
    df_filtrado,
    x="day",
    y="total_bill",
    color="sex",
    points="all",
    hover_data=["time", "smoker", "tip", "size"],
    title="Distribución interactiva de cuentas"
)

st.plotly_chart(fig, use_container_width=True)



import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd



df = sns.load_dataset("tips")

dias = st.multiselect("Selecciona días", df["day"].unique(), default=df["day"].unique())
df_filtrado = df[df["day"].isin(dias)]

fig = px.box(
    df_filtrado,
    x="day",
    y="total_bill",
    color="sex",
    points="all",
    title="Distribución interactiva de cuentas",
    hover_data=["tip", "size", "smoker"]
)

fig.update_layout(
    title_x=0.5,  # centrar título
    plot_bgcolor='rgba(245, 245, 245, 1)',
    paper_bgcolor='rgba(245, 245, 245, 1)',
    margin=dict(t=50, b=40),
    font=dict(family="Arial", size=14)
)

# Centrado con columnas
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.plotly_chart(fig, use_container_width=True)