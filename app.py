import streamlit as st
import pandas as pd
df = pd.read_csv("report.csv")
st.dataframe(df)
