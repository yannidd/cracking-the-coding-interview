def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    accumulator1 = [0]*128
    accumulator2 = [0]*128

    for ch in str1:
        accumulator1[ord(ch)] += 1

    for ch in str2:
        accumulator2[ord(ch)] += 1

    for i in range(128):
        if accumulator1[i] != accumulator2[i]:
            return False

    return True


def main():
    str1 = 'abcdd'
    str2s = [
        'dbcda',  # True
        'abcd',  # False
        'ddcba',  # True
        'abcddd',  # False
    ]

    for str2 in str2s:
        result = check_permutation(str1, str2)
        print(f'Is {str2} a permutation of {str1}: {result}')


if __name__ == '__main__':
    main()
