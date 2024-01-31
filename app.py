import streamlit as st
import requests
import streamlit_lottie as stl
from streamlit_lottie import st_lottie
from PIL import Image
import json

# Lista de páginas
paginas = ["Español", "English"]

# Selector de página
pagina_seleccionada = st.sidebar.selectbox("Elige un idioma / Choose a language", paginas)

# Función para cargar la animación
def cargar_animacion(ruta):
    with open(ruta, "r") as archivo:
        animacion = json.load(archivo)
    return animacion

# Contenido de la página en español
if pagina_seleccionada == "Español":
    st.header("¡Hola, bienvenido a mi sitio web!")
    ruta_animacion = "animation/Animation - 1706587782829.json"

    # Mostrar la animación en la aplicación de Streamlit
    animacion = cargar_animacion(ruta_animacion)
    st_lottie(animacion, speed=1, loop=True)

    # Contenido adicional en español
    with st.container():
        st.markdown("""
        # Ciencia de Datos
        ¡Hola y gracias por visitar mi página web. Me llamo Juan Carlos V, pero mi familia me llama Carlos o Charles.

        Aquí encontrarás una muestra de algunos de los proyectos que he desarrollado a lo largo de mi carrera como científico de datos.

        Cuento con experiencia práctica en una amplia variedad de proyectos, utilizando herramientas como Python, SQL y Google Cloud, entre otras tecnologías del sector. Mi trabajo ha abarcado desde tareas de ETL hasta Ingeniería y Análisis de Datos.

        Además, poseo conocimientos en Machine Learning y tengo un gran interés en profundizar en áreas como la Inteligencia Artificial y el Deep Learning. Soy una persona apasionada por este campo y estoy convencido de que siempre hay más por aprender. Constantemente busco formas de contribuir con conocimientos y aportar valor a los equipos de trabajo.

        ¡Espero que disfrutes explorando mis proyectos!
        """)

    # Sección de objetivo en español
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Mi objetivo")
            st.write(
                """
                Mi objetivo es compartir proyectos que demuestren mi experiencia en ciencia de datos, 
                destacando habilidades en Python, SQL y Google Cloud. 
                Busco colaborar en equipos donde pueda aplicar y expandir mis conocimientos en Machine Learning y explorar áreas como la Inteligencia Artificial y el Deep Learning.
                """
            )
            st.write("[Github](https://github.com/Chinaskidev)")

        with right_column:
            ruta_animacion = "animation/Animation - 1706591655553.json"
            animacion = cargar_animacion(ruta_animacion)
            st_lottie(animacion)

# Contenido de la página en inglés
elif pagina_seleccionada == "English":
    st.header("Hello, welcome to my website!")
    animation_path = "animation/Animation - 1706587782829.json"

    # Display the animation in the Streamlit app
    animation = cargar_animacion(animation_path)
    st_lottie(animation, speed=1, loop=True)

    # Additional content in English
    with st.container():
        st.markdown("""
        # Data Science
        Hello and thank you for visiting my website. My name is Juan Carlos V, but my family calls me Carlos or Charles.
        
        Here you will find a sample of some of the projects I have developed throughout my career as a data scientist.
        
        I have practical experience in a wide variety of projects, using tools such as Python, SQL, and Google Cloud, among other sector technologies. My work has ranged from ETL tasks to Data Engineering and Analysis.
        
        Additionally, I have knowledge in Machine Learning and I have a keen interest in delving into areas such as Artificial Intelligence and Deep Learning. I am passionate about this field and I am convinced that there is always more to learn. I constantly seek ways to contribute knowledge and add value to teams.
        
        I hope you enjoy exploring my projects!
        """)

    # Objective section in English
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("My Objective")
            st.write(
                """
                My objective is to share projects that demonstrate my experience in data science, 
                highlighting skills in Python, SQL, and Google Cloud. 
                I seek to collaborate in teams where I can apply and expand my knowledge in Machine Learning and explore areas such as Artificial Intelligence and Deep Learning.
                """
            )
            st.write("[Github](https://github.com/Chinaskidev)")

        with right_column:
            animation_path = "animation/Animation - 1706591655553.json"
            animation = cargar_animacion(animation_path)
            st_lottie(animation)
