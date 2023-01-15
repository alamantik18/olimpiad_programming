def main(numeric):
    while numeric > 1:
        print(numeric, end=' ')
        numeric = numeric * 3 + 1 if numeric % 2 != 0 else numeric // 2
    print(1)

if __name__ == "__main__":
    input_number = int(input())
    main(input_number)