import pygame
import os

BIRD_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird1.png"))), pygame.transform.scale2x(
    pygame.image.load(os.path.join("assets", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird3.png")))]
BG_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("assets", "bg.png")))
BASE_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("assets", "base.png")))

class Bird:
    IMGS = BIRD_IMG
    #Tilt rotation
    MAX_ROTATION = 25
    #Rotation per time frame
    ROT_VEL = 20
    ANIMATION_TIME = 5 

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.heigth = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        #Coordinates are down-right positive based
        self.velocity = -10.5   #pixels per seconds
        self.tick_count = 0
        self.heigth = self.y

    def move(self):
        self.tick_count += 1
        # Acceleration equation (Kinematics) - Y position
        d = (self.velocity*self.tick_count) + (1.5*self.tick_count**2)

        if d >= 16:
            d = 16
        
        if d < 0 :
            d -= 2

        self.y = self.y + d
        if d < 0 or self.y < self.heigth + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
        
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)

        win.blit(rotated_img, new_rect.topleft)

    # For mask and collision
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    
