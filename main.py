import pygame, sys
from pygame.locals import *

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
p1 = []
p2 = []


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



def make_text_left(text, color, spacing): # For creating the text in the first line
    global WHITE, BLACK
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    textSurfaceObj = fontObj.render(text, True, color, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (spacing, 0)
    return(textSurfaceObj, textRectObj)

def make_text_right(text): # For creating the text at the buttom line
    global WHITE, BLACK
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    textSurfaceObj = fontObj.render(text, True, RED, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.bottomright = (590, 190)
    return(textSurfaceObj, textRectObj)

def result(text): # For creating the text of the result at the middle
    global WHITE, GREEN
    clear_SURF, clear_RECT = make_text_right("                             ")
    DISPLAYSURF.blit(clear_SURF, clear_RECT)
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    textSurfaceObj = fontObj.render(text, True, GREEN, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.midleft = (0, 120)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

def display_score(): # For displaying the score after each turn at the middle
    global WHITE, BLACK
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    textSurfaceObj = fontObj.render('Player 1: ' + str(p1) + '  Player 2: ' + str(p2), True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (0, 50)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def create_REC(): # For displaying and creating the rectangles of the cards
    cards_REC = []
    spacing = 120
    for card in cards:
        card_SURF, card_RECT = make_text_left(str(card), BLUE, spacing)
        DISPLAYSURF.blit(card_SURF, card_RECT)
        cards_REC.append(card_RECT)
        spacing += 12 
    return cards_REC

def play(turn):
    global cards
    turn_SURF, turn_RECT = make_text_right(turn)
    DISPLAYSURF.blit(turn_SURF, turn_RECT) # To show the current turn
    display_score()
    cards_REC = create_REC() # To Update the display the cards 
    end_turn = True
    while(end_turn):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for card in cards: # To check if the user pressed any of the cards
                    index = cards.index(card)
                    if card.isdigit():
                        if cards_REC[index].collidepoint(mouse_pos):
                            cards[index] = ' - ' # To replace tha card with a dash
                            return card
            pygame.display.update()


def main():
    global cards, DISPLAYSURF, p1, p2
    DISPLAYSURF = pygame.display.set_mode((600, 200))
    pygame.display.set_caption('Scrablle Game')
    DISPLAYSURF.fill(WHITE)
    pygame.init() # Setting the window
    numbers_SURF, numbers_RECT = make_text_left("Numbers left: ", BLACK, 0)
    DISPLAYSURF.blit(numbers_SURF, numbers_RECT)
    end = False
    while(True):
        if end == False:
            for turn in ['Players 1 turn!', 'Players 2 turn!']:
                card = play(turn)
                if turn == 'Players 1 turn!':
                    p1.append(card)
                    if len(p1) > 2: # Check if the player has won
                       for i in range (0, len(p1) - 2):
                                # second number
                                for j in range (i + 1 , len(p1) - 1):
                                    # third number
                                    for k in range (j + 1 , len(p1)):
                                        # check if their sum is 15
                                        if int(p1[i]) + int(p1[j]) + int(p1[k]) == 15:
                                            result('Player 1 wins!')
                                            end = True
                                            break

                elif turn == 'Players 2 turn!':
                    p2.append(card)
                    if len(p2) > 2:
                        for i in range (0, len(p2) - 2):
                                # second number
                                for j in range (i + 1 , len(p2) - 1):
                                    # third number
                                    for k in range (j + 1 , len(p2)):
                                        # check if their sum is 15
                                        if int(p2[i]) + int(p2[j]) + int(p2[k]) == 15:
                                            result('Player 2 wins!')
                                            end = True
                                            break
                if end:
                    break

                draw = True # To check if it is a draw game
                for card in cards:
                    if card.isdigit():
                        draw = False
                if draw:
                    result("Draw!")
                    break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        display_score()
        pygame.display.update()
        
                  
if __name__ == '__main__':
    main()