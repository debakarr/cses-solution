"""

CSES - Two Knights



Time limit: 1.00 s
Memory limit: 512 MB



Your task is to count for $k=1,2,\ldots,n$ the number of ways two knights can be placed on a $k \times k$ chessboard so that they do not attack each other.

Input


The only input line contains an integer $n$.

Output


Print $n$ integers: the results.

Constraints

$1 \le n \le 10000$

Example


Input:
8


Output:
0

6

28

96

252

550

1056

1848 
"""


def helper(num: int) -> int:
    k1 = num * num  # number of ways to place the first knight
    k2 = num * num - 1  # number of ways to place the second knight
    together = (
        k1 * k2
    ) // 2  # number of ways to place both knights together without duplication

    attack_area = (num - 1) * (
        num - 2
    )  # number of 2x3 attack area inside a num * num area
    ways_to_attack = (
        attack_area * 4
    )  # number of ways knight can attack each other inside a 2 * 3 area

    place_without_attack = (
        together - ways_to_attack
    )  # number of ways knight can be place so that they don't attack each other
    return place_without_attack


if __name__ == "__main__":
    k = int(input())

    for num in range(1, k + 1):
        print(helper(num))
