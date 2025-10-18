import pygame

GREY=(220,220,220)
NEGRO=(10,10,10)
GRIS_ACTIVO=(245,245,245)
GRIS_NORMAL=(169,169,169)
BLANCO=(255, 255, 255)

MARGEN=5 #ancho del borde entre celdas
MARGEN_DERECHO=125 #ancho del margen derecho entre la cuadrícula y la ventana
TAM=60  #tamaño de la celda
N=9 # número de filas del sudoku
VACIA='0'

def pintarVentana(screen):
    pygame.draw.rect(screen, GREY, [0, 0, N*(TAM+MARGEN)+MARGEN, N*(TAM+MARGEN)+MARGEN],0)

def main():
    pygame.init()
    
    
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

    

if __name__ == "__main__":
    main()