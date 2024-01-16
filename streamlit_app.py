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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text('fruityvice_response')

{
    "name": "Watermelon",
    "id": 25,
    "family": "Cucurbitaceae",
    "order": "Cucurbitales",
    "genus": "Citrullus",
    "nutritions": {
        "calories": 30,
        "fat": 0.2,
        "sugar": 6,
        "carbohydrates": 8,
        "protein": 0.6
    }
}



streamlit.subheader ('By: Chef Bert Lagro')
streamlit.video("https://youtu.be/EdSLy-CyHes", format='video/mp4', start_time=0)


