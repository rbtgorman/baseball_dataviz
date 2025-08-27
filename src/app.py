import streamlit as st
import pandas as pd

df = pd.read_csv("../data/park_factors.csv")

st.title("Ballpark Factors Explorer")
st.dataframe(df)
