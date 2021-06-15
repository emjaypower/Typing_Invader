import arcade

def draw_enemy_text(enemy_list):
    for enemy in enemy_list:
        arcade.draw_text(enemy.text, enemy.center_x - 25, enemy.center_y + 15, arcade.color.WHITE, font_size=(25 - round(len(enemy.text)/1.25)))