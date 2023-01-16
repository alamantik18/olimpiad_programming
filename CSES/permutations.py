def main(num):
    if num == 1:
        print(num)
    elif num < 4:
        print('NO SOLUTION')
    else:
        for i in range(2, num+1, 2):
            print(i, end=' ')
        for i in range(1, num+1, 2):
            print(i, end=' ')

if __name__ == "__main__":
    input_number = int(input())
    main(input_number)