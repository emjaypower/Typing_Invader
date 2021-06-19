import arcade 
import random
from game import MyGame
from game import Player
from enemy import Enemy


class levels():
    def __init(self):
        self.myG = MyGame()
        self.player = Player()
        self.enemy = Enemy()
        self.completed_Level = False
        self.level_number = 0

    def check_Level_up(self):
        if self.player.health > 0 and len(self.myG.enemy_list) == 0:
            self.completed_Level = True 
        else:
            return False

    def Level_Up(self):
        if self.check_Level_up:

           # Increase the enemy speed. 
            self.enemy_change_x -= 1

            # Reset player Health 
            self.player.health = 20
            
            # Keep track of the level they have made it to 
            self.level_number += 1

            # Reset the completed level boolean to false 
            self.completed_Level = False


        