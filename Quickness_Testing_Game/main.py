import pygame, sys
from typing_game import typing_game

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0) 
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
IVORY = (255, 255, 128)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.Font("Comic Sans MS Bold.ttf", 48)
words_font = pygame.font.Font("Comic Sans MS Bold.ttf", 36)
button_font = pygame.font.Font("Comic Sans MS Bold.ttf", 24)

# Title
title_surface = title_font.render("Quickness Testing Games", True, BLACK)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hovered_color):
        # Initialize the button's rectangle, text, colors, and hover state
        self.rect = pygame.Rect(x, y, width, height)  # The button's rectangular area
        self.text = text  # The text displayed on the button
        self.color = color  # The default color of the button
        self.hovered_color = hovered_color  # The color when the button is hovered
        self.is_hovered = False  # Tracks whether the mouse is hovering over the button

    def draw(self, surface):
        # Draw the button on the given surface
        if self.is_hovered:
            color = self.hovered_color  # Use hovered color if hovered
        else:
            color = self.color  # Use default color if not hovered
        pygame.draw.rect(surface, color, self.rect, border_radius=10)  # Draw the button rectangle
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)  # Draw the border of the button
        
        # Render the button's text and center it within the button
        text_surface = button_font.render(self.text, True, BLACK)  # Render the text
        text_rect = text_surface.get_rect(center=self.rect.center)  # Center the text in the button
        surface.blit(text_surface, text_rect)  # Draw the text on the button

    def check_hover(self, pos):
        # Check if the mouse is hovering over the button
        self.is_hovered = self.rect.collidepoint(pos)  # Update hover state
        return self.is_hovered  # Return whether the button is hovered

    def is_clicked(self, pos, event):
        # Check if the button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button click (= 1)
            return self.rect.collidepoint(pos)  # Return True if the click is inside the button
        return False  # Otherwise, return False

# Start button
typing_game_button = Button(300, 400, 200, 80, "Typing game", CYAN, BLUE)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if the start button is clicked
        if typing_game_button.is_clicked(pygame.mouse.get_pos(), event):
            typing_game()

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is hovering over the start button
    typing_game_button.check_hover(mouse_pos)

    # Clear the screen
    screen.fill(IVORY)

    # Draw the title
    screen.blit(title_surface, (110, 100))

    # Draw the start button
    typing_game_button.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)