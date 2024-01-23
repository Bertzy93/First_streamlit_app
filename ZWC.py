import streamlit
import snowflake.connector
import pandas
streamlit.title("Zena's Amazing Athleisure Catalog")



Sweat_list = streamlit.selectbox("Select Sweat Clothings:", 
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
# Sweat_to_show = Sweat_list.loc[Sweat_listed]

streamlit.text(Sweat_list)

if Sweat_list == "90s tracksuit":
    streamlit.header("90s tracksuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/90s_tracksuit.png")

elif Sweat_list == "burgundy sweatsuit":
    streamlit.header("burgundy sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/burgundy_sweatsuit.png")

elif Sweat_list == "charcoal grey sweatsuit":
    streamlit.header("charcoal grey sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/charcoal_grey_sweatsuit.png")

elif Sweat_list == "forest green sweatsuit":
    streamlit.header("forest green sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/forest_green_sweatsuit.png")

elif Sweat_list == "navy blue sweatsuit":
    streamlit.header("navy blue sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/navy_blue_sweatsuit.png")

elif Sweat_list == "orange sweatsuit":
    streamlit.header("orange sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png")
elif Sweat_list == "purple sweatsuit":
    streamlit.header("purple sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/purple_sweatsuit.png")

elif Sweat_list == "red sweatsuit":
    streamlit.header("red sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/red_sweatsuit.png")

elif Sweat_list == "royal blue sweatsuit":
    streamlit.header("royal blue sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/royal_blue_sweatsuit.png")

elif Sweat_list == "yellow sweatsuit":
    streamlit.header("yellow sweatsuit")
    streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/yellow_sweatsuit.png")
else:
    streamlit.header("NO SELECTION!!! PLEASE SELECT!!!")

# streamlit.header("90s tracksuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/90s_tracksuit.png")


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


