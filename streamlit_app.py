


import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry Oat Meal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_lis = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_lis = my_fruit_lis.set_index('Fruit') 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_lis.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_lis.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +  this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
     streamlit.error("please select a fruit to get information")
   else:
     back_from_function=get_fruityvice_data(fruit_choice)
     streamlit.dataframe(back_from_function)
except URLError as e:
   streamlit.error()

    
streamlit.header ("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor () as my_cur:
    my_cur. execute("select * from fruit_load_list")
    return my_cur.fetchall()
# Add a button to load the fruit
if streamlit.button ('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe (my_data_rows)

  
  
  
  
  
  
  
 
def insert_row_snowflake(new_fruit):
  with my_cnx. cursor () as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + my_fruit_lis  + '")
    return "Thanks for adding " + new_fruit
  
add_my_fruit = streamlit.text_input ('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text (back_from_function)





# Allow the end user to add a fruit to the list 
#def insert_row_snowflake (new_fruit):
 # with my_cnx.cursor() as my_cur:
 #   my_cur.execute ("insert into fruit_load_list values ("papaya")
  #  return "Thanks for adding " + new_fruit
                    
                    
                    
streamlit.stop()                                                                             
#streamlit.write('The user entered ', fruit_choice)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +  fruit_choice)
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#treamlit.dataframe(fruityvice_normalized)



#import snowflake.connector

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("insert into fruit_load_list values('from streamlit')")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)


#fruit_choic = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
#streamlit.write('Thanks for adding ', fruit_choic)



