import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Stock Overview")

# Load Data
df = pd.read_csv("Nifty_Stocks.csv")

# Convert Date column (if exists)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

# Show raw data option
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Select Stock Symbol (if Symbol column exists)
if "Symbol" in df.columns:
    symbol = st.selectbox("Select Stock Symbol", df["Symbol"].unique())
    df = df[df["Symbol"] == symbol]

# Show Key Metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

if "Close" in df.columns:
    col1.metric("Latest Close Price", round(df["Close"].iloc[-1], 2))

if "Volume" in df.columns:
    col2.metric("Average Volume", int(df["Volume"].mean()))

if "High" in df.columns:
    col3.metric("Highest Price", round(df["High"].max(), 2))

st.markdown("---")

# Price Chart
if "Date" in df.columns and "Close" in df.columns:
    st.subheader("Price Trend")
    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(df["Date"], df["Close"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    st.pyplot(fig)
