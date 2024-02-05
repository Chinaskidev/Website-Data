import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
from app1 import ecoride_page 


# Page Setup 
# Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"img/sidebymanos.png")  
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

# Crear un objeto de estado de sesión si no existe
def get_state():
    if 'get' not in dir(st.session_state):
        st.session_state['page'] = 'Home'
    return st.session_state

# Función para la página de inicio
def home_page():
    
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

        # Sección de contacto en español
        
        
        with st.container():
            st.write("---")
            st.header("Contacto")
            cols= st.columns(3)

            # Github
            cols[0].image("img/github.png", width=90)
            cols[0].markdown("[Github](https://github.com/Chinaskidev)")

            # LinkedIn
            cols[1].image("img/linkedin.png", width=90)
            cols[1].markdown("[LinkedIn](https://www.linkedin.com/in/juancarlosvz/)")

            # Email
            cols[2].image("img/Gmail.png", width=90)
            cols[2].markdown("[Email](mailto:juangreen17@gmail.com)")            
                                
                
    

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

        # Contact section in English
        with st.container():
            st.write("---")
            st.header("Contacto")
            cols= st.columns(3)

            # Github
            cols[0].image("img/github.png", width=90)
            cols[0].markdown("[Github](https://github.com/Chinaskidev)")

            # LinkedIn
            cols[1].image("img/linkedin.png", width=90)
            cols[1].markdown("[LinkedIn](https://www.linkedin.com/in/juancarlosvz/)")

            # Email
            cols[2].image("img/Gmail.png", width=90)
            cols[2].markdown("[Email](mailto:juangreen17@gmail.com)")   

# Funciones para mostrar las páginas de proyectos                
def vecinonet_page():
    if pagina_seleccionada == "Español":
        st.header("VecinoNet")
        st.write("""VecinoNet: Redes para Todos, surge como respuesta a la creciente importancia del acceso a Internet en el desarrollo y la educación de las comunidades, 
                 especialmente aquellas con recursos limitados. El análisis se fundamenta en datos recopilados por ENACOM , 
                 centrándose en comunidades y provincias de bajos recursos en Argentina.""")
        
        # Imagen de VecinoNet
        imagen_vecino = "img/vecinonet.png"
        st.image(imagen_vecino, use_column_width=True)
        
        # Contenido adicional en español    
        st.markdown("""En este análisis de conectividad a internet, mi enfoque principal se centró en áreas que enfrentan limitaciones de recursos, 
                 donde las comunidades, especialmente en algunas provincias de Argentina, carecen de acceso a una 
                 conectividad de calidad. Esta situación puede deberse tanto a limitaciones económicas como a condiciones 
                 geográficas que dificultan la cobertura de red en esas zonas.""")
        
        st.markdown("""El análisis se enfoca en las tecnologías que actualmente se utilizan en estas comunidades, independientemente de la velocidad de conexión. 
                 Observamos que las velocidades de descarga varían ampliamente, desde 3 Mbps hasta 10 Mbps. 
                 Incluso en la ciudad de Buenos Aires, encontramos disparidades en la calidad de la conexión en diferentes barrios, 
                 donde algunos pueden tener velocidades de conexión inferiores a 1 Mbps.""")
        
        # Imagen de grafico VecinoNet español
        imagen_vecino_grafi = "charts/gragico_descargainter.png"
        st.image(imagen_vecino_grafi, use_column_width=True)

        # Enlace a Github
        st.write("Lee más en [Github](https://github.com/Chinaskidev/VecinoNet_Proyecto)")
          
    elif pagina_seleccionada == "English":
        st.header("VecinoNet")
        st.write("""VecinoNet: Networks for Everyone, arises in response to the growing importance of Internet access in the development and education of communities, 
                 especially those with limited resources. The analysis is based on data collected by ENACOM, 
                 focusing on low-income communities and provinces in Argentina.""")
        
        # Imagen de VecinoNet en inglés
        imagen_vecino = "img/vecinonet.png"
        st.image(imagen_vecino, use_column_width=True)
        
        # Contenido adicional en inglés
        st.markdown("""In this analysis of internet connectivity, my main focus was on areas facing resource limitations,
                    where communities, especially in some provinces of Argentina, lack access to quality connectivity.
                    This situation may be due to both economic constraints and geographical conditions that hinder network coverage in these areas.""")
        
        st.markdown("""The analysis focuses on the technologies currently used in these communities, 
                    regardless of connection speed. We observe that download speeds vary widely, 
                    ranging from 3 Mbps to 10 Mbps. Even in the city of Buenos Aires, we find disparities in connection quality across different 
                    neighborhoods, where some may have connection speeds lower than 1 Mbps.""")
        
        # Imagen de grafico VecinoNet español
        imagen_vecino_grafi = "charts/gragico_descargainter.png"
        st.image(imagen_vecino_grafi, use_column_width=True)
        
        # Enlace a Github
        st.write("Read more on[Github](https://github.com/Chinaskidev/VecinoNet_Proyecto)")


