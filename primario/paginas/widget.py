import streamlit as st


# función para mostrar un mensaje de bienvenida como un H1
st.title("Widgets")

st.subheader("SelectBox")
# selectbox para elegir un color
color = st.selectbox(
    "Elige un color",
    ["Rojo", "Verde", "Azul"]
)
# mostrar el color seleccionado
st.write(f"Has seleccionado el color: {color}")

# Multiselect para elegir varios colores
st.subheader("Multiselect")
colores = st.multiselect(
    "Elige varios colores",
    ["Rojo", "Verde", "Azul", "Amarillo", "Naranja"]
)
# mostrar los colores seleccionados
st.write(f"Has seleccionado los colores: {', '.join(colores)}")

# Radio para elegir un color
st.subheader("Radio")
color_radio = st.radio(
    "Elige un color",
    ["Rojo", "Verde", "Azul"],
    captions=[
        "Opcion 1: Rojo",
        "Opcion 2: Verde",
        "Opcion 3: Azul"
    ]
)

st.subheader("Condicionales")
# Condiconal para mostrar un mensaje si se ha seleccionado un color
if color_radio == "Rojo":
    st.write(f"El color no puede ser {color_radio} porque es un color peligroso")
else:
    st.write(f"Has seleccionado el color: {color_radio}")

var = 1
if var == 1:
    st.write("La variable es igual a 1")

# Checkbox para elegir si se muestra un mensaje
st.subheader("Checkbox con Condicionales")
aceptar = st.checkbox("Aceptar términos y condiciones")
if aceptar:
    st.write("Has aceptado los términos y condiciones")
# Botón para mostrar un mensaje
if st.button("Mostrar mensaje"):
    st.write("Has pulsado el botón para mostrar el mensaje")


# Toggle
st.subheader("Toggle")
rechazo = st.toggle("Rechazar términos y condiciones")
if rechazo:
    st.write("Has rechazado los términos y condiciones")
    st.error("No aceptas los términos y condiciones, no puedes continuar")


# color picker para elegir un color
st.subheader("Color Picker")
color_picker = st.color_picker("Elige un color", "#00f900")
# mostrar el color seleccionado
st.write(f"Has seleccionado el color: {color_picker}")

# Slider
st.subheader("Slider")
slider = st.slider("Elige un número", 0, 100, 50, step=5)
# mostrar el número seleccionado
st.write(f"Has seleccionado el número: {slider}")

rango = st.slider(
    "Elige un rango de números",
    0, 100, (25, 75), step=5
)
# mostrar el rango seleccionado
st.write(f"Has seleccionado el rango: {rango[0]} - {rango[1]}")

