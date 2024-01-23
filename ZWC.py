import streamlit
import snowflake.connector
import pandas
streamlit.title("Zena's Amazing Athleisure Catalog")



Sweat_listed = streamlit.multiselect("Select Sweat Clothings:", 
[
"90s tracksuit"
, "burgundy sweatsuit"
, "charcoal grey sweatsuit"
,"forest green sweatsuit"
,"navy blue sweatsuit"
,"orange sweatsuit"
,"purple sweatsuit"
,"red sweatsuit"
,"royal blue sweatsuit"
,"yellow sweatsuit"
]
)
# Sweat_listed as Selected
Sweat_to_show = Sweat_list.loc[Sweat_listed]

# streamlit.header(Sweat_selected)

# IF Selected == "90s tracksuit":
# streamlit.header("90s tracksuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/90s_tracksuit.png")
# ELSE:
# streamlit.header("No Selection")


# streamlit.header("burgundy sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/burgundy_sweatsuit.png")

# streamlit.header("charcoal grey sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/charcoal_grey_sweatsuit.png")

# streamlit.header("forest green sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/forest_green_sweatsuit.png")

# streamlit.header("navy blue sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/navy_blue_sweatsuit.png")

# streamlit.header("orange sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png")

# streamlit.header("purple sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/purple_sweatsuit.png")

# streamlit.header("red sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/red_sweatsuit.png")

# streamlit.header("royal blue sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/royal_blue_sweatsuit.png")

# streamlit.header("yellow sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/yellow_sweatsuit.png")


