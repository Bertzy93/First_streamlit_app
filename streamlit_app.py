import streamlit
import pandas
import requests
import snowflake.connector
# from urllib.error import URLerror

streamlit.title ('My Parents New healthy Diner')

streamlit.header ('Breakfast Favorites')

streamlit.text ('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


String1 = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(String1.json())
# Pass String1 to String2
String2 = pandas.json_normalize(String1.json())
# write your own comment - what does this do?
streamlit.dataframe(String2)

#don't run anything past here while we troubleshoot


#requirement.txt
# snowflake-connector-phyton


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','apple')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ($add_my_fruit)")

# import snowflakes

streamlit.subheader ('By: Chef Bert Lagro')
streamlit.video("https://youtu.be/EdSLy-CyHes", format='video/mp4', start_time=0)
streamlit.stop()



# import streamlit as st
# import streamlit
# import pandas
# import requests
# # import snowflake.connector
 
# streamlit.title('My Parents New Healthy Diner')
 
# streamlit.header('Breakfast Menu')
# streamlit.text('Omega 3 & Blueberry Oatmeal')
# streamlit.text('Kale, Spinach & Rocket Smoothie')
# streamlit.text('Hard-Boiled Free-Range Egg')
 
# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
 
# # Display the table on the page.
# my_fruit_list = my_fruit_list.set_index('Fruit')
 
# # Let's put a pick list here so they can pick the fruit they want to include 
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[])
# fruits_to_show = my_fruit_list.loc[fruits_selected]
 
# streamlit.dataframe(fruits_to_show)
 
# streamlit.header("Fruityvice Fruit Advice!")
 
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)
 
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# # streamlit.text(fruityvice_response.json())
 
 
# # write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)
 
# #streamlit.stop()
 
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
 
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_rows = my_cur.fetchall()
# #streamlit.text("Hello from Snowflake:")
# streamlit.header("The fruit list contains")
# streamlit.dataframe(my_data_rows)
 
 
# streamlit.text("What fruit would you like to add?")
# text_input = st.text_input("Enter some text 👇")
 
# if text_input:
#     st.write("Thanks for adding : ", text_input)
 
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")
