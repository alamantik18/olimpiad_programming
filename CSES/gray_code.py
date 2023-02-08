def main(bits_count: int):
    if bits_count == 0:
        return ['']

    first_half = main(bits_count-1)
    second_half = first_half.copy()
    first_half = ['0' + code for code in first_half]
    second_half = ['1' + code for code in reversed(second_half)]

    return first_half + second_half

if __name__ == '__main__':
    print(*main(int(input())), sep='\n')