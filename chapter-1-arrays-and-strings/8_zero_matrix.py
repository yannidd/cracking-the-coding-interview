def print_matrix(matrix):
  for row in matrix:
    for col in row:
      print(f'{col:>5}', end='')
    print()


def zero_matrix(in_matrix):
  width = len(in_matrix[0])
  height = len(in_matrix)
  zero_columns = []
  zero_rows = []
  out_matrix = [[0]*width for _ in range(height)]

  for i in range(height):
    for j in range(width):
      if in_matrix[i][j] == 0:
        zero_rows.append(i)
        zero_columns.append(j)

  for i in range(height):
    for j in range(width):
      if j in zero_columns or i in zero_rows:
        continue
      out_matrix[i][j] = in_matrix[i][j]

  return out_matrix


def main():
  in_matrix = [
      [0, 2, 0],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12],
  ]

  out_matrix = zero_matrix(in_matrix)

  print('Input matrix:')
  print_matrix(in_matrix)
  print('Output matrix:')
  print_matrix(out_matrix)


if __name__ == '__main__':
  main()
