# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():
    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here

    background_position = [0, 0]

    background_image = pygame.image.load("C:\images\saturn_family1.jpg").convert()
    player_image = pygame.image.load("C:\images\player.png").convert()         
    player_image.set_colorkey(config.BLACK)
    
    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        screen.blit(background_image, background_position)

        player_position = pygame.mouse.get_pos()
        x = player_position[0] - (player_image.get_width() / 2)
        y = player_position[1] - (player_image.get_height() / 2)

        screen.blit(player_image, [x,y])


        pygame.display.flip()
    # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



