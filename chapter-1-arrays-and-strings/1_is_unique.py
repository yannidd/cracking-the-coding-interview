def is_unique(letters):
  if len(letters) > 128:
    return False

  accumulator = [False]*128

  for ch in letters:
    index = ord(ch)

    if accumulator[index]:
      return False

    accumulator[index] = True

  return True


def main():
  letterss = [
    'asdf',
    'aasdf',
    'asdff',
    'assdf',
  ]

  for letters in letterss:
    result = is_unique(letters)
    print(f'Is {letters} unique: {result}')

if __name__ == '__main__':
  main()
