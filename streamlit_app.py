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

#making constants that we need
RUNNING=[pygame.image.load(os.path.join('./Assets/Dino','DinoRun1.png')),pygame.image.load(os.path.join('./Assets/Dino','DinoRun2.png'))]

JUMPING=pygame.image.load(os.path.join('./Assets/Dino','DinoJump.png'))

DUCKING=[pygame.image.load(os.path.join('./Assets/Dino','DinoDuck1.png')), pygame.image.load(os.path.join('./Assets/Dino','DinoDuck2.png'))]


class Dinosaur:
    xpos=50
    ypos=350
    ypos_duck=400
    JUMPV=8.5
    def __init__(self):
        self.duck_img=DUCKING
        self.run_img=RUNNING
        self.jump_img=JUMPING

        self.dino_duck=False
        self.dino_jump=False
        self.dino_run=True 

        self.step_index=0

        self.image=self.run_img[0]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x= self.xpos
        self.dino_rect.y= self.ypos 
        self.jump_vel=self.JUMPV

    def update(self, userInp):
        
        if(self.dino_duck):
            self.duck()
        if(self.dino_jump):
            self.jump()
        if(self.dino_run):
            self.run()

        if(self.step_index>=10):
            self.step_index=0

      
        if userInp[pygame.K_UP] and not self.dino_jump:
            self.dino_jump=True
            self.dino_duck=False 
            self.dino_run=False
        elif userInp[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck=True
            self.dino_jump=False 
            self.dino_run=False 
        elif not (self.dino_jump or  userInp[pygame.K_DOWN]):
            self.dino_jump=False 
            self.dino_duck=False
            self.dino_run=True
       
        
            
    def duck(self):
        self.image=self.duck_img[self.step_index // 5]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.xpos
        self.dino_rect.y=self.ypos_duck
        self.step_index+=1 
    
    def jump(self):
        # self.image=self.jump_img
        
        if(self.dino_jump):
            self.dino_rect.y -= (self.jump_vel*4)
            self.jump_vel -= 0.9 
            
        
        if(self.jump_vel < -self.JUMPV):
            self.dino_jump=False 
            self.jump_vel=self.JUMPV


       
             
    
    def run(self):
        self.image=self.run_img[self.step_index // 5] 
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.xpos
        self.dino_rect.y=self.ypos 
        self.step_index+=1    
    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))
