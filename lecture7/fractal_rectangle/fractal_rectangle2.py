from graphics import *


def fractal_rectangle(window, A1, A2, B1, B2, C1, C2, D1, D2, alpha, n):
    if n < 1:
        return

    Line(Point(A1, A2), Point(B1, B2)).draw(window)
    Line(Point(B1, B2), Point(C1, C2)).draw(window)
    Line(Point(C1, C2), Point(D1, D2)).draw(window)
    Line(Point(D1, D2), Point(A1, A2)).draw(window)

    a1 = A1 * (1 - alpha) + B1 * alpha
    a2 = A2 * (1 - alpha) + B2 * alpha
    b1 = B1 * (1 - alpha) + C1 * alpha
    b2 = B2 * (1 - alpha) + C2 * alpha
    c1 = C1 * (1 - alpha) + D1 * alpha
    c2 = C2 * (1 - alpha) + D2 * alpha
    d1 = D1 * (1 - alpha) + A1 * alpha
    d2 = D2 * (1 - alpha) + A2 * alpha

    fractal_rectangle(window, a1, a2, b1, b2, c1, c2, d1, d2, alpha, n - 1)


window = GraphWin("Window", 400, 400)
fractal_rectangle(window, 0, 0, 300, 0, 300, 300, 0, 300, 0.15, 20)

window.redraw()
window.wait_window(window)
