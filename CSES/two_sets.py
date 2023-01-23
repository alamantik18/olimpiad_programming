def main(num):
    su = num * (num + 1) // 2
    first_set, second_set = set(), set()

    if su % 2 == 0:
        print('YES')
        subset_sum = su // 2
        for i in range(num, 0, -1):
            if i <= subset_sum:
                subset_sum -= i
                first_set.add(i)
            else:
                second_set.add(i)

        print(len(second_set))
        print(*second_set)
        print(len(first_set))
        print(*first_set)
    else:
        print('NO')

if __name__ == "__main__":
    input_number = int(input())
    main(input_number)