""" Two Names, One Shirt """

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

red = shirt()
print(red)
crimson = red
print(crimson)

print(id(red))
print(id(crimson))

print(red.clean)
print(crimson.clean)

red.make_dirty()
print(red.make_dirty())
print(red.clean)
print(crimson.clean)

print(red is crimson)

crimson = shirt()
print(id(red))
print(id(crimson))
print(crimson.clean)
red.make_clean()
print(red.clean)
print(crimson.clean)

print(red is crimson)