# lecture 7
# fractal_rectangle

import graphics as gr

h = 600
w = 600

window = gr.GraphWin("RG", w, h)

alpha = 0.2


def fractal_rectangle(a, b, c, d, deep=10):
    if deep < 1:
        return

    for m, n in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*m), gr.Point(*n)).draw(window)


    a1 = (a[0] * (1 - alpha) + b[0] * alpha, a[1] * (1 - alpha) + b[1] * alpha)
    b1 = (b[0] * (1 - alpha) + c[0] * alpha, b[1] * (1 - alpha) + c[1] * alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0] * (1 - alpha) + a[0] * alpha, d[1] * (1 - alpha) + a[1] * alpha)

    fractal_rectangle(a1, b1, c1, d1, deep - 1)


set = 10
fractal_rectangle((set, set), (w - set, set), (w - set, h - set), (set, h - set), 20)

window.wait_window()
