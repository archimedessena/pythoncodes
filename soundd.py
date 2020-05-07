# understand sound
import pygame
soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()
import time
time.sleep(1)
soundObj.stop()