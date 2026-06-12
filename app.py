import streamlit as st

st.title("My first Dart-App")

pages = {
  "Account Settings": [
    st.Page("pages/players.py", title="Add new players"),
  ],
}

pg = st.navigation(pages)
pg.run()
