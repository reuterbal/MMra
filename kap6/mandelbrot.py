#!/usr/bin/env python3

from tkinter import Tk, Canvas, PhotoImage, mainloop

# Dimensionen des Fensters
width, height = 1024, 768

# Abbruchkriterium fuer Divergenz (Fluchtradius)
eps = 1000

# Farbschema von https://stackoverflow.com/a/16505538
default_color = '#000000'
colors = 16 * ['#661E0F',  # ( 66, 30, 15)=(brown 3)
               '#19071A',  # ( 25,  7, 26)=(dark violett)
               '#09012F',  # (  9,  1, 47)=(darkest blue)
               '#040449',  # (  4,  4, 73)=(blue 5)
               '#000764',  # (  0,  7,100)=(blue 4)
               '#122C8A',  # ( 12, 44,138)=(blue 3)
               '#1852B1',  # ( 24, 82,177)=(blue 2)
               '#397DD1',  # ( 57,125,209)=(blue 1)
               '#86B5E5',  # (134,181,229)=(blue 0)
               '#D3ECF8',  # (211,236,248)=(lightest blue)
               '#F1E9BF',  # (241,233,191)=(lightest yellow)
               '#F8C95F',  # (248,201, 95)=(light yellow)
               '#FFAA00',  # (255,170,  0)=(dirty yellow)
               '#CC8000',  # (204,128,  0)=(brown 0)
               '#995700',  # (153, 87,  0)=(brown 1)
               '#6A3403']  # (106, 52,  3)=(brown 2)

# Mittelpunkt und Skalierung des Bildausschnitts
scale, center = 0.005, (0, 0)


def eval_point(x, y):
    """Zuweisung der Farbe im Bildpunkt (x, y)."""
    c = complex(center[0] + x * scale, center[1] + y * scale)
    z = c
    for px in colors:
        z = z * z + c
        if abs(z) > eps:
            return px
    else:
        return default_color


def eval_all_points():
    """Bestimmt Farbe aller Bildpunkte."""
    rangex, rangey = width // 2, height // 2
    b = [' '.join([eval_point(x, y)
                   for x in range(-rangex, rangex)])
         for y in range(-rangey, rangey)]
    return '{' + '} {'.join(b) + '}'


def draw():
    """Aktualisiert die Ausgabe im Fenster."""
    global img, canvas
    canvas.config(cursor='watch')
    canvas.update()
    img.put(eval_all_points())
    canvas.config(cursor='crosshair')
    canvas.update()


def zoom_in(event):
    """Vergroessert Ausgabe mit neuem Mittelpunkt."""
    global center, scale
    center = (center[0] + scale * (event.x - width // 2),
              center[1] + scale * (event.y - height // 2))
    scale /= 4
    draw()


def zoom_out(event):
    """Verkleinert Ausgabe auf vorherige Darstellung."""
    global center, scale
    scale *= 4
    if scale >= 0.005:  # Minimales Zoomlevel
        scale, center = 0.005, (0, 0)
    draw()


def mandelbrot():
    """Hauptprogramm."""
    # Lege Fenster fuer graphische Ausgabe an
    window = Tk()
    window.title('Mandelbrot')

    # Erzeuge Flaeche fuer graphische Ausgabe im Fenster
    global canvas, img
    canvas = Canvas(window, width=width, height=height, bg=default_color)
    canvas.pack()
    img = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=img, state='normal')

    # Verknuepfe Handlungsroutinen mit Maustasten
    canvas.bind('<Button-1>', zoom_in)
    canvas.bind('<Button-3>', zoom_out)

    # Zeichne initiale Mandelbrotmenge und betrete Hauptschleife
    draw()
    mainloop()


# Startet das Hauptprogramm, falls Skript direkt aufgerufen wurde.
if __name__ == '__main__':
    mandelbrot()
