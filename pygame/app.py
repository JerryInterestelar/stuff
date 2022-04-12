import pygame as pg
import bean
import point, random

def main():
    pg.init()
    clock = pg.time.Clock()
    pg.display.set_caption("Almost a bean")
    
    width = 900
    height = 450
    screen = pg.display.set_mode((width, height))
    GREEN = pg.Color(0,255,0)
    BLACK = pg.Color(0,0,0)
    WHITE = pg.Color(255,255,255)
    
    bg = pg.Surface((width, height))
    pg.draw.rect(bg, BLACK, bg.get_rect())

    #bean
    beans = []
    for i in range(1):
        x = random.randrange(width)
        y = random.randrange(height)
        bn = bean.Bean(x, y, 10, GREEN)
        beans.append(bn)

    #point
    points = []
    for i in range(15):
        x = random.randrange(width)
        y = random.randrange(height)
        points.append(point.Point(x, y, 10, WHITE))

    running = True
    while running:
        screen.fill((0,0,0))

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                

        for b in beans:
            # b.seek(points[0].pos_x, points[0].pos_y)
            b.eat(points)
            b.update(width, height)
        

        #rotate bean
        for b in beans:
            b_cp = pg.transform.rotate(b.surface, b.get_angle())
            offx = int(b_cp.get_width() / 2)
            offy = int(b_cp.get_height() / 2)

            screen.blit(b_cp, (b.pos_x - offx, b.pos_y - offy))

        for p in points:
            screen.blit(p.surface, (p.pos_x, p.pos_y))

        pg.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    main()
