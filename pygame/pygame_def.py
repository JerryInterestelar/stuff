import pygame

def main():
    pygame.init()

    pygame.display.set_caption("teste")
    

    width = 1040
    height = 580
    screen = pygame.display.set_mode((width, height))
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
        main()