# Función para mostrar la página de Steam
def steam_page():
    if pagina_seleccionada == "Español":
        st.header("Steam")
        st.write("""Este proyecto se enfoca en el desarrollo de un sistema de recomendación para la plataforma de videojuegos STEAM, donde se ha asumido el rol de MLOps Engineer. 
                 Se ha implementado un proceso de Extracción, Transformación y Carga (ETL) y un Análisis Exploratorio de Datos (EDA). 
                 El objetivo principal es desplegar una API con un modelo de Machine Learning capaz de analizar los sentimientos a partir de los comentarios de los usuarios. 
                 Este modelo también servirá para ofrecer un sistema de recomendación de videojuegos para la plataforma, mejorando la experiencia de los usuario""")

        # Imagen de  Steam
        imagen_steam = "img/steam.png"
        st.image(imagen_steam, use_column_width=True)
        
        st.markdown(""""En el proceso del proyecto, se llevó a cabo un Modelo de Recomendación, basado en la similitud del coseno,
                    donde se crearon las siguientes funciones:""")

        st.markdown("""- Primera Función item-item, introduciendo el id del juego y le devuelve 5 juegos similares al usuario.""")

        st.markdown(""" - Segunda Función de usuario-item, Ingresa el id del usuario y le devuelve 5 juegos recomendados. """)
                           
        st.markdown("""Para el primer enfoque del modelo, se establece una relación ítem-ítem. En este escenario, se evalúa un ítem con respecto a su similitud con otros ítems para ofrecer 
                recomendaciones similares. En este caso, el input corresponde a un juego y el output es una lista de juegos recomendados, 
                utilizando el concepto de similitud del coseno.""")        

        st.markdown("""Por otra parte, se considera una segunda propuesta para el sistema de recomendación,
                basada en el filtro user-item. En esta estrategia, se analiza a un usuario para identificar usuarios con gustos similares y se recomiendan 
                ítems que hayan sido apreciados por estos usuarios afines.""")   
        
        # Enlace a video    
        st.write("Puedes ver el Deploy en [Video](https://www.loom.com/share/8cfd463c84d24f748390800dc3718fbb?sid=4625d89b-43ee-4693-89ec-193e66c28301)")
        # Enlace a Github
        st.write("Lee más en [Github](https://github.com/Chinaskidev/STEAM_Recomendacion)")
        
        
    elif pagina_seleccionada == "English":
        st.header("Steam")
        st.write("""This project focuses on the development of a recommendation system for the STEAM video game platform, where the role of MLOps Engineer has been assumed. 
                 An Extraction, Transformation and Load (ETL) process and an Exploratory Data Analysis (EDA) have been implemented. 
                 The main objective is to deploy an API with a Machine Learning model capable of analyzing sentiments from user comments. 
                 This model will also serve to offer a video game recommendation system for the platform, improving the user experience""")
        
        # Imagen de Steam en inglés
        imagen_steam = "img/steam.png"
        st.image(imagen_steam, use_column_width=True)
        
        # Additional content in English
        st.markdown("""In the project process, a Recommendation Model was 
                    implemented based on cosine similarity, where the following functions were created:""")
        
        st.markdown("""- First Function item-item, inputting the game ID and returning 5 similar games to the user.""")

        st.markdown("""- Second user-item Function, inputs the user ID and returns 5 recommended games.""")
        
        st.markdown("""For the first model approach, an item-item relationship is established. In this scenario, an item is evaluated with respect to its similarity to other items to provide similar recommendations. 
                    In this case, the input corresponds to a game, and the output is a list of recommended games, 
                    using the concept of cosine similarity.""")   
        
        st.markdown("""On the other hand, a second proposal for the recommendation system is considered, based on the user-item filter. 
                    In this strategy, a user is analyzed to identify users with similar tastes, 
                    and items appreciated by these like-minded users are recommended.""") 
        
        # Enlace a video    
        st.write("You can see the deployment at [Video](https://www.loom.com/share/8cfd463c84d24f748390800dc3718fbb?sid=4625d89b-43ee-4693-89ec-193e66c28301)")
        # Enlace a Github
        st.write("Read more on [Github](https://github.com/Chinaskidev/STEAM_Recomendacion)")      


# Obtener el estado de la sesión
state = get_state()

# Mostrar el selector de página en la barra lateral
pagina_adicional_seleccionada = st.sidebar.selectbox("Proyectos/Projects", ["Home", "VecinoNet", "Steam", "ECORIDE-NYC"])

# Actualizar el estado de la página
state.page = pagina_adicional_seleccionada

# Mostrar la página correspondiente
if state.page == 'Home':
    home_page()
elif state.page == 'VecinoNet':
    vecinonet_page()
elif state.page == 'Steam':
    steam_page()
elif state.page == 'ECORIDE-NYC':
    ecoride_page(pagina_seleccionada)

