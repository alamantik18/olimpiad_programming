def main(string: str) -> str:
    mass, m, half, x = sorted(list(set(string))), '', '', 0

    if len(string) == 1:
        return string

    for element in mass:
        element_count = string.count(element)
        if element_count % 2 == 0:
            half += element * (element_count//2)
        elif x == 1:
            half = 0
            return 'NO SOLUTION'
        else:
            x = 1
            m = element
            half += element * ((element_count-1)//2)

    if half:
        return half + m + half[::-1]

if __name__ == '__main__':
    print(main(input()))