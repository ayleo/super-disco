import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Leo's Showcase Site", 
    page_icon=":🧊", 
    layout="wide",
    menu_items={
        'Get Help': 'https://twitter.com/elonmusk/',
        'Report a bug': 'https://twitter.com/elonmusk/',
        'About': "This is a simple example of a Streamlit app."
    }
)


col1, col_empty_space, col2 = st.columns(3)

with col1:
    st.image("images/photo.jpg", use_column_width=True, caption="Leo")

with col_empty_space:
    st.title("Leo")
    content = '''
    I am a Self-Studying student with a passion for Data Science and Machine Learning.
    Below you can find some of the apps I have built in Python. Feel free to explore them! 🚀
'''
    st.info(content)

st.divider()

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")
        st.divider()

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")
        st.divider()


