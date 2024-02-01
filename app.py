import streamlit as st
import requests
import streamlit_lottie as stl
from streamlit_lottie import st_lottie
from PIL import Image
import json

# Ruta local a la imagen de encabezado
imagen_cabecera = "animation/sidebyside.png"

# Page Setup 
#Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"animation/sidebymanos.png")  
    st.image(image, use_column_width=True)

# Lista de páginas
paginas = ["Español", "English"]

# Selector de página
pagina_seleccionada = st.sidebar.selectbox("Elige un idioma / Choose a language", paginas)

# Función para cargar la animación
def cargar_animacion(ruta_animacion):
    with open(ruta_animacion) as f:
        data = json.load(f)
    return data

# Navegación a la página adicional seleccionada

# Crear un objeto de estado de sesión si no existe
def get_state():
    if 'get' not in dir(st.session_state):
        st.session_state['page'] = 'main'
    return st.session_state

def main_page():
    st.image(imagen_cabecera, use_column_width=True)

    # Agregar una línea divisoria
    st.write("---")

    # Contenido de la página en español
    if pagina_seleccionada == "Español":
        st.header("Ciencia de Datos")
        ruta_animacion = "animation/Animation - 1706587782829.json"
        animacion = cargar_animacion(ruta_animacion)
        st_lottie(animacion, speed=1, loop=True)

        # Contenido adicional en español
        with st.container():
            st.markdown("""
            ¡Hola, bienvenido a mi sitio web!. Me llamo Juan Carlos V, pero mi familia me llama Carlos o Charles.
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
        st.header("Data Science")
        animation_path = "animation/Animation - 1706587782829.json"
        animation = cargar_animacion(animation_path)
        st_lottie(animation, speed=1, loop=True)

        # Additional content in English
        with st.container():
            st.markdown("""
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
                
def vecinonet_page():
    st.write("Contenido de la página de VecinoNet")

def steam_page():
    st.write("Contenido de la página de Steam")

state = get_state()

# Mostrar el selector de página en la barra lateral
pagina_adicional_seleccionada = st.sidebar.selectbox("Proyectos", ["main", "VecinoNet", "Steam"])

# Actualizar el estado de la página
state.page = pagina_adicional_seleccionada

def vecinonet_page():
    if pagina_seleccionada == "Español":
        st.header("VecinoNet")
        st.write("""VecinoNet: Redes para Todos, surge como respuesta a la creciente importancia del acceso a Internet en el desarrollo y la educación de las comunidades, 
                 especialmente aquellas con recursos limitados. El análisis se fundamenta en datos recopilados por ENACOM , 
                 centrándose en comunidades y provincias de bajos recursos en Argentina.""")
        # Aquí puedes agregar más contenido relacionado con VecinoNet
    elif pagina_seleccionada == "English":
        st.header("VecinoNet")
        st.write("""VecinoNet: Networks for Everyone, arises in response to the growing importance of Internet access in the development and education of communities, 
                 especially those with limited resources. The analysis is based on data collected by ENACOM, 
                 focusing on low-income communities and provinces in Argentina.""")
        # Aquí puedes agregar más contenido relacionado con VecinoNet en inglés

def steam_page():
    if pagina_seleccionada == "Español":
        st.header("Steam")
        st.write("""Este proyecto se enfoca en el desarrollo de un sistema de recomendación para la plataforma de videojuegos STEAM, donde se ha asumido el rol de MLOps Engineer. 
                 Se ha implementado un proceso de Extracción, Transformación y Carga (ETL) y un Análisis Exploratorio de Datos (EDA). 
                 El objetivo principal es desplegar una API con un modelo de Machine Learning capaz de analizar los sentimientos a partir de los comentarios de los usuarios. 
                 Este modelo también servirá para ofrecer un sistema de recomendación de videojuegos para la plataforma, mejorando la experiencia de los usuario""")
        # Aquí puedes agregar más contenido relacionado con Steam
    elif pagina_seleccionada == "English":
        st.header("Steam")
        st.write("""This project focuses on the development of a recommendation system for the STEAM video game platform, where the role of MLOps Engineer has been assumed. 
                 An Extraction, Transformation and Load (ETL) process and an Exploratory Data Analysis (EDA) have been implemented. 
                 The main objective is to deploy an API with a Machine Learning model capable of analyzing sentiments from user comments. 
                 This model will also serve to offer a video game recommendation system for the platform, improving the user experience""")
        # Aquí puedes agregar más contenido relacionado con Steam en inglés

# Mostrar la página correspondiente
if state.page == 'main':
    main_page()
elif state.page == 'VecinoNet':
    vecinonet_page()
elif state.page == 'Steam':
    steam_page()
    
    

