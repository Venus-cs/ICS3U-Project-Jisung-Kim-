import pygame, sys, typing_game_wordlists

# Colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)    # For incorrect characters
GREEN = (0, 255, 0)  # For correct characters
BLUE = (0, 0, 255)   # For correct words
MAGENTA = (255, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def typing_game():
    # Initialize fonts inside the function to ensure pygame is initialized
    words_font = pygame.font.Font("Comic Sans MS Bold.ttf", 36)

    # ...existing code...
    input_text = ""
    input_rect = pygame.Rect(100, 100, 600, 80)
    active = False
    limited_number = 20
    words_number = 1
    score = 0
    target_word = typing_game_wordlists.random_English_word()
    success = False
    start_time = pygame.time.get_ticks()  # Start the timer for the first word
    timer_per_word = len(target_word) * 1000  # 1 second per character
    wait_start_time = 0  # Initialize wait start time

    while words_number <= limited_number:
        current_time = pygame.time.get_ticks()
        remaining_time = max(0, timer_per_word - (current_time - start_time))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif len(input_text) < len(target_word) and event.unicode.isprintable():
                    input_text += event.unicode

        # Check if the input matches the target word
        if input_text == target_word and not success:
            success = True
            wait_start_time = pygame.time.get_ticks()  # Start the wait timer
            score += 1
            words_number += 1

        # Move to the next word after the wait or if time runs out
        if (success and pygame.time.get_ticks() - wait_start_time >= 1000) or remaining_time == 0:
            success = False
            input_text = ""
            target_word = typing_game_wordlists.random_English_word()
            timer_per_word = len(target_word) * 1000  # Recalculate timer for the new word
            start_time = pygame.time.get_ticks()  # Reset the timer for the new word

        # Clear the screen
        screen.fill(WHITE)

        # Draw the input box
        pygame.draw.rect(screen, BLACK if active else GREY, input_rect, 2)

        # Render the target word and score
        target_surface = words_font.render(f"Type this: {target_word}", True, BLACK)
        screen.blit(target_surface, (100, 50))
        score_surface = words_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surface, (600, 500))

        # Render the timer
        timer_width = 800 * (remaining_time / timer_per_word)
        timer_surface = pygame.Surface((timer_width, 100))  # Pass a tuple for width and height
        timer_surface.fill(MAGENTA)
        screen.blit(timer_surface, (0, 700))

        # Draw input text
        if success:
            word_surface = words_font.render(input_text, True, BLUE)
            screen.blit(word_surface, (input_rect.x + 10, input_rect.y + 10))
            correct_surface = words_font.render("Correct!", True, BLACK)
            screen.blit(correct_surface, (100, 200))
        else:
            for i, char in enumerate(input_text):
                color = GREEN if i < len(target_word) and char == target_word[i] else RED
                char_surface = words_font.render(char, True, color)
                screen.blit(char_surface, (input_rect.x + 10 + i * 35, input_rect.y + 10))

        # Update the display
        pygame.display.flip()
        clock.tick(60)
