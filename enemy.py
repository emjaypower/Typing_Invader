import arcade
import random
ENEMY_SPEED = 2
# This margin controls how close the enemy gets to the left or right side
# before reversing direction.
ENEMY_VERTICAL_MARGIN = 15
SPRITE_SCALING_enemy = 0.5
# RIGHT_ENEMY_BORDER = 0 - ENEMY_VERTICAL_MARGIN
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN

# How many pixels to move the enemy down when reversing
ENEMY_MOVE_DOWN_AMOUNT = 30

class Enemy(arcade.Window):

    def __init__(self):

        # Variables that will hold sprite lists
        self.enemy_list = arcade.SpriteList()

        # Textures for the enemy
        self.enemy_textures = None

        # Enemy movement
        self.enemy_change_x = -ENEMY_SPEED

        self.right_enemy_border = - ENEMY_VERTICAL_MARGIN

    def set_width(self, width):
        self.right_enemy_border += width

    def load_enemy(self):
        # Load the textures for the enemies, one facing left, one right
        self.enemy_textures = []
        texture = arcade.load_texture(":resources:images/enemies/slimeBlue.png", mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture(":resources:images/enemies/slimeBlue.png")
        self.enemy_textures.append(texture)

        # Create rows and columns of enemies
        x_count = 7
        x_start = 380
        x_spacing = 60
        y_count = 5
        y_start = 420
        y_spacing = 40
        for x in range(x_start, x_spacing * x_count + x_start, x_spacing):
            for y in range(y_start, y_spacing * y_count + y_start, y_spacing):
                # Create the enemy instance
                # enemy image from kenney.nl
                enemy = arcade.Sprite()
                # enemy._set_alpha("bob")
                enemy.scale = SPRITE_SCALING_enemy
                enemy.texture = self.enemy_textures[1]

                # Position the enemy
                enemy.center_x = x
                enemy.center_y = y

                # Add the enemy to the lists
                self.enemy_list.append(enemy)
    
    def setup(self):
        # self.enemy_list = arcade.SpriteList()
        return self.enemy_list

    def update_enemies(self):
        # Move the enemy vertically
        for enemy in self.enemy_list:
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

