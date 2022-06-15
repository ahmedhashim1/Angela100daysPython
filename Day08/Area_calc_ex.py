import math

# numer of cans = (wall height x wall width) / coverage per can
def paint_calc(height, width, cover):
    num_of_paints = math.ceil((height * width) / cover)
    print(f"You'll need {num_of_paints} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)