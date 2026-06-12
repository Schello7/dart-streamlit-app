import streamlit as st

st.title("My first Dart-App")

page = st.sidebar.selectbox("Navigation", ["Players", "Matches"])

if page == "Players":
    import pages.players
