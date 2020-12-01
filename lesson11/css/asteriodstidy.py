
"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
"""slowed this so the game was more playable"""
BIG_ROCK_SPEED = 1
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
MEDIUM_ROCK_SPEED = 2

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2
SMALL_ROCK_SPEED = 1.5

class Point():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        
class Velocity():
    def __init__(self):
        self.dx = 1.0
        self.dy = 1.0
        
class Flying():
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True
        self.rotate = 0.0
        self.angle = 0.0
        self.points = 0.0
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.angle += self.rotate
        
    def is_off_screen(self, screen_width, screen_height):
        if self.center.x > screen_width:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = screen_width
        if self.center.y > screen_height: 
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = screen_height
            
    def hit(self):
        self.alive = False
        return self.points
        
    
class Rock(Flying):
    def __init__(self):
        super().__init__()
        self.center.x = float(random.uniform(0, SCREEN_WIDTH))
        self.center.y = float(random.uniform(0, SCREEN_HEIGHT))
        self.velocity.dx = float(random.uniform(-2, 5))
        self.velocity.dy = float(random.uniform(-2, 5))
        self.points = 1.0
        self.radius = 40
        self.angle = float(random.uniform(0, 360))
    
    def draw(self):
        med = ":resources:images/space_shooter/meteorGrey_med1.png"
        texture = arcade.load_texture(med)

        width = texture.width
        height = texture.height

        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, 255)
    
    def crack(self):
        rock_list = []
        return rock_list
        

class Large(Rock):
    def __init__(self):
        super().__init__()
        self.velocity.dy = 1.5
        self.velocity.dx = 1.5
        self.rotate = BIG_ROCK_SPIN
        
        
    def draw(self):
        large = ":resources:images/space_shooter/meteorGrey_big1.png"
        texture = arcade.load_texture(large)

        width = texture.width
        height = texture.height

        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, 255)
        
    def crack(self):
        rock_list = []
        med_one = Med()
        med_one.center.x = self.center.x
        med_one.center.y = self.center.y
        med_one.velocity.dx = self.velocity.dx 
        med_one.velocity.dy = self.velocity.dy + MEDIUM_ROCK_SPEED
        med_two = Med()
        med_two.center.x = self.center.x
        med_two.center.y = self.center.y
        med_two.velocity.dx = self.velocity.dx 
        med_two.velocity.dy = self.velocity.dy - MEDIUM_ROCK_SPEED
        smallrock = Small()
        smallrock.center.x = self.center.x
        smallrock.center.y = self.center.y
        smallrock.velocity.dx = self.velocity.dx + 5
        smallrock.velocity.dy = self.velocity.dy 
    
        rock_list.append(med_one)
        rock_list.append(med_two)
        rock_list.append(smallrock)
        return rock_list
    
        
class Med(Rock):
    def __init__(self):
        super().__init__()
        self.rotate = MEDIUM_ROCK_SPIN
        self.points = 2
        
    def draw(self):
        med = ":resources:images/space_shooter/meteorGrey_med1.png"
        texture = arcade.load_texture(med)

        width = texture.width
        height = texture.height

        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, 255)
        
    def crack(self):
        rock_list = []
        smallrock = Small()
        smallrock.center.x = self.center.x
        smallrock.center.y = self.center.y
        smallrock.velocity.dx = self.velocity.dx + SMALL_ROCK_SPEED
        smallrock.velocity.dy = self.velocity.dy + SMALL_ROCK_SPEED
        smallrockt = Small()
        smallrockt.center.x = self.center.x
        smallrockt.center.y = self.center.y
        smallrockt.velocity.dx = self.velocity.dx - SMALL_ROCK_SPEED
        smallrockt.velocity.dy = self.velocity.dy - SMALL_ROCK_SPEED
    
        rock_list.append(smallrock)
        rock_list.append(smallrockt)
        return rock_list
        
class Small(Rock):
    def __init__(self):
        super().__init__()
        self.rotate = SMALL_ROCK_SPIN
        self.points = 5

    def draw(self):
        small = ":resources:images/space_shooter/meteorGrey_small1.png"
        texture = arcade.load_texture(small)

        width = texture.width
        height = texture.height

        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, 255)
        
class Bullet(Flying):
    def __init__(self):
        super().__init__()
        self.radius = 1
        self.velocity.dx= BULLET_SPEED
        self.angle = 0
        self.life = BULLET_LIFE
        
    def draw(self):
        med = ":resources:images/space_shooter/laserBlue01.png"
        texture = arcade.load_texture(med)
        
        width = texture.width
        height = texture.height

        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, (angle ) , 255)

    def fire(self, shipvelocity, shipcenter, shipangle):
        self.angle = shipangle
        self.center.x = shipcenter.x
        self.center.y = shipcenter.y
        self.velocity.dy = shipvelocity.dy
        self.velocity.dx = shipvelocity.dx
        self.velocity.dx += math.cos(math.radians(shipangle)) * BULLET_SPEED
        self.velocity.dy += math.sin(math.radians(shipangle)) * BULLET_SPEED
        
    def advance(self):
        super().advance()
        self.life-=1
        if self.life == 0:
            self.alive = False
        
class Ship(Flying):
    def __init__(self):
        super().__init__()
        self.radius = SHIP_RADIUS
        self.velocity.dx = 0.0
        self.velocity.dy = 0.0
        self.angle = 0
        self.center.x = SCREEN_WIDTH// 2
        self.center.y = SCREEN_HEIGHT// 2
        
        
    def draw(self):
        med = ":resources:images/space_shooter/playerShip1_orange.png"
        texture = arcade.load_texture(med)
        width = texture.width
        height = texture.height
        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, (angle - 90), 255)
    

