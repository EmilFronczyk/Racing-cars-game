from car import *
from gameInfo import *

pygame.font.init()
def get_font(size):
    return pygame.font.Font("img/font.ttf",size)



def draw_pc_player(win, images, player_car, computer_car, game_info):
    for img, pos in images:
        win.blit(img, pos)

    pc_lap_text = MAIN_FONT.render(f"PC lap {computer_car.lap}/5", 1 , (255,255,255))
    win.blit(pc_lap_text, (10,HEIGHT-pc_lap_text.get_height() -  100))

    p1_lap_text = MAIN_FONT.render(f"P1 lap {player_car.lap}/5", 1, (255, 255, 255))
    win.blit(p1_lap_text, (10, HEIGHT - p1_lap_text.get_height() - 70))

    time_text = MAIN_FONT.render(f"Time: {game_info.get_level_time()} s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(f"Speed: {round(player_car.vel,1)} px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))


    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()


def draw_player1_v_player2(win, images, player_car_1, player_car_2, game_info):
    for img, pos in images:
        win.blit(img, pos)

    pc_lap_text = MAIN_FONT.render(f"P2 lap {player_car_2.lap}/5", 1 , (255,255,255))
    win.blit(pc_lap_text, (10,HEIGHT-pc_lap_text.get_height() -  100))

    p1_lap_text = MAIN_FONT.render(f"P1 lap {player_car_1.lap}/5", 1, (255, 255, 255))
    win.blit(p1_lap_text, (10, HEIGHT - p1_lap_text.get_height() - 70))

    time_text = MAIN_FONT.render(f"Time: {game_info.get_level_time()} s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(f"Speed: {round(player_car_1.vel,1)} px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))


    player_car_1.draw(win)
    player_car_2.draw(win)
    pygame.display.update()

GRASS = scale_img(pygame.image.load("img/grass.jpg"), 2.5)
TRACK = scale_img(pygame.image.load("img/track.png"), 0.99)
BACKGROUND = pygame.image.load("img/background.png")

WIDTH, HEIGHT = BACKGROUND.get_width(), BACKGROUND.get_height()

TRACK_BORDER = scale_img(pygame.image.load("img/track-border.png"), 0.99)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
FINISH_LINE = pygame.image.load("img/finish (1).png")
FINISH_LINE_MASK = pygame.mask.from_surface(FINISH_LINE)
FINISH_LINE_POSITION = (146,250)

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

FPS = 60 # liczba klatek
GAME_CLOCK = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0)), (FINISH_LINE, FINISH_LINE_POSITION), (TRACK_BORDER,(0,0))]
PATH = [(199, 84), (42, 115), (75, 515), (195, 701), (339, 813), (417, 688), (510, 524), (668, 649), (702, 824), (840, 607), (797, 401), (580, 407), (437, 341), (544, 262), (772, 295), (791, 139), (630, 82), (329, 85), (327, 260), (286, 434), (170, 352), (185, 254), (170, 200)]

MAIN_FONT = pygame.font.SysFont("comicsans", 35)

def blit_text_center(win, font, text):
    render = font.render(text, 1, (200,200,200))
    win.blit(render, (win.get_width()/2 - render.get_width()/2, win.get_height()/2 - render.get_height()/2))                        #renderujemy tekst tak aby był idelanie po środku

def move_player1(player_car):
    keys = pygame.key.get_pressed()

    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_r]:
        moved = True
        player_car.move_backward()
    if keys[pygame.K_s]:
        player_car.brake()
    if not moved:
        player_car.reduce_speed()

def move_player2(player_car):
    keys = pygame.key.get_pressed()

    moved = False

    if keys[pygame.K_LEFT]:
        player_car.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        player_car.rotate(right=True)
    if keys[pygame.K_UP]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_KP0]:
        moved = True
        player_car.move_backward()
    if keys[pygame.K_DOWN]:
        player_car.brake()
    if not moved:
        player_car.reduce_speed()

def handle_collision_pc_v_player(player_car, computer_car, game_info):
    keys = pygame.key.get_pressed()
    if player_car.collide(TRACK_BORDER_MASK) is not None:
        player_car.bounce()


    computer_finish_poi_collide = computer_car.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)
    if computer_finish_poi_collide is not None:
        computer_car.reset_next_lap(computer_car.lap)
        computer_car.next_lap()
        print(f"{computer_finish_poi_collide}")
        print(f"{game_info.lap}")
    if computer_car.race_finished():
        WINNER_TEXT = get_font(70).render("COMPUTER WON!", True, "#FF7F50")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(450, 100))
        WINDOW.blit(WINNER_TEXT, WINNER_RECT)
        print("computer wins")
        return True


    player_finish_poi_collide = player_car.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)

    if player_finish_poi_collide is not None:
        print(f"{player_finish_poi_collide}")
        print(f"{player_car.lap}")
        if player_finish_poi_collide[1] == 0 and keys[pygame.K_r]:
            player_car.bounce()
        else:
            player_car.reset_next_lap()
            player_car.next_lap()
            print(f"{player_finish_poi_collide}")
            print(f"{player_car.lap}")
    if player_car.race_finished():
        WINNER_TEXT = get_font(70).render("YOU WON!", True, "#FF7F50")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(450, 100))
        WINDOW.blit(WINNER_TEXT, WINNER_RECT)
        print("you wins")
        return True

def handle_collision_player1_v_player2(player_car_1, player_car_2):
    keys = pygame.key.get_pressed()
    if player_car_1.collide(TRACK_BORDER_MASK) is not None:
        player_car_1.bounce()
    if player_car_2.collide(TRACK_BORDER_MASK) is not None:
        player_car_2.bounce()

    player_1_finish_poi_collide = player_car_1.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)

    if player_1_finish_poi_collide is not None:
        if player_1_finish_poi_collide[1] == 0 and keys[pygame.K_r]:
            player_car_1.bounce()
        else:
            player_car_1.reset_next_lap()
            player_car_1.next_lap()
    if player_car_1.race_finished():
        WINNER_TEXT = get_font(70).render("Player 1 won!", True, "#FF7F50")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(450, 100))
        WINDOW.blit(WINNER_TEXT, WINNER_RECT)
        return True


    player_2_finish_poi_collide = player_car_2.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)

    if player_2_finish_poi_collide is not None:
        if player_2_finish_poi_collide[1] == 0 and keys[pygame.K_r]:
            player_car_2.bounce()
        else:
            player_car_2.reset_next_lap()
            player_car_2.next_lap()
    if player_car_2.race_finished():
        WINNER_TEXT = get_font(70).render("Player 2 won!", True, "#FF7F50")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(450, 100))
        WINDOW.blit(WINNER_TEXT, WINNER_RECT)
        return True

player_car_1 = PlayerCar(4, 4,RED_CAR)
player_car_2 = PlayerCar(4, 4, WHITE_CAR)
computer_car = ComputerCar(2.5,4,GREY_CAR,PATH)
game_info = GameInfo()