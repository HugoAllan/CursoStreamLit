import streamlit as st


# configuración de la página
st.set_page_config(
    page_title="Curso de Streamlit",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Inicio del Curso de Streamlit")
st.write("Bienvenido al curso de Streamlit. Aquí aprenderás a crear aplicaciones web interactivas con Python.")

# Definición de las páginas del menú lateral    
pages = {
    "Widgets Elements": [
        st.Page("paginas/widget.py", title="Widgets", icon=":material/add:"),
        st.Page("paginas/button.py", title="Botones", icon=":material/search:")
    ],
    "Textos": [
        st.Page("paginas/texto.py", title="Textos", icon=":material/book:")
    ],
    "Sesiones": [
        st.Page("paginas/session.py", title="Sesiones", icon=":material/done:"),
    ],
    "Formularios": [
        st.Page("paginas/formularios.py", title="Formularios", icon=":material/favorite:")
    ],
    "Config": [
        st.Page("paginas/pagina1.py", title="Pagina 1", icon=":material/favorite:"),
        st.Page("paginas/pagina2.py", title="Pagina 2", icon=":material/favorite:")
    ]
}

# Agregar las páginas al menú lateral
pg = st.navigation(
    pages=pages,
    position="sidebar",
    expanded=True
)
pg.run()