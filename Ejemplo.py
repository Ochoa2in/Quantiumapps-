import streamlit as st 
import pandas as pd
st.title("Mi primer app")
#st.button("dale click")
#st.button("otro botón")
df=pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
st.write(df)
st.map(df)