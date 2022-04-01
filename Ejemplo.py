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
num1=st.slider("elige un numero 1",0.0,100.0,50.00)
num2=st.slider("elige el numero 2",0.0,100.0,50.00)
suma=num1+num2
st.write("la suma de",num1,"y",num2,"es:",suma)

st.write("ahora multipliquemos")
nn1=st.number_imput("mete un n1")
nn2=st.number_imput("dame n2")

mult=nn1(nn2)
st.write("la multiplicacion de nn1",nn1,"y"nn2,"es:",mult )