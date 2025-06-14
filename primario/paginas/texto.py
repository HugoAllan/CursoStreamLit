import streamlit as st



# función para mostrar un mensaje de bienvenida como un H1
st.title("Textos")

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


# Latex
st.latex(r"""
\begin{equation}
E = mc^2
\end{equation}
""")

st.latex("E = mc^2")
# matrices
st.latex(r"""
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
""")

# json
st.json({
    "nombre": "Hugo",
    "apellido": "Martinez",
    "edad": 30,
    "lenguajes": ["Python", "JavaScript", "C++"],
    "activo": True,
    "direccion": {
        "calle": "123 Main St",
        "ciudad": "Ciudad",
        "pais": "Pais"
    }
})  

code = """
# Ejemplo de código en Python
def saludar(nombre):
    return f"Hola, {nombre}!"   
"""
st.code(code, language='python')

# write
st.write("Este es un texto escrito con `st.write()`")




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


# Metricas
st.metric(label="Temperatura", value="25 °C", delta="1 °C")
st.metric(label="Velocidad", value="120 km/h", delta="-5 km/h")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Temperatura", value="25 °C", delta="1 °C")

with col2:
    st.metric(label="Velocidad", value="120 km/h", delta="-5 km/h")

# Barra de progreso
st.progress(50)  # Progreso al 50%
# Contador
if "contador" not in st.session_state:
    st.session_state.contador = 0
if st.button("Incrementar contador"):
    st.session_state.contador += 1
st.write(f"Contador: {st.session_state.contador}")
# Selección de opciones
opcion = st.selectbox("Selecciona una opción", ["Opción 1", "Opción 2", "Opción 3"])
st.write(f"Opción seleccionada: {opcion}")
# Casillas de verificación
checkbox = st.checkbox("Marcar esta casilla")
st.write(f"Casilla marcada: {checkbox}")
# Radio buttons
radio = st.radio("Selecciona una opción", ["Opción A", "Opción B", "Opción C"])
st.write(f"Opción seleccionada: {radio}")
# Desplegables
desplegable = st.selectbox("Selecciona un elemento", ["Elemento 1", "Elemento 2", "Elemento 3"])
st.write(f"Elemento seleccionado: {desplegable}")
# Entradas de texto
texto = st.text_input("Ingresa un texto")
st.write(f"Texto ingresado: {texto}")
# Entradas de contraseña
contrasena = st.text_input("Ingresa una contraseña", type="password")
st.write(f"Contraseña ingresada: {contrasena}")
# Entradas de número
numero = st.number_input("Ingresa un número", min_value=0, max_value=100, value=50)
st.write(f"Número ingresado: {numero}")
# Entradas de fecha
fecha = st.date_input("Selecciona una fecha")
st.write(f"Fecha seleccionada: {fecha}")
# Entradas de hora
hora = st.time_input("Selecciona una hora")
st.write(f"Hora seleccionada: {hora}")
# Entradas de archivo
archivo = st.file_uploader("Sube un archivo", type=["txt", "csv", "xlsx"])
if archivo is not None:
    st.write(f"Archivo subido: {archivo.name}")
    # Mostrar el contenido del archivo si es un texto
    if archivo.type == "text/plain":
        contenido = archivo.read().decode("utf-8")
        st.text_area("Contenido del archivo", value=contenido, height=300)
    elif archivo.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        import pandas as pd
        df = pd.read_excel(archivo)
        st.dataframe(df)
# Botones
if st.button("Botón de acción"):
    st.success("¡Botón presionado!")
# Mostrar un mensaje de éxito
st.success("¡Todo ha ido bien!")
# Mostrar un mensaje de error
st.error("¡Ha ocurrido un error!")
# Mostrar un mensaje de advertencia
st.warning("¡Cuidado! Esto es una advertencia.")
# Mostrar un mensaje de información
st.info("¡Esto es información importante!")
# Mostrar un mensaje de éxito
st.success("¡Operación exitosa!")
# Mostrar un mensaje de error
st.error("¡Ha ocurrido un error!")
# Mostrar un mensaje de advertencia
st.warning("¡Cuidado! Esto es una advertencia.")
# Mostrar un mensaje de información
st.info("¡Esto es información importante!") 




