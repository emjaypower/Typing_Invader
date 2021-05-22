import arcade
import random
from enemy import Enemy

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Typing Invader"

class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()
        self.game_over = False
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.player_list = None
        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.enemies = Enemy()
        self.enemies.set_width(SCREEN_WIDTH)
        self.enemies.load_enemy()
        # Our physics engine
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.WHITE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.background = arcade.load_texture("space_type/assets/rsz_emfutr.png")
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        # Create player
        # image_source = "space_type/assets/pirate.png"
        self.player_sprite = arcade.Sprite("space_type/assets/pirate.png", 1)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)
        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        # Create enemey
        self.enemy_list = self.enemies.setup()

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()
        # enemy draw
        self.enemy_list.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.ENTER:
            self.game_over = True

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()
        #
        self.enemies.update_enemies()

        if self.game_over:
            end = gameOver()
            self.window.show_view(end)
            #
        if len(self.enemies.enemy_list) == 0:
            self.enemies.load_enemy()

class Sounds:
    
    def __init__(self):
        """This class holds all of the sounds that we are going to be using, including sound effects
           and songs for various parts of the game"""
        self.volume = 20
        self.sounds = {"main_1":"IceBlizzard.wav"}
    
    def play_sound(self, sound):
        arcade.Sound(self.sounds[sound]).play(volume=self.volume)

class mainMenu(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ANTIQUE_RUBY)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Typing Invader", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLACK, 
                        font_size=75, anchor_x="center")
        arcade.draw_text("CLICK TO START", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 -50, arcade.color.BLACK, 
                        font_size=40, anchor_x="center")
        
    def on_mouse_press(self,_x,_y,_button,_modifiers):
        game = MyGame()
        game.setup()
        self.window.show_view(game)

class gameOver(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ANTIQUE_RUBY)
        self.output = "Game"

    def on_draw(self):
        arcade.start_render()
        arcade.set_viewport(0, SCREEN_WIDTH,0, SCREEN_HEIGHT)
        arcade.draw_text(self.output, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLACK, 
                        font_size=75, anchor_x="center")
        arcade.draw_xywh_rectangle_filled(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT/2 - 50,200,50,arcade.color.BLACK)
        arcade.draw_text("RESTART", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50, arcade.color.WHITE, 
                        font_size=40, anchor_x="center")

    def on_mouse_press(self,_x,_y,_button,_modifiers):
        if _x < SCREEN_WIDTH/2 + 100 and _x > SCREEN_WIDTH/2 - 100 and _y < SCREEN_HEIGHT/2 and _y > SCREEN_HEIGHT/2 - 50:
            menu = mainMenu()
            self.window.show_view(menu)


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = mainMenu()
    window.show_view(menu)
    hand_sound = arcade.load_sound("space_type\IceBlizzard.wav")
    arcade.play_sound(hand_sound)
    arcade.run()


if __name__ == "__main__":
    main()