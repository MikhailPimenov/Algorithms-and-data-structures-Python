# lecture 18
# class
# named_tuple
# linked_list


class Goat:
    legs_number = 4

    def __init__(self, weight=30, height=50):
        self.weight = weight
        self.height = height

    def __str__(self):
        string = "Goat: weight = " + str(self.weight) + "  height = " + str(self.height)
        return string


def test_class_Goat():
    notka = Goat()
    nada = Goat(35, 50)

    goats = [notka, nada]

    for k in goats:
        print(k)


from collections import namedtuple


def test_namedtuple():
    Point = namedtuple("Point", "x y z")
    a1 = Point(2, 3, 4)
    a2 = Point(-1, 0, 0)

    distance = ((a1.x - a2.x) ** 2 + (a1.y - a2.y) ** 2 + (a1.z - a2.z) ** 2) ** 0.5
    print(distance)


def test_linked_list():
    a = [10]
    a.append([20])
    a[1].append([30])
    a[1][1].append([40])
    a[1][1][1].append([50, None])

    p = a
    while p is not None:
        print(p[0])
        p = p[1]


# test_class_Goat()
# test_namedtuple()
test_linked_list()
