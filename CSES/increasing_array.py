def main(mass: list) -> int:
    moves = 0
    for i in range(len(mass) - 1):
        if mass[i] > mass[i+1]:
            moves += mass[i] - mass[i+1]
            mass[i+1] = mass[i]
    return moves

if __name__ == "__main__":
    number = int(input())
    input_mass = [int(i) for i in input().split()]
    print(main(input_mass))