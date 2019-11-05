import math


def one_away(str1, str2):
  n_edits = 0

  if len(str1) > len(str2):
    long = str1
    short = str2
  else:
    long = str2
    short = str1

  i = len(long) - 1  # long counter
  j = len(short) - 1  # short counter

  while i > 0 and j > 0:
    if long[i] != short[j]:
      n_edits += 1
      i -= 1
      if n_edits > 1 or abs(j - i) > 1:
        return False
      continue

    i -= 1
    j -= 1

  return True


def main():
  str1 = 'pale'
  str2s = [
      'pa',  # False
      'ple',  # True
      'pale',  # True
      'bale',  # True
      'bake',  # False
  ]

  for str2 in str2s:
    result = one_away(str1, str2)
    print(f'{str1}, {str2} -> {result}')


if __name__ == '__main__':
  main()
