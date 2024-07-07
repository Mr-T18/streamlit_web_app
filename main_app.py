import streamlit as st
from PIL import Image
import os

st.title("Tのアプリ")
st.caption("これはTのテストアプリです")

path = os.path.dirname(__file__)
image = Image.open(path + "/data/image1.png")
st.image(image,width=200)