import streamlit
import snowflake.connector
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog')


Sweat_list = pandas.read_xml("https://uni-klaus.s3.us-west-2.amazonaws.com")
# Sweat_list = Sweat_list.set_index('90s_tracksuit')
# Sweat_selected = streamlit.multiselect("Pick some Sweat:", list (Sweat_list.index),['burgundy_sweatsuit','charcoal_grey_sweatsuit'])
# Sweat_to_show = Sweat_list.loc[Sweat_selected]


streamlit.header("90s tracksuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/90s_tracksuit.png")

streamlit.header("burgundy sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/burgundy_sweatsuit.png")

streamlit.header("charcoal grey sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/charcoal_grey_sweatsuit.png")

streamlit.header("forest green sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/forest_green_sweatsuit.png")

streamlit.header("navy blue sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/navy_blue_sweatsuit.png")

streamlit.header("orange sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png")

streamlit.header("purple sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/purple_sweatsuit.png")

streamlit.header("red sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/red_sweatsuit.png")

streamlit.header("royal blue sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/royal_blue_sweatsuit.png")

streamlit.header("yellow sweatsuit")
streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/yellow_sweatsuit.png")


