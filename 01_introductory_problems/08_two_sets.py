"""

CSES - Two Sets



Time limit: 1.00 s
Memory limit: 512 MB



Your task is to divide the numbers $1,2,\ldots,n$ into two sets of equal sum.

Input


The only input line contains an integer $n$.

Output


Print "YES", if the division is possible, and "NO" otherwise.


After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints

 $1 \le n \le 10^6$

Example 1


Input:
7


Output:
YES

4

1 2 4 7

3

3 5 6

Example 2


Input:
6


Output:
NO 
"""

if __name__ == "__main__":
    number = int(input())

    total = sum(range(1, number + 1))

    if total % 2 != 0:
        print("NO")
    else:
        print("YES")

        expected_sum = int(total / 2)
        set1, set2 = set(), set()

        for num in range(number, 0, -1):
            if expected_sum - num >= 0:
                set1.add(num)
                expected_sum -= num
            else:
                set2.add(num)

        print(len(set1))
        print(" ".join(map(str, set1)))
        print(len(set2))
        print(" ".join(map(str, set2)))
