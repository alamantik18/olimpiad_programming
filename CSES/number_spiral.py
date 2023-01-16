def main(num, mass):
    for i in range(num):
        y, x = mass[i]
        if x > y:
            print(x ** 2 - y + 1 if x % 2 == 1 else (x-1) ** 2 + y)
        else:
            print(y ** 2 - x + 1 if y % 2 == 0 else (y - 1) ** 2 + x)

if __name__ == "__main__":
    input_number = int(input())
    input_mass = [tuple(int(i) for i in input().split()) for j in range(input_number)]
    main(input_number, input_mass)