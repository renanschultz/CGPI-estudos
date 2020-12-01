import cairo

WIDHT = 4
HEIGHT = 2
PIXEL_SCALE = 80 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDHT*PIXEL_SCALE, HEIGHT*PIXEL_SCALE)


c = cairo.Context(surface)
c.scale(PIXEL_SCALE, PIXEL_SCALE)

c.rectangle(0,0, WIDHT, HEIGHT)
c.set_source_rgb(0.3, 1, 0.5)
c.fill()

c.move_to(1,1)
c.line_to(0.5,0.5)

c.move_to(2,1)
c.line_to(0.5, 0.5)

c.set_source_rgb(1, 0, 0)
c.set_line_width(0.05)
c.stroke()

surface.write_to_png('line.png')