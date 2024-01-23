import streamlit
import snowflake.connector
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog')

# streamlit.header("90s tracksuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/90s_tracksuit.png")

# streamlit.header("burgundy_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/burgundy_sweatsuit.png")

# streamlit.header("charcoal_grey_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/charcoal_grey_sweatsuit.png")

# streamlit.header("forest_green_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/forest_green_sweatsuit.png")

# streamlit.header("navy_blue_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/navy_blue_sweatsuit.png")

# streamlit.header("orange_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png")

# streamlit.header("purple_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/purple_sweatsuit.png")

# streamlit.header("red_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/red_sweatsuit.png")

# streamlit.header("royal_blue_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/royal_blue_sweatsuit.png")

# streamlit.header("yellow_sweatsuit")
# streamlit.image("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/yellow_sweatsuit.png")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
# CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
