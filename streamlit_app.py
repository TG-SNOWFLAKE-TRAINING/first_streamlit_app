import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Smoothies
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Datei einlesen
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Index setzen sodass Fruit Namen ausgewählt werden statt Zahlen
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Lets put a pick List here si they can pick the fruiot they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Tabelle anzeigen
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# json normalizing 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# json in dataframe darstellen
streamlit.dataframe(fruityvice_normalized)
