import pygame

pygame.init()


char_bubble_waffle = {
    # 0 for bubble waffle,  1 for bubble chocolate, 2 for green bubble tea, 3 for bubble gum
    'effect' : 0,
    # between 1 and 0
    'multiplier' : 0.5, 

    'win_quote' : 'That was a nice try... punk.',
    'effect_description' : "Blow up your foe's board!", 
    'character_description' : "The raging beast - Bubble Waffle \nDon't mess with Bubble Waffle, \nhe tastes extra aggresive today! \n Skill - Blow up your foe's board!", 

    'neutral_sprite' : 'source/art/0_idle.png',
    'hit_sprite' : 'source/art/0_hurt.png',
    'attack_sprite' : 'source/art/0_attack.png', 
    'bar_sprite' : 'source/art/0_border.png',
    'progression_meter_sprite' : 'source/art/0_uncharged.png', 
    'charged_meter_sprite' : 'source/art/0_charged.png', 

    'colour_rgb' : (255, 252, 227)
}

char_bubble_chocolate = {
    # 0 for bubble waffle,  1 for bubble chocolate, 2 for green bubble tea, 3 for bubble gum
    'effect' : 1,
    # between 1 and 0
    'multiplier' : 1.0, 

    'win_quote' : 'You couldn\'t even beat half of us!',
    'effect_description' : "Switch your board with the foe!", 
    'character_description' : "The tricksters - Bubble Chocolates \nWant double the trouble? \nBubble Chocolate twins are here!\n Skill - Switch your board with the foe!", 

    'neutral_sprite' : 'source/art/1_idle.png',
    'hit_sprite' : 'source/art/1_hurt.png',
    'attack_sprite' : "source/art/1_attack.png", 
    'bar_sprite' : 'source/art/1_border.png',
    'progression_meter_sprite' : 'source/art/1_uncharged.png', 
    'charged_meter_sprite' : 'source/art/1_charged.png', 

    'colour_rgb' : (255, 227, 227)
}

char_bubble_tea = {
    # 0 for bubble waffle,  1 for bubble chocolate, 2 for green bubble tea, 3 for bubble gum
    'effect' : 2,
    # between 1 and 0
    'multiplier' : 1.0, 

    'win_quote' : 'T-thanks for going easy on me...',
    'effect_description' : "Random Powerup!", 
    'character_description' : "The shy pop - Bubble Tea \nOne cute matcha bubble tea with the \nbest pearls in town, please!\n Skill - Random Powerup!", 

    'neutral_sprite' : 'source/art/2_idle.png',
    'hit_sprite' : 'source/art/2_hurt.png',
    'attack_sprite' : "source/art/2_attack.png", 
    'bar_sprite' : 'source/art/2_border.png',
    'progression_meter_sprite' : 'source/art/2_uncharged.png', 
    'charged_meter_sprite' : 'source/art/2_charged.png', 

    'colour_rgb' : (228, 255, 227)
}

char_bubble_gum = {
    # 0 for bubble waffle,  1 for bubble chocolate, 2 for green bubble tea, 3 for bubble gum
    'effect' : 3,
    # between 1 and 0
    'multiplier' : 0.5, 

    'win_quote' : 'Move aside plebeian!',
    'effect_description' : "Autosolves 3 rows!", 
    'character_description' : "The bubble queen - Bubble Gum \nThe sassiest pink bubble gum from the \nsweetest gumball machine you'll ever meet!\n Skill - Autosolves 3 rows!", 

    'neutral_sprite' : 'source/art/3_idle.png',
    'hit_sprite' : 'source/art/3_hurt.png',
    'attack_sprite' : "source/art/3_attack.png", 
    'bar_sprite' : 'source/art/3_border.png',
    'progression_meter_sprite' : 'source/art/3_uncharged.png', 
    'charged_meter_sprite' : 'source/art/3_charged.png', 

    'colour_rgb' : (239, 227, 255)
}

# Screen dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
ORANGE = (255,127,80)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Font
text_font = pygame.font.SysFont(None, 100)

# Initialize screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg = pygame.image.load('source/art/bg_dark.png')
win = pygame.mixer.Sound('source/music/win.mp3')


# Winner is a character
def end_screen(winner):
    win.play()
    global text
    start_time = pygame.time.get_ticks()
    current = True
    text = text_font.render(winner['win_quote'], True, winner["colour_rgb"])
    while current:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current= False
        screen.blit(bg, (0,0))

        if winner["neutral_sprite"]:
            sprite = pygame.image.load(winner["neutral_sprite"])
            screen.blit(sprite, (-400,0))

        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        text_rect.right = WINDOW_WIDTH
        screen.blit(text, text_rect)
        if pygame.time.get_ticks() - start_time > 5000:
            current = False
        pygame.display.update()
    
    pygame.QUIT()

        