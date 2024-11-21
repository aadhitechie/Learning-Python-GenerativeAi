import streamlit as st
import pandas as pd
import numpy as np


st.title("Hi Hello")

#write the content 
st.write("The content are shown below")

#create a column
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

#display the data frame
st.write(df)

#creating chart

chart = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(chart)

#slider
age = st.slider("select your age:",18,60,23)
st.write(age)

# select box
options = ["python","dart","javascript","java"]
select_box = st.selectbox("Choose best",options)
st.write(f"you selected {select_box}")