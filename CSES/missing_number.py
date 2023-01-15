def main(num: int, string: str) -> int:
    return sum(range(num + 1)) - sum(map(int, string.split(' ')))

if __name__ == "__main__":
    input_number, input_string = int(input()), input()
    print(main(input_number, input_string))