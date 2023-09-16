if __name__ == "__main__":
    number = int(input())
    array = [int(num) for num in input().split()]

    moves = 0
    prev = array[0]
    for num in array[1:]:
        if num < prev:
            moves += prev - num
        else:
            prev = num

    print(moves)