class Game(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.held_keys = set()
        self.asteriods = []
        self.bullets = []
        self.score = 0
        self.ship = Ship()
        self.restart()
        
    def restart(self):
        self.asteriods.clear()
        self.bullets.clear()
        self.score = 0
        self.ship = Ship()
        """Creating inital asteriods"""
        l1 = Large()
        l2 = Large()
        l3 = Large()
        l4 = Large()
        l5 = Large()
        """Placing inital asteriods"""
        l1.center.x = 100
        l2.center.x = 300
        l3.center.x = 500
        l4.center.x = 400
        l5.center.x = 100
        l1.center.y = 50
        l2.center.y = 500
        l3.center.y = 100
        l4.center.y = 80
        l5.center.y = 400
        """Adding inital asteriods"""
        self.asteriods.append(l1)
        self.asteriods.append(l2)
        self.asteriods.append(l3)
        self.asteriods.append(l4)
        self.asteriods.append(l5)

    def on_draw(self):
        arcade.start_render()
        
        self.draw_score()
        
        for bullet in self.bullets:
            bullet.draw()
            
        self.ship.draw()
        
        for asteriod in self.asteriods:
            asteriod.draw()
               
        if self.ship.alive == False:
            self.draw_game_over()
            
   
    def update(self, delta_time):
        self.check_keys()
    
        if random.randint(1, 500) == 1:
            self.create_rocks()
            
        for asteriod in self.asteriods:
            asteriod.advance()
            asteriod.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)
            
        for bullet in self.bullets:
            bullet.advance()
            bullet.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)

        self.ship.advance()
        self.ship.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)
        
        self.check_collisions()
        
    def draw_game_over(self):
        msg_text = "GAME OVER" 
        start_x = SCREEN_WIDTH//2 - 155
        start_y = SCREEN_HEIGHT//2 
        arcade.draw_text(msg_text, start_x=start_x, start_y=start_y, font_size=40, color=arcade.color.RED)
        msg_text = "Press Enter To Try Again" 
        start_x = SCREEN_WIDTH//2 - 195
        start_y = SCREEN_HEIGHT//2 -100
        arcade.draw_text(msg_text, start_x=start_x, start_y=start_y, font_size=30, color=arcade.color.RED)
        
        
    def draw_score(self):
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.GREEN)
        
    def check_keys(self):
    
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle -= SHIP_TURN_AMOUNT

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle += SHIP_TURN_AMOUNT

        if arcade.key.UP in self.held_keys:
            self.ship.velocity.dy += SHIP_THRUST_AMOUNT * math.sin(math.radians(self.ship.angle))
            self.ship.velocity.dx += SHIP_THRUST_AMOUNT * math.cos(math.radians(self.ship.angle))
            if self.ship.velocity.dy > 7: 
                self.ship.velocity.dy = 7
            if self.ship.velocity.dy <-7:
                self.ship.velocity.dy = -7
            if self.ship.velocity.dx > 7: 
                self.ship.velocity.dx = 7
            if self.ship.velocity.dx <-7:
                self.ship.velocity.dx = -7

        if arcade.key.DOWN in self.held_keys:
            self.ship.velocity.dy -= SHIP_THRUST_AMOUNT * math.sin(math.radians(self.ship.angle))
            self.ship.velocity.dx -= SHIP_THRUST_AMOUNT * math.cos(math.radians(self.ship.angle))
            if self.ship.velocity.dy > 7: 
                self.ship.velocity.dy = 7
            if self.ship.velocity.dy <-7:
                self.ship.velocity.dy = -7
            if self.ship.velocity.dx > 7: 
                self.ship.velocity.dx = 7
            if self.ship.velocity.dx <-7:
                self.ship.velocity.dx = -7
   
    def on_key_press(self, key: int, modifiers: int):
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullet()
                bullet.fire(self.ship.velocity, self.ship.center, self.ship.angle)

                self.bullets.append(bullet)
        else:
            if key == arcade.key.ENTER:
                self.restart()
              
    def on_key_release(self, key: int, modifiers: int):
        if key in self.held_keys:
            self.held_keys.remove(key)
            
    def check_collisions(self):
        for asteriod in self.asteriods:
            for bullet in self.bullets:

                if bullet.alive and asteriod.alive:
                    too_close = bullet.radius + asteriod.radius

                    if (abs(bullet.center.x - asteriod.center.x) < too_close and
                                abs(bullet.center.y - asteriod.center.y) < too_close):
                        bullet.alive = False
                        self.score += asteriod.hit()
                        
            if asteriod.alive and self.ship.alive:
                too_close = self.ship.radius + asteriod.radius

                if (abs(self.ship.center.x - asteriod.center.x) < too_close and
                        abs(self.ship.center.y - asteriod.center.y) < too_close):
                    self.score += self.ship.hit()

        self.cleanup()

    def cleanup(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteriod in self.asteriods:
            if not asteriod.alive:
                rock_list = asteriod.crack()
                self.asteriods.extend(rock_list)
                self.asteriods.remove(asteriod)
                
    def create_rocks(self):
        if random.randint(1, 3) == 1:
            newrock = Small()
            self.asteriods.append(newrock)
        elif random.randint(1, 3) == 2:
            newrocktwo = Med()
            self.asteriods.append(newrocktwo)
        else:
            newrockthree = Large()
            self.asteriods.append(newrockthree)

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()


