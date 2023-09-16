def dfs(nums, aux):
    if not nums:
        return
    
    for i, num in enumerate(nums):
        new_num = nums[:i] + nums[i+1:]
        new_aux = aux + [num]
        if sum(new_num) == sum(new_aux):
            print("YES")
            print(len(new_num))
            print(" ".join(map(str, new_num)))
            print(len(new_aux))
            print(" ".join(map(str, new_aux)))
            exit()
        dfs(new_num, new_aux)


if __name__ == "__main__":
    number = int(input())

    if number < 3:
        print('NO')
    else:
        result = []
        nums = list(range(1, number + 1))
        dfs(nums, [])
    print('NO')
