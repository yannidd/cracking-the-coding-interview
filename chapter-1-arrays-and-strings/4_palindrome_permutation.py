import random


def atoi(ch):
  index = ord(ch)
  if 97 <= index <= 122:
    return index - 97
  else:
    return -1


def is_palindrome_permutation(str1):
  accumulator = [0]*26

  for ch in str1:
    i = atoi(ch)
    if i != -1:
      accumulator[i] += 1
    else:
      return False

  found_odds = False
  for count in accumulator:
    if count % 2 == 1:
      if found_odds:
        return False
      else:
        found_odds = True

  return True


def main():
  str1s = [
      'aabbc',  # True
      'abbc',  # False
      'aabbcc',  # True
  ]
  for str1 in str1s:
    result = is_palindrome_permutation(str1)
    print(f'Is \'{str1}\' a palindrome permutation: {result}')


if __name__ == '__main__':
  main()
