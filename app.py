import streamlit as st

st.set_page_config(
    page_title="Stock Market Analytics",
    layout="wide"
)

st.title("📈 Stock Market Analytics Platform")

st.markdown("""
Welcome to the Stock Market Dashboard.

Use the sidebar to navigate between:

• Overview  
• Volatility Analysis  
• Return Analysis  
""")

st.info("Select a page from the left sidebar to begin.")
