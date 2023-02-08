def main():
    coin_piles = [tuple(map(int, input().split(' '))) for _ in range(int(input()))]

    for i in range(len(coin_piles)):
        pile_1, pile_2 = coin_piles[i]
        print('YES' if pile_1 <= 2 * pile_2 and pile_2 <= 2 * pile_1 and (pile_2 + pile_1) % 3 == 0 else 'NO')

if __name__ == "__main__":
    main()