import pygame
import math

def scale_img(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img,size)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image,angle)                 # Obracamy oryginalny obraz
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft= top_left).center)          #Obracamy obraz bez zmiany wpółrzednych X oraz Y obrazu na ekranie, dzieki temu obracamy obraz wzgledem jego srodka a nie leweo gornego rogu
    win.blit(rotated_image,new_rect.topleft)

RED_CAR = scale_img(pygame.image.load("img/red-car.png"), 0.55)
GREEN_CAR = scale_img(pygame.image.load("img/green-car.png"), 0.55)
GREY_CAR = scale_img(pygame.image.load("img/grey-car.png"), 0.55)
PURPLE_CAR = scale_img(pygame.image.load("img/purple-car.png"), 0.55)
WHITE_CAR = scale_img(pygame.image.load("img/white-car.png"), 0.55)



class AbstractCar: #Klasa nadrzędna na klas samochodów użytkowników i samochodu sterowanego przez komputer
    LAPS = 5
    def __init__(self, max_vel, rotation_vel):
        self.max_vel=max_vel
        self.vel = 0                    # początkowa prędkość samochodu jest równa 0
        self.rotation_vel=rotation_vel
        self.angle = 0                   # początkowy kąt skrętu samochodu
        self.x_pos, self.y_pos = self.START_POS
        self.acceleration = 0.01
        self.lap = 1
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x_pos, self.y_pos), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/1.5)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y_pos -= vertical
        self.x_pos -= horizontal


    def brake(self):
        self.vel = self.vel - self.acceleration*4

    def collide(self, mask, x =0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x_pos - x), int(self.y_pos -y))
        poi = mask.overlap(car_mask, offset)                #punkt przecięca obrazów
        return poi

    def reset(self):
        self.x_pos, self.y_pos = self.START_POS
        self.angle = 0
        self.vel = 0

    def next_lap(self):
        self.lap += 1

    def race_finished(self):
        return self.lap > self.LAPS


class PlayerCar(AbstractCar):
    START_POS = (200, 200)
    def __init__(self, max_vel, rotation_vel, img):
        super().__init__(max_vel,rotation_vel)
        self.img = img

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2,0)
        self.move()

    def bounce(self):
        self.vel = -self.vel/2
        self.move()

    def reset_next_lap(self):
        self.x_pos, self.y_pos = self.START_POS
        self.angle = 0
        self.vel = self.max_vel - 2

class ComputerCar(AbstractCar):
    START_POS = (170, 200)

    def __init__(self, max_vel, rotation_vel,img, path=[]):
        super().__init__(max_vel,rotation_vel)                                #z klasy AbstrartCar uzywamy init, żeby zaincjować wszystkie potrzebne wartosci
        self.path = path
        self.current_point = 0
        self.vel = 0
        self.img = img

    def draw_points(self,win):
        for point in self.path:
            pygame.draw.circle(win,(255,0,0),point, 5)                                   #kolor okręgu - czerwony

    def draw(self, win):
        super().draw(win)
        #self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x_pos
        y_diff = target_y - self.y_pos

        if y_diff == 0:
            radian_angle = math.pi/2
        else:
            radian_angle = math.atan(x_diff/y_diff)

        if target_y > self.y_pos:               #kąt skrętu jest większy niż 90 stopni
            radian_angle += math.pi

        angle_diff = self.angle - math.degrees(radian_angle)

        if angle_diff >= 180:                   #Różnica musi być najmnniejsza, żeby zmiast skręcać o 260 stopni w lewo można było skręcić o 100 w prawo
            angle_diff -= 360

        if angle_diff > 0:
            self.angle -= min(self.rotation_vel, abs(angle_diff))           #Upewniamy się, że ustawiamy dobry kąt, żeby nie ominąć punktu, który ma przejechać samochód PC
        else:
            self.angle += min(self.rotation_vel, abs(angle_diff))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x_pos, self.y_pos, self.img.get_width(), self.img.get_height())

        if rect.collidepoint(*target):
            self.current_point += 1
    def move(self):
        if self.current_point >= len(self.path):
            self.angle = 0
            self.current_point = 0
        self.calculate_angle()
        self.update_path_point()
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        super().move()

    def reset_next_lap(self,lap):
        self.x_pos, self.y_pos = self.START_POS
        self.angle = 0
        self.vel = self.max_vel + (lap - 1) * 0.3
