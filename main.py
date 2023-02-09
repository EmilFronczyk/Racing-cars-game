import sys
from button import Button
from funtions_and_utilities import *


pygame.init()

def player_v_player(FPS,GAME_CLOCK):
    GAME_CLOCK.tick(FPS)
    WINDOW.fill("black")
    draw_player1_v_player2(WINDOW, images, player_car_1, player_car_2, game_info)

    while not game_info.started:
        start = MAIN_FONT.render("Press W/UP to start the race!", 1, (55, 55, 215))
        WINDOW.blit(start, (WIDTH / 2 - start.get_width() / 2, HEIGHT / 2 - start.get_height() / 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_info.start_level()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     computer_car.path.append(pos)

    move_player1(player_car_1)
    move_player2(player_car_2)
    if handle_collision_player1_v_player2(player_car_1, player_car_2):
        return True

def player_v_pc(FPS,GAME_CLOCK):
    GAME_CLOCK.tick(FPS)
    WINDOW.fill("black")
    draw_pc_player(WINDOW, images, player_car_1, computer_car, game_info)

    while not game_info.started:
        start = MAIN_FONT.render("Press W to start the race!", 1 , (55,55,215))
        WINDOW.blit(start, (WIDTH / 2 - start.get_width()/2, HEIGHT / 2 - start.get_height()/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_info.start_level()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     computer_car.path.append(pos)

    move_player1(player_car_1)
    computer_car.move()
    if handle_collision_pc_v_player(player_car_1, computer_car, game_info):
        return True
def play(FPS,GAME_CLOCK):

    pygame.display.set_caption("Oldschool web racing game - Menu")
    WINDOW.blit(BACKGROUND, (0, 0))
    new_button = False

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAYER_V_PLAYER_BUTTON = Button(image=pygame.image.load("img/pvp.png"), pos=(215, HEIGHT/2),
                         text_input="P1VP2", font=get_font(73), base_color="#d7fcd4", hovering_color="White")
        PLAYER_V_PC_BUTTON = Button(image=pygame.image.load("img/pvpc.png"), pos=(WIDTH-215, HEIGHT/2),
                                        text_input="PvPC", font=get_font(75), base_color="#d7fcd4",
                                        hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("img/pvp.png"), pos=(WIDTH / 2, HEIGHT / 2),
                             text_input="Menu", font=get_font(73), base_color="#d7fcd4",
                             hovering_color="White")

        if new_button is not True:
            for button in [PLAYER_V_PLAYER_BUTTON,PLAYER_V_PC_BUTTON ]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(WINDOW)

        if new_button:
            for button in [QUIT_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(WINDOW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if QUIT_BUTTON.checkForUserInput(PLAY_MOUSE_POS):
                        menu()
                pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_V_PLAYER_BUTTON.checkForUserInput(PLAY_MOUSE_POS):
                    while True:
                        if player_v_player(FPS,GAME_CLOCK):
                            new_button = True
                            break

                if PLAYER_V_PC_BUTTON.checkForUserInput(PLAY_MOUSE_POS):
                    while True:
                        if player_v_pc(FPS, GAME_CLOCK):
                            new_button = True
                            break

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
        QUIT_BUTTON = Button(image=pygame.image.load("img/quit_rect.png"), pos=(450, 450),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        WINDOW.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForUserInput(MENU_MOUSE_POS):
                    play(FPS,GAME_CLOCK)
                if QUIT_BUTTON.checkForUserInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



menu()