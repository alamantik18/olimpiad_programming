def main(num: int) -> int:
    return pow(2, num, 10 ** 9 + 7)

if __name__ == "__main__":
    input_number = int(input())
    print(main(input_number))