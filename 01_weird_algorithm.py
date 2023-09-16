if __name__ == "__main__":
    number = int(input())

    print(number, end="")
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        print(f" {number}", end="")

