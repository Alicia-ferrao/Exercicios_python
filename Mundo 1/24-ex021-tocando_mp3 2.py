
import pygame

# Inicializar o pygame
pygame.init()

# Carregar a música
pygame.mixer.music.load("exe1.mp3")

# Tocar a música
pygame.mixer.music.play()

# Loop para manter o programa rodando até a música acabar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    