import streamlit as st
import pandas as pd
import io

def tables():
    st.title("Tablas")
    st.write("Esta es la página de tablas.")
    
    # carga de archivo CSV
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Mostrar las primeras filas del DataFrame
        st.subheader("Primeras Filas del Archivo")
        st.dataframe(df.head())  # Mostrar el DataFrame cargado
        
        # Seleccionar filas para mostrar
        num_rows = st.slider("Selecciona el número de filas a mostrar", min_value=1, max_value=len(df), value=0, step=100)
        st.subheader(f"Primeras {num_rows} Filas del Archivo")
        st.dataframe(df.head(num_rows))
        
        # Eliminar columnas seleccionadas
        columns_to_drop = st.multiselect("Selecciona columnas para eliminar", options=df.columns.tolist())
        if columns_to_drop:
            df = df.drop(columns=columns_to_drop)
            st.success(f"Columnas eliminadas: {', '.join(columns_to_drop)}")
        else:
            st.info("No se han seleccionado columnas para eliminar.")
        # Mostrar el DataFrame actualizado
        st.subheader("DataFrame Actualizado")
        st.dataframe(df)

        # Mostrar información del DataFrame
        st.subheader("Información de la Data")
        info_df = pd.DataFrame({
            "Columna": df.columns,
            "Tipo de Dato": [str(df[col].dtype) for col in df.columns],
            "Valores Nulos": [df[col].isnull().sum() for col in df.columns],
            "Valores Únicos": [df[col].nunique() for col in df.columns] 
        })
        st.dataframe(info_df)

    else:
        st.warning("Por favor, carga un archivo CSV para ver las tablas.")
