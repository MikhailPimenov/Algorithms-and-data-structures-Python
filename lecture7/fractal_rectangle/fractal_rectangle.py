import graphics

window = graphics.GraphWin("Rectangle", 500, 500)
window.redraw()
margin = 10
width = window.width
height = window.height


def fractal_rectangle(p1: list, p2: list, p3: list, p4: list, depth: int, alpha: float):
    if depth == 0:
        return

    for (A, B) in (p1, p2), (p2, p3), (p3, p4), (p4, p1):
        graphics.Line(graphics.Point(*A), graphics.Point(*B)).draw(window)

    fractal_rectangle([p1[0] + alpha * (p2[0] - p1[0]), p1[1] + alpha * (p2[1] - p1[1])],
                      [p2[0] + alpha * (p3[0] - p2[0]), p2[1] + alpha * (p3[1] - p2[1])],
                      [p3[0] + alpha * (p4[0] - p3[0]), p3[1] + alpha * (p4[1] - p3[1])],
                      [p4[0] + alpha * (p1[0] - p4[0]), p4[1] + alpha * (p1[1] - p4[1])],
                      depth - 1, alpha)


fractal_rectangle([margin, margin],
                  [width - margin, margin],
                  [width - margin, height - margin],
                  [margin, height - margin],
                  20, 0.15)

window.wait_window(window)
