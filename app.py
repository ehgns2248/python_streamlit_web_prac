import streamlit as st
import pandas as pd

st.write('# 파이썬 웹 연습')

st.write('## -변수')
arr = [10, 50, 70, 20]
arr

st.write('### --차트')
st.bar_chart(arr)

st.write('#### ---데이터')
data = pd.Series(arr)
data