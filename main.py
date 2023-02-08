import sys
from button import Button
from funtions_and_utilities import *


pygame.init()

def player_v_player(FPS,GAME_CLOCK):
    pass

def player_v_pc(FPS,GAME_CLOCK,MENU_TEXT, MENU_RECT):
    GAME_CLOCK.tick(FPS)
    WINDOW.fill("black")
    draw(WINDOW, images, player_car, computer_car, game_info)

    while not game_info.started:
        blit_text_center(WINDOW, MAIN_FONT, f"Press any to start level {game_info.level}!")
        pygame.display.update()
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event1.type == pygame.KEYDOWN:
                game_info.start_level()
    for event2 in pygame.event.get():
        if event2.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     computer_car.path.append(pos)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     #if PLAY_BACK.checkForUserInput(PLAY_MOUSE_POS):
        #         menu()

    move_player1(player_car)
    computer_car.move()
    if handle_collision(player_car, computer_car, game_info, MENU_TEXT, MENU_RECT):
        return True
def play(FPS,GAME_CLOCK,MENU_TEXT, MENU_RECT):
    # while True:
    #     GAME_CLOCK.tick(FPS) # upewniamy sie, ze nasza petla (gra) nie bedzie dzialac szybciej niz 60 FPS, dzieki temu gra bedzie dzialac tak samo niezaleznie od procesora
    #
    #     PLAY_MOUSE_POS = pygame.mouse.get_pos()
    #
    #     WINDOW.fill("black")
    #
    #     PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
    #     PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
    #     WINDOW.blit(PLAY_TEXT, PLAY_RECT)
    #
    #     PLAY_BACK = Button(image=None, pos=(640, 460),
    #                        text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
    #
    #     PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    #     PLAY_BACK.update(WINDOW)
    #
    #     WINDOW.fill("black")
    #     draw(WINDOW,images, player_car, computer_car, game_info)
    #
    #     while not game_info.started:
    #         blit_text_center(WINDOW, MAIN_FONT, f"Press any to start level {game_info.level}!")
    #         pygame.display.update()
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #
    #             if event.type == pygame.KEYDOWN:
    #                 game_info.start_level()
    #
    #     pygame.display.update()
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             pos = pygame.mouse.get_pos()
    #             computer_car.path.append(pos)
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if PLAY_BACK.checkForUserInput(PLAY_MOUSE_POS):
    #                 menu()
    #
    #     move_player1(player_car)
    #     computer_car.move()
    #     handle_collision(player_car,computer_car,game_info,lap_number)
    #
    #     print(computer_car.path)
    #     pygame.display.update()
        pygame.display.set_caption("Oldschool web racing game - Menu")
        WINDOW.blit(BACKGROUND, (0, 0))
        pvp_text = "P1vP2"

        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            PLAYER_V_PLAYER_BUTTON = Button(image=pygame.image.load("img/pvp.png"), pos=(215, HEIGHT/2),
                             text_input=pvp_text, font=get_font(73), base_color="#d7fcd4", hovering_color="White")
            PLAYER_V_PC_BUTTON = Button(image=pygame.image.load("img/pvpc.png"), pos=(WIDTH-215, HEIGHT/2),
                                            text_input="PvPC", font=get_font(75), base_color="#d7fcd4",
                                            hovering_color="White")
            for button in [PLAYER_V_PLAYER_BUTTON,PLAYER_V_PC_BUTTON ]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(WINDOW)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAYER_V_PLAYER_BUTTON.checkForUserInput(PLAY_MOUSE_POS):
                        while True:
                            pass

                    if PLAYER_V_PC_BUTTON.checkForUserInput(PLAY_MOUSE_POS):
                        while True:
                            if player_v_pc(FPS, GAME_CLOCK,MENU_TEXT, MENU_RECT):
                                break
            pygame.display.update()



def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WINDOW.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(450, 260))
        WINDOW.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(450, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForUserInput(OPTIONS_MOUSE_POS):
                    menu()

        pygame.display.update()
def menu(): #Ekran z menu
    pygame.display.set_caption("Oldschool web racing game - Menu")
    WINDOW.blit(BACKGROUND, (0,0))

    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(80).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(450,100))

        PLAY_BUTTON = Button(image=pygame.image.load("img/play_rect.png"), pos=(450, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("img/options_rect.png"), pos=(450, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("img/quit_rect.png"), pos=(450, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        WINDOW.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForUserInput(MENU_MOUSE_POS):
                    play(FPS,GAME_CLOCK,MENU_TEXT, MENU_RECT)
                if OPTIONS_BUTTON.checkForUserInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForUserInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



menu()