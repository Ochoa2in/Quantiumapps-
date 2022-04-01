import streamlit as st 
import pandas as pd
st.title("Mi primer app")
#las lienas eran para aprender a el primer ejericio 
click=st.button("dale click")
st.write("el valor de click es: ",click)

if click==True: 
    st.image("perro.jpg")

#st.button("otro botón")
#df=pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
#st.write(df)
#st.map(df)
#st.text("hola mundo")
#st.text("la siguiente es una integral")
#st.latex("\int_1^6sin(x)")
#st.markdown("#titulo")
#st.markdown("*este es una viñeta*")
