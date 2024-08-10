import pygame as py
from game import Game



width = 800
height = 600
background = py.image.load('pictures/background.png')
background = py.transform.scale(background, (width + 500, height))
clock = py.time.Clock




def main():

    running = True
    game = Game()
    rotation = -1
    while running:
        

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
                elif event.key == py.K_SPACE:
                    print(1)
                    
                    

        keys = py.key.get_pressed()
        
        if keys[py.K_RIGHT]:
            game.player_move_right()
            rotation = 1

        elif keys[py.K_LEFT]:
            game.player_move_left()
            rotation = 0

    
        game.screen.blit(background, (0, 0))
        game.screen.blit(game.player.image,(game.player.rect.x,game.player.position_y))
        py.display.set_caption('1st game')    
        py.display.flip()

    py.quit


if __name__ == '__main__':
    main()