import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
from app1 import agente_page 


# Page Setup 
# Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"img/charles.jpg")  
    st.image(image)

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
        st.header("¡Hola, bienvenido a mi sitio web!")
        ruta_animacion = "animation/Animation - 1706587782829.json"
        animacion = cargar_animacion(ruta_animacion)
        st_lottie(animacion, speed=1, loop=True)

        # Contenido adicional en español
        with st.container():
            st.markdown("""
            Soy Juan Carlos V, aunque mi familia me llama Carlos o Charles. Aquí encontrarás una muestra de los proyectos 
            que he desarrollado a lo largo de mi carrera como Full Stack & Data Engineer. 
            Poseo experiencia práctica en una amplia variedad de proyectos, utilizando herramientas 
            como Python, TypeScript, JavaScript, Next.js, React y Google Cloud, entre otras tecnologías.
            Mi trabajo ha abarcado tareas de ETL, Ingeniería y Análisis de Datos, así como proyectos en Web3. Además, tengo conocimientos en Machine Learning y un gran interés por áreas como la Inteligencia Artificial y el Deep Learning. Soy un apasionado de este campo y estoy convencido de que siempre hay algo nuevo por aprender.
            Actualmente, me desempeño como Desarrollador en Skinner, una plataforma que emplea IA para el reclutamiento de personal.
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
        st.header("Hello, and welcome to my website!")
        animation_path = "animation/Animation - 1706587782829.json"
        animation = cargar_animacion(animation_path)
        st_lottie(animation, speed=1, loop=True)

        # Additional content in English
        with st.container():
            st.markdown("""
            I am Juan Carlos V, although my family calls me Carlos or Charles. Here you will find a selection
            of the projects I have developed throughout my career as a Full Stack & Data Engineer. 
            I have practical experience in a wide range of projects, utilising tools such as Python, 
            TypeScript, JavaScript, Next.js, React and Google Cloud, among other technologies.
            My work has encompassed tasks in ETL, Data Engineering and Data Analysis, as well as 
            projects in Web3. I also have knowledge in Machine Learning and a keen interest in fields such as Artificial 
            Intelligence and Deep Learning. I am passionate about this area and firmly believe that there is always something new to learn.
            I am currently employed as a Developer at Skinner, a platform that employs AI for staff recruitment.

            I hope you enjoy exploring my projects!
            """)

        # Contact section in English
        with st.container():
            st.write("---")
            st.header("Contact")
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
        st.image(imagen_vecino)
        
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
        st.image(imagen_vecino_grafi)

        # Enlace a Github
        st.write("Lee más en [Github](https://github.com/Chinaskidev/VecinoNet_Proyecto)")
          
    elif pagina_seleccionada == "English":
        st.header("VecinoNet")
        st.write("""VecinoNet: Networks for Everyone, arises in response to the growing importance of Internet access in the development and education of communities, 
                 especially those with limited resources. The analysis is based on data collected by ENACOM, 
                 focusing on low-income communities and provinces in Argentina.""")
        
        # Imagen de VecinoNet en inglés
        imagen_vecino = "img/vecinonet.png"
        st.image(imagen_vecino)
        
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
        st.image(imagen_vecino_grafi)
        
        # Enlace a Github
        st.write("Read more on[Github](https://github.com/Chinaskidev/VecinoNet_Proyecto)")


# Función para mostrar la página de Steam
def SivarETH_page():
    if pagina_seleccionada == "Español":
        st.header("SivarETH-Dapp")
        st.write("""
                 El objetivo principal de SivarETH es apoyar a emprendedores y pequeñas fundaciones para beneficiar a personas necesitadas. 
                 El enfoque de SivarETH se puede describir como una fórmula colaborativa: a + b = 1, 
                 donde:

                “a” representa a los emprendedores y fundaciones, a quienes educamos en el ecosistema 
                Web3, ayudándolos a adoptar nuevas tecnologías y estrategias para crecer y adaptarse a la era digital.

                “b” corresponde a los beneficiarios de estos emprendedores, quienes también reciben 
                educación en Web3, y se les brinda acceso a productos y servicios ofrecidos por ‘a’. 
                A su vez, “b” puede aprender a usar herramientas descentralizadas, como las criptomonedas, 
                para mejorar su calidad de vida y acceder a recursos esenciales.

                El modelo SivarETH busca crear un ciclo de impacto mutuo: los emprendedores 
                (“a”) se capacitan en Web3, mejoran sus negocios y, gracias a las ventas de NFT y 
                donaciones, se generan fondos para ayudar a los beneficiarios (“b”). 
                Estos beneficiarios, además de recibir ayuda económica, consumen productos o 
                servicios de los emprendedores participantes, lo que fortalece las economías 
                locales y genera sinergia entre ambos grupos. 
                A largo plazo, tanto “a” como “b” se benefician, no solo económicamente, sino también 
                a través del aprendizaje y la adopción de nuevas tecnologías.

                Este enfoque garantiza que la tecnología Web3 se utilice no solo como un medio 
                para recaudar fondos, sino como una herramienta educativa que empodera a todos 
                los involucrados, creando así un ecosistema inclusivo y sostenible.
                 """)

        # Imagen de  Steam
        imagen_SivarETH = "img/sivar.jpg"
        st.image(imagen_SivarETH)
        
        
        # Enlace a Github
        st.write("Lee más en [Github](https://github.com/Chinaskidev/Dapp-SivarETH)")
        
        
    elif pagina_seleccionada == "English":
        st.header("SivarETH-Dapp")
        st.write("""
                 SivarETH main objective is to support entrepreneurs and small foundations in order 
                 to benefit people in need. SivarETH's approach can be described as a collaborative 
                 formula: a + b = 1, where:

                “a” represents entrepreneurs and foundations, whom we educate in the Web3 ecosystem, 
                helping them adopt new technologies and strategies to grow and adapt to the digital age.

                “b” corresponds to the beneficiaries of these entrepreneurs, who also receive 
                education in Web3, and are provided access to products and services offered by ‘a’. 
                In turn, “b” can learn to use decentralized tools, such as cryptocurrencies, 
                to improve their quality of life and access essential resources.

                The SivarETH model seeks to create a cycle of mutual impact: entrepreneurs 
                (“a”) are trained in Web3, improve their businesses and, thanks to the sales of 
                NFTs and donations, funds are generated to help beneficiaries (“b”). 
                These beneficiaries, in addition to receiving financial assistance, 
                consume products or services from the participating entrepreneurs, 
                which strengthens local economies and generates synergy between the two groups. 
                In the long run, both “a” and “b” benefit, not only economically, 
                but also through learning and adopting new technologies.

                This approach ensures that Web3 technology is used not only as a means of 
                fundraising, but as an educational tool that empowers all involved, thus creating 
                an inclusive and sustainable ecosystem.
                 
                 """)
        
        # Imagen de Steam en inglés
        imagen_SivarETH = "img/sivar.jpg"
        st.image(imagen_SivarETH)
        
        
        # Enlace a Github
        st.write("Read more on [Github](https://github.com/Chinaskidev/Dapp-SivarETH)")      


# Obtener el estado de la sesión
state = get_state()

# Mostrar el selector de página en la barra lateral
pagina_adicional_seleccionada = st.sidebar.selectbox("Proyectos/Projects", ["Home", "VecinoNet", "SivarETH", "Agente-ElizaOs"])

# Actualizar el estado de la página
state.page = pagina_adicional_seleccionada

# Mostrar la página correspondiente
if state.page == 'Home':
    home_page()
elif state.page == 'VecinoNet':
    vecinonet_page()
elif state.page == 'SivarETH':
    SivarETH_page()
elif state.page == 'Agente-ElizaOs':
    agente_page(pagina_seleccionada)

