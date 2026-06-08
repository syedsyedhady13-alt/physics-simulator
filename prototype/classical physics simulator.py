import pygame as py
# import tkinter as tk

py.init()

class space:

     def __init__(self, l, h, cap):

          self.winscr = [l, h]

          self.window = py.display.set_mode(
               self.winscr,
               py.RESIZABLE,
               py.SCALED,
               vsync=1,
               display=0
          )

          py.display.set_caption(cap)

          self.clock = py.time.Clock()
          """
          self.pane = panel(400, 300, "Control Panel")
          """
          self.all_matter = []


     def update(self):

          self.dt = self.clock.tick(60) / 1000.0

          for event in py.event.get():
               if event.type == py.QUIT:
                    py.quit()
                    quit()
          """
          self.pane.update()
          """
          self.physics_step()
          self.render()


     def add_matter(self, mattter):
          self.all_matter.append(mattter)


     def render(self):

          self.window.fill((0, 0, 0))

          for obj in self.all_matter:
               obj.render(self.window)

          py.display.update()


     def physics_step(self):
          
          # collision
          for i in range(len(self.all_matter)):
               for j in range(i + 1, len(self.all_matter)):

                    a = self.all_matter[i]
                    b = self.all_matter[j]

                                   
                    # collision
                    if a.rect.colliderect(b.rect):

                         m1 = a.m
                         m2 = b.m

                         v1 = a.velocity.x
                         v2 = b.velocity.x

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

                         a.velocity.x = new_v1
                         b.velocity.x = new_v2
                         # separate bodies
                         overlap = a.rect.right - b.rect.left

                         v1 = a.velocity.y
                         v2 = b.velocity.y

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

                         a.velocity.y = new_v1
                         b.velocity.y = new_v2

                         overlap_x= min(a.rect.right, b.rect.right) - max(a.rect.left, b.rect.left)
                         overlap_y = min(a.rect.bottom, b.rect.bottom) - max(a.rect.top, b.rect.top)
          """
          # gravity
          G = 425

          # pairwise gravity
          for i in range(len(self.all_matter)):
               for j in range(i + 1, len(self.all_matter)):

                    a = self.all_matter[i]
                    b = self.all_matter[j]

                    direction = py.Vector2(b.x - a.x, b.y - a.y)
                    distance = direction.length()

                    if distance == 0:
                         continue

                    # softening to avoid explosion
                    distance = max(distance, 20)

                    force_magnitude = (a.m * b.m) / (distance * distance)
                    force_magnitude *= G

                    direction = direction.normalize()
                    force = direction * force_magnitude

                    a.apply_force(force)
                    b.apply_force(-force)
"""
          # integrate motion
          for obj in self.all_matter:

               obj.velocity += obj.acceleration * self.dt
               obj.x += obj.velocity.x * self.dt
               obj.y += obj.velocity.y * self.dt

               obj.rect.topleft = (obj.x, obj.y)

               obj.acceleration = py.Vector2(0, 0)

"""
class panel:

     def __init__(self, l, h, cap):

          self.winscr = [l, h]

          self.window = tk.Tk()
          self.window.geometry(f"{l}x{h}")
          self.window.title(cap)

     def update(self):
          self.window.update()
"""

class matter:

     def __init__(self, x, y, w, l, m):

          self.id = id(self)

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

          if self.m != 0:
               self.acceleration += force / self.m

     def render(self, surface):

          py.draw.rect(
               surface,
               "#FF0000",
               self.rect
          )


universe = space(1200, 700, "Classical Physics Simulator")
m1 = matter(150, 150, 10, 10, 1)
m2 = matter(550, 550, 10, 10, 1)

universe.add_matter(m1)
universe.add_matter(m2)

m1.velocity = py.Vector2(100, 0)
m2.velocity = py.Vector2(-50, -150)

while True:
     universe.update()