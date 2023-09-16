from collections import deque

if __name__ == "__main__":
    number = int(input())

    if number == 1:
        print(number)
    elif number < 4:
        print("NO SOLUTION")
    else:
        for num in range(2, number + 1, 2):
            print(num, end=" ")
        for num in range(1, number + 1, 2):
            print(num, end=" ")
