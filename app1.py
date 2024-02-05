#app1.py
import streamlit as st

# Función para mostrar la página Dataminds
def ecoride_page(pagina_seleccionada):
    if pagina_seleccionada == "Español":
        st.header("ECORIDE-NYC")
        st.write("""En la actualidad, los servicios de taxis y viajes compartidos en la ciudad de Nueva York han emergido como alternativas populares al transporte público. 
                 Estos servicios no solo proporcionan una valiosa fuente de datos sobre la ubicación de los vehículos, 
                 sino también información relevante sobre la calificación de los conductores, 
                 las ganancias diarias y mensuales de los taxis convencionales en diversos boroughs de la ciudad de Nueva York, 
                 así como la autonomía, eficiencia y costos asociados a los autos eléctricos. 
                 El análisis de estos datos puede ofrecer percepciones clave sobre los cambios en los patrones de viaje, 
                 particularmente en el contexto de la evolución postpandemia y la creciente adopción de modelos de trabajo flexibles.""")

        # Imagen de ecoride
        imagen_eco = "img/taxi.jpg"
        st.image(imagen_eco, use_column_width=True)
        
        st.markdown("""En este proyecto se desarrollo un análisis integral de datos donde se aplicaron técnicas de Machine Learning para evaluar 
                    la viabilidad y el impacto de la incorporación de vehículos eléctricos en la flota, orientado a mejorar la sostenibilidad y eficiencia del transporte urbano. 
                    Este proyecto tiene como **objetivo general** proporcionar a una empresa de transporte de pasajeros de micros de media y larga distancia 
                    información clave sobre la posible transición a vehículos eléctricos, considerando aspectos como la reducción de la huella ambiental, 
                    el análisis de costos y ganancias, así como la implementación de estrategias sostenibles.""")
        
         # Imagen de ML
        imagen_eco = "img/app.png"
        st.image(imagen_eco, use_column_width=True)
        
        # Enlace a App
        st.write("Puedes probar el Modelo en [ML](https://demandpredictor-argsx2hozvnjcd7wlxfqg9.streamlit.app/)")
        
        # Enlace a Github
        st.write("Lee más en [Github](https://github.com/Chinaskidev/Dataminds-Consulting)")

        
        
    elif pagina_seleccionada == "English":
        st.header("ECORIDE-NYC")
        st.write("""Currently, taxi and ridesharing services in New York City have emerged as popular alternatives to public transportation. 
                 These services not only provide valuable data on vehicle locations but also relevant information on driver ratings,
                 daily and monthly earnings of conventional taxis in various boroughs of New York City, as well as the autonomy, 
                 efficiency, and costs associated with electric vehicles. 
                 Analyzing this data can offer key insights into changes in travel patterns, particularly in the context of post-pandemic 
                 evolution and the growing adoption of flexible work models.""")
        
        # Imagen de VecinoNet en inglés
        imagen_ecoride = "img/taxi.jpg"
        st.image(imagen_ecoride, use_column_width=True)
        
        st.markdown("""In this project, a comprehensive data analysis was conducted applying Machine Learning techniques 
                    to assess the feasibility and impact of incorporating electric vehicles into the fleet, 
                    aimed at enhancing the sustainability and efficiency of urban transportation. 
                    The main objective of this project is to provide a long-distance passenger transport company with key insights into 
                    the potential transition to electric vehicles, considering aspects such as reducing environmental footprint, 
                    cost-benefit analysis, and the implementation of sustainable strategies.""")
        
        # Imagen de ML
        imagen_eco = "img/app.png"
        st.image(imagen_eco, use_column_width=True)
        
        # Enlace a App
        st.write("You can test the model on [ML](https://demandpredictor-argsx2hozvnjcd7wlxfqg9.streamlit.app/)")
        
        # Enlace a Github
        st.write("Read more on [Github](https://github.com/Chinaskidev/Dataminds-Consulting)")
        