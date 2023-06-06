rows = int(input())
matrix = []
for _ in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

positions = (
    (-2,-1), # up 2 left 1
    (-2, 1), # up 2 right 1
    (-1,-2), # up 1 left 2
    (-1, 2), # up 1 right 2
    (1,-2), # down 1 left 2
    (1,2), # down 1 right 2
    (2, -1 ), # down 2 left 1
    (2, 1), # down 2 right 1
)
removed_knights = 0

while True:

    max_attacks = 0
    knight_with_max_position = []

    for row_index in range(rows):
        for col_index in range(rows):
            if matrix[row_index][col_index] == 'K':
                attacks = 0

                for pos in positions:   # you go through every possibile moves of the knight
                    row_pos = row_index + pos[0]
                    col_pos = col_index + pos[1]

                    if 0<= row_pos < rows and 0<= col_pos < rows:
                        if matrix[row_pos][col_pos] == 'K':
                            attacks +=1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_max_position = [row_index, col_index]

    if knight_with_max_position:
        matrix[knight_with_max_position[0]][knight_with_max_position[1]] = '0'
        removed_knights +=1
    else:
        break

print(removed_knights)