import pygame
import sys


def main():
    print_screen("night_time","31°C","Snowy","2025-07-03","16:51")
    
    
def print_screen(sky,temperature,condition,date,time):
    #graphic preset
    if sky == "day_time":
        background = "backgrounds/daytime_clearsky.jpg"
        text_color = "Orange"
    elif sky == "night_time":
        background = "backgrounds/nighttime_clearsky.jpg"
        text_color = "White"
        
    pygame.init()

    # Screen settings
    screen_size = (500,300)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Output")

    # Background set
    background_image = pygame.image.load(background)
    background_image = pygame.transform.scale(background_image,screen_size)

    # Font settings
    temp_font = pygame.font.SysFont("Arial", 65)
    font = pygame.font.Font("backgrounds/Pixel.ttf", 60)
    
    # TEXTS
    temp_text = temp_font.render(temperature, True, text_color) # TEMPERATURE
    temp_rect = temp_text.get_rect(bottomright=(480,240))
    
    cond_text = font.render(condition, True, text_color)
    cond_rect = cond_text.get_rect(bottomright=(480,280)) # CONDITION
    
    date_text = font.render(date, False, text_color) # DATE
    date_rect = date_text.get_rect(topright=(480,75))
    
    time_text = font.render(time, False, text_color) # TIME
    time_rect = time_text.get_rect(topright=(480,20))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background
        screen.blit(background_image, (0, 0))

        # Draw text
        screen.blit(temp_text, temp_rect)
        screen.blit(cond_text, cond_rect)
        screen.blit(time_text, time_rect)
        screen.blit(date_text, date_rect)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    main()