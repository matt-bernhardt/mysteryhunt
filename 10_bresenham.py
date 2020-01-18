# Drawing the beanstalk as a straight line...
def func(x0, y0, x1, y1):
  points = []
  dx = abs(x1 - x0)
  sx = 1 if x0 < x1 else -1
  dy = abs(y1 - y0)
  sy = 1 if y0 < y1 else -1
  x, y = x0, y0
  if dx < dy:
      err = dx / 2.0
      while x != x1:
          points.append((x,y))
          err -= dy
          if err < 0:
              y += sy
              err += dx
          x += sx
  else:
      err = dy / 2.0
      while y != y1:
          points.append((x, y))
          err -= dx
          if err < 0:
              x += sx
              err += dy
          y += sy      
  points.append((x, y))
  return points