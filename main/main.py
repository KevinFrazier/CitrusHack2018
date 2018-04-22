#def run_menu():
import pygame
import main_selection
from pygame.locals import *
import time
import random

pygame.init()

def run_menu():
    #background image size
    background_width = 900
    background_height = 506

    #shortcut colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    title_color = (142, 42, 43)
    start_color = (238, 208, 156)
    brighter_red = (172, 32, 35)
    darker_red = (122, 0, 38)

    #placement of title
    title_height = (background_height*0.45)
    title_width = (background_width*0.8)

    endgame = False

    # loads images
    background_img = pygame.image.load("background.png")  # You need an example picture in the same folder as this file!
    start_img = pygame.image.load("startgame.png")
    megaocto = pygame.image.load("megaocto.png")
    octoninja = pygame.image.load("octoninja.png")
    ironcat = pygame.image.load("ironcat.png")

    #setting the screen
    screen = pygame.display.set_mode((background_width,background_height))
    screen.blit(pygame.transform.scale(background_img, (background_width, background_height)), (0, 0))
    pygame.display.flip()

    text_font = pygame.font.Font('m5x7.ttf', 35)
    title_font = pygame.font.Font('Fipps-Regular.otf', 30)
    menu_font = pygame.font.Font('m5x7.ttf', 50)

    pygame.display.set_caption('Game #1')
    clock = pygame.time.Clock()

    def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect(),

    # def button(msg, x, y, w, h, ic, ac, f, action=None):
    #     mouse = pygame.mouse.get_pos()
    #     click = pygame.mouse.get_pressed()
    #     print(click)
    #     if x + w > mouse[0] > x and y + h > mouse[1] > y:
    #         TextSurf, TextRect = text_objects(msg, f, ac)
    #         TextRect.center = ((background_width*.65), (background_height*.65))
    #         screen.blit(TextSurf, TextRect)
    #
    #         if click[0] == 1 and action != None:
    #             action()
    #
    #     else:
    #         TextSurf, TextRect = text_objects(msg, f, ic)
    #         TextRect.center = ((background_width * .65), (background_height * .65))
    #         screen.blit(TextSurf, TextRect)

    def game_intro():
        while not endgame:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # elif event.type == VIDEORESIZE:
                #    screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                #    screen.blit(pygame.transform.scale(background_img, event.dict['size']), (0, 0))
                #    pygame.display.flip()

            #TextSurf, TextRect = text_objects("", title_font, title_color)
            #TextRect.center = ((background_width / 2), (background_height / 2))
            #screen.blit(TextSurf, TextRect)

            #screen.blit(pygame.transform.scale(start_img, (150, 44)), (336, 301))
            #button("Start Game", 370, 285, 150, 43, brighter_red, darker_red, text_font, game_selection)
            #pygame.draw.rect(screen, brighter_red, (370, 285, 150, 43))


            #click = pygame.mouse.get_pressed()
            #print(click)

            #start_game_click()

                #when user clicks "Start Game" > Time to choose player
                #if click[0] == 1:
                #    choose_heroes()
                #pygame.event.get()
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(white)
                pygame.draw.rect(screen, white, (370, 285, 150, 43))
                select_char()

            pygame.display.flip()
            clock.tick(15)

    def select_char():

        text_font = pygame.font.Font('m5x7.ttf', 35)
        TextSurf, TextRect = text_objects("Select Character:", title_font, title_color)
        TextRect.center = ((background_width /2), (background_height * .15))
        screen.blit(TextSurf, TextRect)

        #character1
        text_font = pygame.font.Font('m5x7.ttf', 35)
        TextSurf, TextRect = text_objects("MegaOcto", menu_font, start_color)
        TextRect.center = ((background_width * .25), (background_height * .35))
        screen.blit(TextSurf, TextRect)

        #screen.blit(megaocto, (background_width * .25), (background_height * .35))

        #character2
        text_font = pygame.font.Font('m5x7.ttf', 35)
        TextSurf, TextRect = text_objects("IronCat", menu_font, start_color)
        TextRect.center = ((background_width * .5), (background_height * .35))
        screen.blit(TextSurf, TextRect)

        #screen.blit(ironcat, (background_width * .5), (background_height * .35))

        #character3
        text_font = pygame.font.Font('m5x7.ttf', 35)
        TextSurf, TextRect = text_objects("OctoNinja", menu_font, start_color)
        TextRect.center = ((background_width * .75), (background_height * .35))
        screen.blit(TextSurf, TextRect)

        #screen.blit(octoninja, (background_width * .75), (background_height * .35))

        pygame.draw.rect(screen, start_color, (370, 375, 165, 55))

        mouse = pygame.mouse.get_pos()
        if 370 + 150 > mouse[0] > 150 and 285 + 43 > mouse[1] > 43:
            TextSurf, TextRect = text_objects("Ready", title_font, title_color)
            TextRect.center = ((background_width * 0.5), (background_height * .8))
            screen.blit(TextSurf, TextRect)
        else:
            TextSurf, TextRect = text_objects("Ready", title_font, black)
            TextRect.center = ((background_width * 0.5), (background_height * .8))
            screen.blit(TextSurf, TextRect)

            screen.fill(white)

        pygame.display.update()
        clock.tick(60)


    TextSurf, TextRect = text_objects("Game #1", title_font, title_color)
    TextRect.center = ((background_width / 2), (background_height / 2))
    screen.blit(TextSurf, TextRect)

    # screen.blit(pygame.transform.scale(start_img, (150, 44)), (336, 301))
    # button("Start Game", 370, 285, 150, 43, brighter_red, darker_red, text_font, game_selection)
    pygame.draw.rect(screen, title_color, (370, 285, 165, 43))
    pygame.display.update()

    TextSurf, TextRec = text_objects("START GAME", text_font, start_color)
    TextRect.center = ((background_width * .54), (background_height * .65))
    screen.blit(TextSurf, TextRect)

    #Interactive button needs to be fixed
    mouse = pygame.mouse.get_pos()
    if 370 + 150 > mouse[0] > 150 and 285 + 43 > mouse[1] > 43:
        TextSurf, TextRec = text_objects("Start Game", text_font, black)
        TextRect.center = ((background_width * .65), (background_height * .65))
        screen.blit(TextSurf, TextRect)


    game_intro()
    pygame.quit()
    quit()

run_menu()
pygame.quit()
quit()

