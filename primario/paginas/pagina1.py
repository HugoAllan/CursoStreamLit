import streamlit as st

st.title("Página 1")

if st.button("Ir a pagina 2"):
    st.switch_page("paginas/pagina2.py")
    
enviarID = st.text_input("Enviar ID")

submit = st.button("Enviar ID")
if submit:
    st.session_state.id = enviarID
    st.switch_page("paginas/pagina2.py")