import streamlit as st


# configuración de la página
st.set_page_config(
    page_title="Curso de Streamlit",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# función para mostrar un mensaje de bienvenida como un H1
st.title("Bienvenido al curso de Streamlit")

st.header("¡Hola, soy un header!")
st.subheader("¡Hola, soy un subheader!")
st.caption("¡Hola, soy un caption!")
st.text("¡Hola, soy un texto!")


# Concatenación de cadenas
nombre = "Hugo"  
apellido = "Martinez, desde el curso de Streamlit"
st.text(f"Hola, {nombre} {apellido}")

# Markdown
st.markdown("## Este es un texto en **Markdown**")
st.markdown("**Este es un texto en negrita**")
# Texto en cursiva
st.markdown("*Este es un texto en cursiva*")
# Texto en código
st.markdown("`def mi_funcion():`")
# Texto con enlace
st.markdown("[Visita Streamlit](https://streamlit.io/)")
# Texto con lista
st.markdown("- Elemento de lista 1\n- Elemento de lista 2\n- Elemento de lista 3")  
# Texto con bloque de código
st.markdown("```python\nprint('Hola, mundo!')\n```")
# Texto con imagen
st.markdown("![Imagen de ejemplo](https://via.placeholder.com/150)")
# Texto con tabla
st.markdown("| Columna 1 | Columna 2 |\n| --- | --- |\n| Dato 1 | Dato 2 |\n| Dato 3 | Dato 4 |")   
# Texto con cita
st.markdown("> Esta es una cita en Markdown")   
# Texto con HTML
st.markdown("<h1>Este es un texto en HTML</h1>", unsafe_allow_html=True)
# Texto con emojis
st.markdown("¡Hola! :smile: :rocket: :heart:")
# Texto con enlaces con iconos
st.markdown("[Streamlit](https://streamlit.io/) :guardsman:")
# Texto con tablas
st.markdown("| Nombre | Edad |\n| --- | --- |\n| Hugo | 30 |\n| Maria | 25 |")



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Inicializar los estados la primera vez
if "mostrar_bienvenida" not in st.session_state:
    st.session_state.mostrar_bienvenida = False
if "mostrar_grafica" not in st.session_state:
    st.session_state.mostrar_grafica = False

# Botón A: Mensaje de bienvenida
if st.button("Mostrar bienvenida"):
    st.session_state.mostrar_bienvenida = True

# Botón B: Gráfica
if st.button("Mostrar gráfica"):
    st.session_state.mostrar_grafica = True

# Mostrar el mensaje si fue activado
if st.session_state.mostrar_bienvenida:
    st.success("¡Bienvenido a la aplicación!")

# Mostrar la gráfica si fue activado
if st.session_state.mostrar_grafica:
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Gráfica de Seno")
    st.pyplot(fig)






