import pygame as py

py.init()


class space:

     def __init__(self, l, h, cap):

          self.winscr = [l, h]

          self.window = py.display.set_mode(self.winscr)

          py.display.set_caption(cap)

     def update(self):
          
          matter1.update(self.window)
          matter2.update(self.window)

          for event in py.event.get():
               if event.type == py.QUIT:
                    py.quit()
                    quit()


class matter:

     def __init__(self, x, y, w, l, m):

          self.x = x
          self.y = y

          self.w = w
          self.l = l
          self.m = m

          self.volume = self.w * self.l
          self.density = self.m / self.volume if self.volume != 0 else 0
          
          self.velocity = py.Vector2(0, 0)
          self.acceleration = py.Vector2(0, 0)

          self.rect = py.FRect(
               self.x,
               self.y,
               self.w,
               self.l
          )
     
     def apply_force(self, force):

          self.acceleration += force / self.m

     def update(self, surface):

          py.draw.rect(
               surface,
               "#FF0000",
               self.rect
          )

          self.velocity += self.acceleration

          self.rect.x = self.x
          self.rect.y = self.y

          self.x += self.velocity.x
          self.y += self.velocity.y

          self.acceleration *= 0   

static_univrs = space(
     500,
     500,
     "Force and Mass"
)

matter1 = matter(
     100,
     100,
     50,
     50,
     100
)

matter2 = matter(
     200,
     200,
     50,
     50,
     200
)

while True:

     static_univrs.update()

     py.display.update()