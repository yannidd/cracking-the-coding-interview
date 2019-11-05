def compress(str1):
  compressed = []

  counter = 1
  current = str1[0]
  for ch in str1[1:]:
    if ch == current:
      counter += 1
    else:
      compressed.extend([current, str(counter)])
      current = ch
      counter = 1
  compressed.extend([current, str(counter)])

  if len(compressed) >= len(str1):
    return str1
  else:
    return compressed


def main():
  str1s = [
      'abcd',  # abcd
      'aabbbccccdd',  # a2b3c4d2
      'abbd',  # abbd
      'aabd',  # aabd
      'abdd',  # abdd
      'abddddd',  # a1b1d5
  ]

  for str1 in str1s:
    result = ''.join(compress(str1))
    print(f'{str1} compressed is {result}')


if __name__ == '__main__':
  main()
