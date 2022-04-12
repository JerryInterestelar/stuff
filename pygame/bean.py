import math, numpy, pygame

class Bean:
    def __init__(self,x, y, s, color):
        self.pos_x = x
        self.pos_y = y
        self.vel_x = 1
        self.vel_y = 1
        self.acc_x = 0
        self.acc_y = 0
        # self.r = 6
        self.max_s = 15
        self.max_a = .3

        self.angle = 0
        self.an_vel = 0
        self.size_x = 5*s
        self.size_y = s
        self.draw(color)


    def update(self, width, height):

        vx = self.vel_x + self.acc_x
        vy = self.vel_y + self.acc_y

        self.vel_x, self.vel_y = self.clamp_norm(vx, vy, self.max_s)

        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        self.angle += self.an_vel

        self.acc_x *= 0
        self.acc_y *= 0

    def apply_force(self, force_x, force_y):
        self.acc_x += force_x
        self.acc_y += force_y

    def seek(self, target_x, target_y):
        #set mag 
        d_x = target_x - self.pos_x
        d_y = target_y - self.pos_y

        desired_x, desired_y = self.set_mag(d_x, d_y, self.max_s)

        ax = desired_x - self.vel_x
        ay = desired_y - self.vel_y
        
        steer_x, steer_y = self.clamp_norm(ax, ay, self.max_a)
        self.apply_force(steer_x, steer_y)

    def eat(self, list):
        record = numpy.inf
        closest = -1
        for i in range(len(list)):

            d = math.dist((self.pos_x, self.pos_y), (list[i].pos_x, list[i].pos_y))
            if d < record:
                record = d
                closest = i

        if record < 8:
            list.pop(closest)
        
        self.seek(list[closest].pos_x, list[closest].pos_y)

    def clamp_norm(self, v_x, v_y, a_max):
        a_mag = self.get_mag(v_x, v_y)
        a_min = min(a_mag, a_max)

        if a_mag != 0:
            return v_x * (a_min/a_mag), v_y * (a_min/a_mag)
        return v_x, v_y 

    def set_mag(self, x, y, n_mag):
        norm_c = n_mag/self.get_mag(x, y)       
        return x * norm_c, y * norm_c

    def get_mag(self, a, b):
        return math.sqrt(a**2 +b**2)

    def get_angle(self):
        return math.degrees(math.atan2(self.vel_x, self.vel_y)) - 90

    def draw(self, color):
        self.surface = pygame.Surface((self.size_x, self.size_y))
        points = [
            (0, 0),
            (self.size_x, int(self.size_y/2)),
                (0, self.size_y)
        ]
        self.shape = pygame.draw.polygon(self.surface, color, points)
        # self.shape = pygame.draw.rect(self.surface, color, self.surface.get_rect())
        self.surface.set_colorkey((0,0,0))

