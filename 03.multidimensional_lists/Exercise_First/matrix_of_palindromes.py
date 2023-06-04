rows, cols  = [int(el) for el in input().split()]

start = ord('a')

for row_index in range(start, start+rows):
  for col_index in range(start, start+cols):
    print(f"{chr(row_index)}{chr(row_index+col_index - start)}{chr(row_index)}", end =' ')

  print()
