import os
import pygame as py
from game import Game

width = 800
height = 600
background = py.image.load('pictures/background.png')
background = py.transform.scale(background, (width + 500, height))
clock = py.time.Clock()
frequence = 60



def main():

    running = True
    game = Game()

    while running:

#########################################   MOVE   ############################################
           
        keys = py.key.get_pressed()

        if keys[py.K_RIGHT] and keys[py.K_LEFT]:
            game.player_1.dont_move()
        
        elif keys[py.K_RIGHT]:
            game.player_move_right(game.player_1)
            game.player_1.image = game.player_1.image_left

        elif keys[py.K_LEFT]:
            game.player_move_left(game.player_1)
            game.player_1.image = game.player_1.image_right

        if keys[py.K_a] and keys[py.K_d]:
            game.player_2.dont_move()

        elif keys[py.K_d]:
            game.player_move_right(game.player_2)
            game.player_2.image = game.player_2.image_right

        elif keys[py.K_a]:
            game.player_move_left(game.player_2)
            game.player_2.image = game.player_2.image_left

        
#########################################   EVENTS   ############################################
        for event in py.event.get():

            if event.type == py.QUIT:
                running = False

            elif event.type == py.KEYDOWN:

                if event.key == py.K_UP:
                    game.player_1.jumping = True

                if event.key == py.K_SPACE:
                    game.player_1.attack()

                if event.key == py.K_w:
                    game.player_2.jumping = True

                if event.key == py.K_y:
                    game.player_2.attack()
                        
        if game.player_1.jumping:
            game.player_1.jump()

        if game.player_2.jumping:
            game.player_2.jump()
            
#########################################   FIRE  (player_1) ############################################

        for fire in game.player_1.all_fire:
            if not fire.given_side:
                if game.player_1.image == game.player_1.image_right:
                    fire.side = 'left'
                    fire.given_side = True

                elif game.player_1.image == game.player_1.image_left:
                    fire.side = 'right'
                    fire.given_side = True

            if fire.side == 'right':
                fire.move_right()

            else:
                if not fire.confirmed:
                    fire.rect.x = game.player_1.rect.x - 12 
                    fire.confirmed = True
                fire.move_left()

#########################################   FIRE  (player_2) ############################################

        for fire in game.player_2.all_fire:
            if not fire.given_side:
                if game.player_2.image == game.player_2.image_right:
                    fire.side = 'left'
                    fire.given_side = True

                elif game.player_2.image == game.player_2.image_left:
                    fire.side = 'right'
                    fire.given_side = True

            if fire.side == 'right':
                fire.move_right()

            else:
                if not fire.confirmed:
                    fire.rect.x = game.player_2.rect.x - 12 
                    fire.confirmed = True
                fire.move_left()

#########################################   DISPLAY   ############################################
        game.screen.blit(background, (0, 0))
        game.draw_player(game.player_1)
        game.draw_player(game.player_2)
        game.draw_rectangle(game.player_1)
        game.draw_rectangle(game.player_2)
        game.player_1.all_fire.draw(surface=game.screen) 
        py.display.set_caption('1st game')    
        py.display.flip()
        clock.tick(frequence)

    py.quit


if __name__ == '__main__':
    main()
    os.system('clear')