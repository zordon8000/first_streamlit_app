
import streamlit as st
import pandas as pd

# 🥗 🐔 🥑🍞

st.title('My parents are New Healthy Diner')
st.header('Breakfast menu')
st.text('🥣 Omega 3 blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rokkie smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

st.dataframe(my_fruit_list)

st.multiselect("Pick some fruits:", list(my_fruit_list.index))



