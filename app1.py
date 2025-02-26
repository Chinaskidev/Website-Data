#app1.py
import streamlit as st

# Función para mostrar la página Dataminds
def agente_page(pagina_seleccionada):
    if pagina_seleccionada == "Español":
        st.header("Agente-en-X-ElizaOs")
        st.write("""
                 Construí un agente sencillo que te habla sobre Blockchain y Web3 utilizando ElizaOS, 
                 un framework que te permite crear tus propios agentes de inteligencia artificial.
                Este agente está diseñado para responder preguntas y ofrecer explicaciones sobre 
                conceptos clave en el ecosistema de la Web3, desde la tecnología Blockchain hasta 
                criptomonedas y contratos inteligentes.
                Con ElizaOS, puedes desarrollar agentes personalizados que se ajusten a tus 
                necesidades, integrando múltiples modelos de IA y diferentes plataformas. 
                ¡Es una herramienta poderosa para construir tus propios agentes!
                 
                 """)

        
        
        # Imagen de agente
        imagen_agente = "img/eliza_diagram.png"
        st.image(imagen_agente)
        
        
        
         
        
        # Enlace a Github
        st.write("Lee más en [Github](https://github.com/Chinaskidev/Agente-en-X-ElizaOs)")

        
        
    elif pagina_seleccionada == "English":
        st.header("Agent-in-X-ElizaOs")
        st.write("""
                 I built a simple agent that talks to you about Blockchain and Web3 using 
                 ElizaOS, a framework that lets you create your own artificial intelligence agents. 
                 This agent is designed to answer questions and provide explanations on key concepts 
                 within the Web3 ecosystem, from blockchain technology to cryptocurrencies and smart 
                 contracts. With ElizaOS, you can develop custom agents tailored to your needs, 
                 integrating multiple AI models and different platforms. It's a powerful tool for 
                 exploring decentralisation and the future of the web!
                 
                 """)
        
        
        
        # Imagen de agente
        imagen_agente = "img/eliza_diagram.png"
        st.image(imagen_agente)
        
        
        # Enlace a Github
        st.write("Read more on [Github](https://github.com/Chinaskidev/Agente-en-X-ElizaOs)")
        