import streamlit as st
import pandas as pd
import main
import time

df = pd.read_csv("report.csv")
df["Date"] = pd.to_datetime(df["Date"])
st.dataframe(df)

stutus = "Relaxed"
# Function to read and display data from "report.csv"
def display_data():
    df = pd.read_csv("report.csv")
    df["Date"] = pd.to_datetime(df["Date"])

# Create the button and handle its click event
if st.button("Run Test and Reload Data"):

    # Replace this placeholder with your actual test function
    main.runme()

    # Reload data after the test function runs
    display_data()

