def main(num):
    for i in range(1, num+1):
        print(((i ** 2 * ((i ** 2) - 1)) - 8 - 24 - 16 * (i - 4) - 16 - 24 * (i - 4) - (i - 4) ** 2 * 8) // 2)

if __name__ == "__main__":
    input_number = int(input())
    main(input_number)