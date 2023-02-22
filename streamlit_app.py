
import streamlit
streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry Oat Meal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_lis = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_lis = my_fruit_lis.set_index('Fruit') 

streamlit.multiselect("Pick some fruits:", list(my_fruit_lis.index)) 

streamlit.dataframe(my_fruit_lis)



