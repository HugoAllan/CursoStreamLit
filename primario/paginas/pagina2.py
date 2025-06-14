import streamlit as st

st.title("Página 2")

if "id" in st.session_state:
    st.write(f"ID recibido: {st.session_state.id}")
else:
    st.write("No se ha recibido ningún ID")