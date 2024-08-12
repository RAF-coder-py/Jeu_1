import os
import pygame as py
from game import Game
from rectangles import Green_Rectangle, White_Rectangle

width = 800
height = 600
background = py.image.load('pictures/background.png')
background = py.transform.scale(background, (width + 500, height))
clock = py.time.Clock()
frequence = 60



def main():

    running = True
    game = Game()
    rotation = -1
    g_rectangle = Green_Rectangle()
    w_rectangle = White_Rectangle()

    while running:

#########################################   MOVE   ############################################
           
        keys = py.key.get_pressed()

        if keys[py.K_RIGHT] and keys[py.K_LEFT]:
            #do nothing
            print('je ne fait rien')
        
        elif keys[py.K_RIGHT]:
            game.player_move_right(game.player)
            rotation = 1

        elif keys[py.K_LEFT]:
            game.player_move_left(game.player)
            rotation = 0
        
#########################################   EVENTS   ############################################
        for event in py.event.get():

            if event.type == py.QUIT:
                running = False

            elif event.type == py.KEYDOWN:
                if rotation == 1 and event.key == py.K_LEFT:
                    game.player.turn()
                    rotation = -1
                    
                elif rotation == 0 and event.key == py.K_RIGHT:
                    game.player.turn()
                    rotation = -1

                elif event.key == py.K_UP:
                    game.player.jumping = True

                elif event.key == py.K_SPACE:
                    game.player.attack()
                    
        if game.player.jumping:
            game.player.jump()
            
#########################################   FIRE   ############################################
        for fire in game.player.all_fire:

            if fire.side == '':
                if rotation == 1 or rotation == -1:
                    fire.side = 'right'

                elif rotation == 0:
                    fire.side = 'left'

            elif fire.side == 'right':
                fire.move_right()

            else:
                if not fire.confirmed:
                    fire.rect.x = game.player.rect.x - 12 
                    fire.confirmed = True
                fire.move_left()
#########################################   DISPLAY   ############################################
        game.screen.blit(background, (0, 0))
        game.screen.blit(game.player.image,(game.player.rect.x,game.player.rect.y))
        py.draw.rect(game.screen, w_rectangle.color, (game.player.rect.x-3, game.player.rect.y - 33, w_rectangle.length, w_rectangle.height))
        py.draw.rect(game.screen, g_rectangle.color, (game.player.rect.x, game.player.rect.y - 30, int((game.player.health/game.player.original_health)*g_rectangle.length), g_rectangle.height))
        game.player.all_fire.draw(surface=game.screen) 
        py.display.set_caption('1st game')    
        py.display.flip()
        clock.tick(frequence)
        # print(keys[py.K_LEFT], keys[py.K_RIGHT])

    py.quit


if __name__ == '__main__':
    main()
    os.system('clear')