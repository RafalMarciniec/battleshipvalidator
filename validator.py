def validate_battlefield(field):
    ships = {4: 1, 3: 2, 2: 3, 1: 4}
    if sum((value for inner_list in field for value in inner_list if value)) != 20:
        return False
    for row_index, row in enumerate(field):
        for col_index, value in enumerate(row):
            if value:
                if not is_correctly_surrounded(row_index, col_index, 1, field, ships): return False

    return True


def is_correctly_surrounded(row_index, col_index, size, field, ships):
    if size > 4:
        return False
    counter = 0
    coordinate_x = -1
    coordinate_y = -1
    field[row_index][col_index] = 0
    for row in range(row_index - 1, row_index + 2):
        for col in range(col_index - 1, col_index + 2):
            if row in (-1, 10) or col in (-1, 10):
                continue
            try:
                if field[row][col]:
                    counter += 1
                    coordinate_x = row
                    coordinate_y = col
            except IndexError:
                continue
    if counter >= 2:
        return False
    if counter == 0:
        if size == 1:
            if ships[1] == 0:
                return False
            ships[1] -= 1
            return True
        else:
            if ships[size] == 0:
                return False
            ships[size] -= 1
            return True
    if counter == 1:
        if coordinate_x == row_index:
            if not is_correctly_surrounded(row_index, coordinate_y, size + 1, field, ships):
                return False
        else:
            if not is_correctly_surrounded(coordinate_x, col_index, size + 1, field, ships):
                return False
        return True
    return False
