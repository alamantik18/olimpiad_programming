def main(string: str) -> int:
    count, tmp_count = 0, 0
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            tmp_count += 1
            count = tmp_count if count < tmp_count else count
        else:
            tmp_count = 0
    return count + 1

if __name__ == "__main__":
    input_string = input().upper()
    print(main(input_string))