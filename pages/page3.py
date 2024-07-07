import streamlit as st
import pandas as pd
import os

#データ分析関連
df_path = os.path.dirname(os.path.dirname(__file__))
df = pd.read_csv(df_path + "/data/平均気温.csv",index_col="月")
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df["2023年"])