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




streamlit.subheader ('By: Chef Bert Lagro')
streamlit.video("https://youtu.be/EdSLy-CyHes", format='video/mp4', start_time=0)


import pygame 
import os
import random 

CLOUDS=pygame.image.load(os.path.join('./Assets/Other','Cloud.png'))

class Cloud:

   def __init__(self,gamespeed,screen_width) :
       self.gamespeed=gamespeed 
       self.image= CLOUDS       
       self.rect = self.image.get_rect()
       self.screen_width=screen_width 
       self.x=self.screen_width+random.randint(300,1000)
       self.y=random.randint(150,250)
       
   
   def update(self):
       
       self.x-=self.gamespeed
       if(self.x < self.rect.x):
            self.x=self.screen_width+random.randint(300,1000)
            self.y=random.randint(150,250)
   def draw(self,screen):
       screen.blit(self.image,(self.x,self.y))


