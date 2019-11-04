def print_char_list(str1, end=''):
  for ch in str1:
    print(ch, end=end)


def urlify(str1, length):
  end = len(str1) - 1

  for i in reversed(range(length)):
    if str1[i] != ' ':
      str1[end] = str1[i]
      end -= 1
    else:
      str1[end - 2:end + 1] = list('%20')
      end -= 3


def main():
  str1 = list('Mr John Smith    ')  # Extra spaces in the end because operation
                                    # will be in place.

  print('Urlification of \'', end='')
  print_char_list(str1)

  urlify(str1, 13)  # In place urlification.
  
  print('\' is \'', end='')
  print_char_list(str1)
  print('\'.')


if __name__ == '__main__':
  main()
