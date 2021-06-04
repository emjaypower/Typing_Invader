import arcade
import random
import pathlib  # I edited this line
ENEMY_SPEED = 2
from arcade.sprite_list import check_for_collision
# This margin controls how close the enemy gets to the left or right side
# before reversing direction.
ENEMY_VERTICAL_MARGIN = 15
SPRITE_SCALING_enemy = 0.5
# RIGHT_ENEMY_BORDER = 0 - ENEMY_VERTICAL_MARGIN
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN

# How many pixels to move the enemy down when reversing
ENEMY_MOVE_DOWN_AMOUNT = 30


WORDS_PATH = pathlib.Path("assets/words.txt")  # I edited this line
WORDS_PATH = WORDS_PATH.absolute()
FULL_WORDS_PATH = pathlib.Path("/Users/McIntyre 1/PycharmProjects/Typing_Invader/assets/words.txt")

CITY_PATH = pathlib.Path("~/PycharmProjects/Typing_Invader/assets/city.png")  # I edited this line
ASSETS_PATH = pathlib.Path("~/PycharmProjects/Typing_Invader/assets")  # I edited this line


class Enemy(arcade.Window):

    def __init__(self):

        # Variables that will hold sprite lists
        self.enemy_list = arcade.SpriteList()

        # Textures for the enemy
        self.enemy_textures = None

        # Enemy movement
        self.enemy_change_x = -ENEMY_SPEED

        self.right_enemy_border = - ENEMY_VERTICAL_MARGIN

        # Edits start here
        # This class could be more acurately called enemies. this controls all enemies
        # instead of each individual enemy.
        # self.text = "Big string"
        # self.center_x = random.randint(0, 400)
        # self.center_y = random.randint(0, 400)
        # Edits end here

    def set_width(self, width):
        self.right_enemy_border += width

    # Edits start here
    def set_text(self):
        with open (f"{FULL_WORDS_PATH}") as file:  # (f"{ASSETS_PATH}/words.txt") as file:  # fix the path so it works on all platforms using path module
            word_list = file.readlines()
            max_index = len(word_list) - 1
            # possibly add a difficulty modifier here, specifying what length of word to grab
            selected_word = word_list[random.randint(0, max_index)]
        return selected_word


    def draw_string(self, obj):
        text = f"{obj.text}"
        arcade.draw_text(text,
                         start_x=obj.center_x,  # constants.HEALTH_NUMBER_OFFSET_X,
                         start_y=obj.center_y,  # constants.HEALTH_NUMBER_OFFSET_Y,
                         font_size=15,
                         color=arcade.color.GOLD)
        # print(obj.text)


    # def on_draw(self):
        # for enemy in self.enemy_list:
            # self.draw_string(enemy)



    # Edits end here

    def load_enemy(self):
        # Load the textures for the enemies, one facing left, one right
        self.enemy_textures = []
        texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_green.png", mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_green.png")
        self.enemy_textures.append(texture)

        # Create rows and columns of enemies
        x_count = 7
        x_start = 380
        x_spacing = 100
        y_count = 1
        y_start = 600
        y_spacing = 40
        for x in range(x_start, x_spacing * x_count + x_start, x_spacing):
            for y in range(y_start, y_spacing * y_count + y_start, y_spacing):
                # Create the enemy instance
                # enemy image from kenney.nl
                enemy = Enemy2(self.set_text())
                # enemy.draw_string()  ##### recent edit
                # Edits start here
                enemy.text = self.set_text()
                # Edits end here
                # enemy = arcade.Sprite()  ##### recent edit
                # enemy._set_alpha("bob")
                enemy.scale = SPRITE_SCALING_enemy
                enemy.texture = self.enemy_textures[1]

                # Position the enemy
                enemy.center_x = x
                enemy.center_y = y
                enemy.angle = 180


                # Add the enemy to the lists
                self.enemy_list.append(enemy)
    
    def setup(self):
        # self.enemy_list = arcade.SpriteList()
        return self.enemy_list

    def collision_detect(self, player):
        hit_list = []
        hit_list = arcade.check_for_collision_with_list(player, self.enemy_list)
        # if len(hit_list) > 0:
        #     self.enemy_list.remove_from_sprite_lists()
        for enemy in hit_list:
            enemy.remove_from_sprite_lists()
        return  

    def update_enemies(self, player):
        # Move the enemy vertically
        for enemy in self.enemy_list:
            # arcade.draw_text(F'LIVES: Work, play, and a lot of work', 400 - 100, 200, arcade.color.WHITE,
            #                  font_size=40, anchor_x="center")
            # enemy.draw_string()
            print(enemy.text)
            enemy.center_x += self.enemy_change_x

        # Check every enemy to see if any hit the edge. If so, reverse the
        # direction and flag to move down.
        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > self.right_enemy_border and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        # Did we hit the edge above, and need to move t he enemy down?
        if move_down:
            # Yes
            for enemy in self.enemy_list:
                # Move enemy down
                enemy.center_y -= ENEMY_MOVE_DOWN_AMOUNT
                # Flip texture on enemy so it faces the other way
                if self.enemy_change_x > 0:
                    enemy.texture = self.enemy_textures[0]
                else:
                    enemy.texture = self.enemy_textures[1]
        self.collision_detect(player)
        
 


class Enemy2(arcade.Sprite):
    def __init__(self, text):
        super().__init__()
        self.text = text


    def draw_string(self):
        text = f"{self.text}"
        arcade.start_render()
        arcade.draw_text(text, self.center_x, self.center_y, arcade.color.BLACK,
                         font_size=40)
        arcade.finish_render()

        """arcade.draw_text(text,
                         start_x=self.center_x + 50,
                         start_y=self.center_y + 50,
                         font_size=15,
                         color=arcade.color.WHITE)"""
        # arcade.finish_render()
