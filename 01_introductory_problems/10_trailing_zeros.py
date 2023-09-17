"""

CSES - Trailing Zeros



Time limit: 1.00 s
Memory limit: 512 MB



Your task is to calculate the number of trailing zeros in the factorial $n!$.


For example, $20!=2432902008176640000$ and it has $4$ trailing zeros.

Input


The only input line has an integer $n$.

Output


Print the number of trailing zeros in $n!$.

Constraints

$1 \le n \le 10^9$

Example


Input:
20


Output:
4 
"""

if __name__ == "__main__":
    number = int(input())

    count = 0
    power_of_5 = 5

    while power_of_5 <= number:
        count += number // power_of_5
        power_of_5 *= 5

    for power_of_5 in range(5, number + 1, )

    print(count)
