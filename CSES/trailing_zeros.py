def main(num: int) -> int:
    counter, i = 0, 5
    while num / i >= 1:
        counter += int(num/i)
        i *= 5
    return int(counter)

if __name__ == "__main__":
    input_number = int(input())
    print(main(input_number))