import streamlit as st


# configuración de la página
st.set_page_config(
    page_title="Curso de Streamlit",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Botones y Callbacks")

btnA = st.button("Botón simple", key="boton_simpleA")
btnB = st.button("Botón simple", key="boton_simpleB")

if btnA:
    st.write("Has pulsado el botón A")
if btnB:
    st.write("Has pulsado el botón B")

st.divider()

st.subheader("Botones con Callback")

def callback():
    st.write("Has pulsado el botón con callback")
    
btn_callback = st.button("Botón con Callback", on_click=callback)

st.divider()
st.subheader("Botones con Parámetros")
def callback_parametro(parametro):
    st.write(f"Has pulsado el botón con parámetro: {parametro}")

btn_parametro = st.button("Botón con Parámetro", on_click=callback_parametro, args=("Hola, soy un parámetro",))


st.divider()
