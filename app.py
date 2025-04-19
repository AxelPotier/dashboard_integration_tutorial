import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mon premier dashboard Streamlit")

# Charger les données
data = pd.read_csv("sales_data.csv")

# Afficher les données
st.write(data)

# Créer un graphique
fig, ax = plt.subplots()
data['total'].hist(ax=ax)
st.pyplot(fig)
