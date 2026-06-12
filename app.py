import streamlit as st

st.title("My first Dart-App")

player = st.text_input("Player Name")

if player:
  st.success(f"Hallo {player}")
