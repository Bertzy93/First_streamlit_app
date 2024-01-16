import streamlit

streamlit.title ('My Parents New healthy Diner')

streamlit.header ('Breakfast Favorites')

streamlit.text ('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
String1 = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(String1.json())
# Pass String1 to String2
String2 = pandas.json_normalize(String1.json())
# write your own comment - what does this do?
streamlit.dataframe(String2)



streamlit.subheader ('By: Chef Bert Lagro')
streamlit.video("https://youtu.be/EdSLy-CyHes", format='video/mp4', start_time=0)


