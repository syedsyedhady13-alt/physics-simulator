import pygame as py

py.init()

WIDTH = 1000
HEIGHT = 300

window = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()


class Body:

     def __init__(self, x, mass, velocity, color):

          self.mass = mass
          self.velocity = velocity

          self.rect = py.Rect(
               x,
               HEIGHT // 2 - 25,
               50,
               50
          )

          self.color = color

     def update(self, dt):

          self.rect.x += self.velocity * dt

     def draw(self, surface):

          py.draw.rect(
               surface,
               self.color,
               self.rect
          )


body1 = Body(
     x=200,
     mass=10000000,
     velocity=150,
     color="red"
)

body2 = Body(
     x=700,
     mass=10,
     velocity=-100,
     color="green"
)

running = True

while running:

     dt = clock.tick(60) / 1000.0

     for event in py.event.get():

          if event.type == py.QUIT:
               running = False

     # movement
     body1.update(dt)
     body2.update(dt)

     # collision
     if body1.rect.colliderect(body2.rect):

          m1 = body1.mass
          m2 = body2.mass

          v1 = body1.velocity
          v2 = body2.velocity

          # elastic collision formulas
          new_v1 = (
               ((m1 - m2) / (m1 + m2)) * v1
               +
               ((2 * m2) / (m1 + m2)) * v2
          )

          new_v2 = (
               ((2 * m1) / (m1 + m2)) * v1
               +
               ((m2 - m1) / (m1 + m2)) * v2
          )

          body1.velocity = new_v1
          body2.velocity = new_v2

          # separate bodies
          overlap = body1.rect.right - body2.rect.left

          body1.rect.x -= overlap // 2
          body2.rect.x += overlap // 2

     window.fill("black")

     body1.draw(window)
     body2.draw(window)

     py.display.flip()

py.quit()