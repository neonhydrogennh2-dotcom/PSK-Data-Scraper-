import streamlit as st
import pandas as pd

st.title("PSX Data Dashboard")
# Load the CSV data
csv_file = "psx_data.csv"
try:
    df = pd.read_csv(csv_file)
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"Error: The file '{csv_file}' was not found. Please ensure the data has been scraped and saved correctly.")
    
    
if __name__ == "__main__":
    st.write("This dashboard displays the latest stock data from the Pakistan Stock Exchange (PSX).")