import streamlit as st
from PIL import Image

st.title("Tのアプリ")
st.caption("これはTのテストアプリです")

image = Image.open("./data/image1.png")
st.image(image,width=200)