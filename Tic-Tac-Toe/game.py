def coor_to_px(coordinates):
    x, y = coordinates
    return (x * 200, y * 200)

# CreateMatrix function
# 1 is equivalent to cross and 2 to zero


def createMatrix():
    for x in range(3):
        for y in range(3):
            if matrix[y][x] == 0:
                screen.blit(box, coor_to_px((x, y)))
            elif matrix[y][x] == 1:
                screen.blit(cross, coor_to_px((x, y)))
            else:
                screen.blit(zero, coor_to_px((x, y)))

# Position to Coordinate


def pos_to_coord(x, y):
    x = (x/200) % 3
    y = (y/200) % 3
    return int(x), int(y)