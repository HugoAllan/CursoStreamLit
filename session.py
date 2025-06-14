# configuración de la página
import streamlit as st

# configuración de la página
st.set_page_config(
    page_title="Curso de Streamlit",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Sesiones y Estado de la Aplicación")

# creación de una sesión
if "texto" not in st.session_state:
    st.session_state.texto = "Un texto por defecto"
    
st.write("Texto en la sesión:", st.session_state.texto)

# botón para cambiar el texto
if st.button("Cambiar texto"):
    st.session_state.texto = "Un nuevo texto agregado"

st.write("Texto actualizado en la sesión:", st.session_state.texto)


st.divider()

# CallBacks
if "texto_callback" not in st.session_state:
    st.session_state.texto_callback = "Texto inicial"

def cambiar_texto():
    st.session_state.texto_callback = "Texto actualizado"

st.write(st.session_state.texto_callback)
btn_callback = st.button("Boton con Callback", on_click=cambiar_texto)
st.write(st.session_state.texto_callback)

st.divider()

state = st.session_state
# Ejemplo de uso de session_state
if "contador" not in state:
    state.contador = 0

def incrementar_contador():
    state.contador += 1

def decrementar_contador():
    if state.contador > 0:
        state.contador -= 1

st.write(f"## {state.contador}")
# if st.button("Incrementar contador"):
#     state.contador += 1

# if st.button("Decrementar contador"):
#     state.contador -= 1
col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    st.button("Sumar", on_click=incrementar_contador, use_container_width=True)
with col2:
    st.button("Restar", key="botonB", on_click=decrementar_contador, use_container_width=True)

st.divider()

# Ejemplo de uso de session_state con un formulario
form = st.form("my_form")
form.text_input("Texto del formulario", key="form_texto")
form.form_submit_button("Enviar")
st.write("Texto del formulario:", st.session_state.form_texto)


st.divider()

st.subheader("Operaciones Matemáticas con Streamlit")

# Inicializa el estado para el resultado
if 'op' not in st.session_state:
    st.session_state['op'] = 'ninguna'

# Layout de los botones en columnas iguales
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Suma", use_container_width=True):
        st.session_state['op'] = 'suma'
with col2:
    if st.button("Resta", use_container_width=True):
        st.session_state['op'] = 'resta'
with col3:
    if st.button("División", use_container_width=True):
        st.session_state['op'] = 'division'
with col4:
    if st.button("Multiplicación", use_container_width=True):
        st.session_state['op'] = 'multiplicacion'

# Diccionario con operaciones, colores y mensajes
opciones = {
    'suma': {'resultado': 10 + 5, 'color': '#ffe066', 'texto': 'Suma (10+5):'},
    'resta': {'resultado': 10 - 5, 'color': '#74c0fc', 'texto': 'Resta (10-5):'},
    'division': {'resultado': 10 / 5, 'color': '#ff6b6b', 'texto': 'División (10/5):'},
    'multiplicacion': {'resultado': 10 * 5, 'color': '#f3d9fa', 'texto': 'Multiplicación (10*5):'}
}

# Usa un solo container para mostrar el resultado
container = st.container()
with container:
    op = st.session_state['op']
    if op in opciones:
        style = f"""
        <div style='background-color:{opciones[op]['color']};
                    padding:40px;
                    border-radius:16px;
                    min-height:100px;
                    display:flex;
                    flex-direction:column;
                    justify-content:center;
                    align-items:center;
                    font-size:2rem;
                    font-weight:bold;
                    transition: background 0.3s;'>
            {opciones[op]['texto']} {opciones[op]['resultado']}
        </div>
        """
        st.markdown(style, unsafe_allow_html=True)
    else:
        # Placeholder inicial
        st.markdown(
            """
            <div style='background-color:#f1f3f5;
                        padding:40px;
                        border-radius:16px;
                        min-height:100px;
                        display:flex;
                        flex-direction:column;
                        justify-content:center;
                        align-items:center;
                        color:#888;
                        font-size:1.5rem;'>
                Selecciona una operación para ver el resultado aquí.
            </div>
            """, unsafe_allow_html=True
        )
        
st.divider()

with open("assets/streamlit_logo.jpeg", "rb") as file:
    st.download_button(
        label="Descargar Logo de Streamlit",
        data=file,
        file_name="streamlit_logo.jpeg",
        mime="image/jpeg"
    )
st.write("¡Gracias por usar esta aplicación de ejemplo!")