def prepare_row(row):
    return row[1:-1].split(",")


def prepare_table(str_array):
    return [prepare_row(row) for row in str_array]


def is_valid_row(row_value, row):
    return row.count(row_value) == 1


def is_valid_column(column_value, row_index, column_index, table):
    for i in range(9):
        if row_index != i and table[i][column_index] == column_value:
            return False
    return True


def row_colum_by_quadrant(quadrant):
    values = {
        "1": (2, 2),
        "2": (2, 5),
        "3": (2, 8),
        "4": (5, 2),
        "5": (5, 5),
        "6": (5, 8),
        "7": (8, 2),
        "8": (8, 5),
        "9": (8, 8),
    }
    return values[quadrant]


def is_valid_quadrant(column_value, row_index, column_index, quadrant, table):
    max_row, max_column = row_colum_by_quadrant(quadrant)
    repeated = {column_value}
    for row in range(max_row - 2, max_row + 1):
        for col in range(max_column - 2, max_column + 1):
            if column_index != col and row_index != row:
                if table[row][col] in repeated:
                    return False
                if table[row][col] != "x":
                    repeated.add(table[row][col])
    return True


def identify_quadrant(row_index, col_index):
    if col_index < 3:
        # q = 1,4,7
        if row_index < 3:
            return "1"
        elif row_index < 6:
            return "4"
        else:
            return "7"
    elif col_index < 6:
        # q = 2, 5, 8
        if row_index < 3:
            return "2"
        elif row_index < 6:
            return "5"
        else:
            return "8"
    else:
        # q = 3, 6, 9
        if row_index < 3:
            return "3"
        elif row_index < 6:
            return "6"
        else:
            return "9"


def matrix_challenge(str_array):
    quadrants = set()

    table = prepare_table(str_array)

    for row_index, row in enumerate(table):
        for column_index, column_value in enumerate(row):
            # check if the value is empty or has value
            if column_value != "x":
                quadrant = identify_quadrant(row_index, column_index)
                # check row
                valid_row = is_valid_row(column_value, row)
                # check column
                valid_colum = is_valid_column(
                    column_value, row_index, column_index, table
                )
                # check quadrant
                valid_quadrant = is_valid_quadrant(
                    column_value, row_index, column_index, quadrant, table
                )
                # if one fails check what cuadrant is
                if not valid_row or not valid_colum or not valid_quadrant:
                    quadrants.add(quadrant)

    return ",".join(sorted(quadrants)) if quadrants else "legal"


if __name__ == "__main__":
    input_val = [
        "(1,2,3,4,5,6,7,8,9)",
        "(x,x,x,x,x,x,x,x,x)",
        "(6,x,5,x,3,x,x,4,x)",
        "(2,x,1,5,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,9)",
        "(x,x,x,x,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,9)",
        "(9,1,2,3,4,5,6,7,8)",
    ]
    matrix_challenge(input_val)
