SIZE = 8


def save_positions(searched_letter, r, index):
    if searched_letter in board[r]:
        positions[index].append(r)
        positions[index].append(board[r].index(searched_letter))


board = []
positions = [[], []]

for row in range(SIZE):
    board.append(input().split())

    # if 'w' in board[row]:
    # positions[0].append(row)
    # positions[0].append(board[row].index('w'))

    # elif 'b' in board[row]:
    # positions[1].append(row)
    # positions[1].append(board[row].index('b'))

    save_positions('w', row, 0)
    save_positions('b', row, 1)

# if the two paws are in columns next to each other, in other words one can take the other this means that the subtract of the columns will always be = 1
# this is the scenario in which we do not have them one next to each other
# size- positions(white) - 1 - ogledalen obraz na white , it is like the two paws are going into the same direction . -1 is get a valid index

if abs(positions[0][1] - positions[1][1]) != 1 or positions[1][0] > positions[0][0]:
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")

else:
    place = (positions[0][0] + positions[1][0]) // 2
    # if w and black are on even or w and black are both on odd positions black wins
    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")

    else:
        print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")
