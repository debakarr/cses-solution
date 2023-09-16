if __name__ == "__main__":
    n = int(input())

    numbers = [int(number) for number in input().split()]
    
    sum_of_n_numbers = (n * (n+1)) // 2
    sum_of_input_numbers = sum(numbers)
    print(sum_of_n_numbers - sum_of_input_numbers)

