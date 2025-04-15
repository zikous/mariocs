import os
from pygame.locals import *
from pygame import mixer

# Initialize pygame mixer
mixer.init()

def music(path, volume):
    """
    Joue la musique du chemin spécifié avec un volume donné.

    Args:
    path (str): Chemin vers la musique à jouer.
    volume (float): Volume de lecture de la musique (entre 0.0 et 1.0).

    Returns:
    None
    """
    if not os.path.exists(path):
        print(f"Error: Sound file '{path}' not found.")
        return
    sound = mixer.Sound(path)
    sound.set_volume(volume)
    sound.play()
