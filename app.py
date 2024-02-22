import streamlit as st
import pandas as pd
df = pd.read_csv("report.csv")
df["Date"] = pd.to_datetime(df["Date"])
st.dataframe(df)
