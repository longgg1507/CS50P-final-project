import pygame
import sys

def main():
    print(input_screen())

def input_screen():
    pygame.init()
    # Basic setting (screen, font, fps)
    screen = pygame.display.set_mode((500, 200))
    pygame.display.set_caption("Input")
    font = pygame.font.Font("backgrounds/Pixel.ttf", 48)
    clock = pygame.time.Clock()

    input_box = pygame.Rect(50, 80, 400, 50)
    # Creating color preset
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color('lightskyblue3')
    color = color_inactive
    active = False
    text = ''

    while True:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                    
                if active:
                    color = color_active
                else:
                    color = color_inactive

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    return text  # return typed input
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Render text
        txt_surface = font.render(text, True, color)
        width = max(400, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+10, input_box.y+10))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
        

if __name__ == "__main__":
    main()