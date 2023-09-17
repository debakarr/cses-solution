"""

CSES - Coin Piles



Time limit: 1.00 s
Memory limit: 512 MB



You have two coin piles containing $a$ and $b$ coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.


Your task is to efficiently find out if you can empty both the piles.

Input


The first input line has an integer $t$: the number of tests.


After this, there are $t$ lines, each of which has two integers $a$ and $b$: the numbers of coins in the piles.

Output


For each test, print "YES" if you can empty the piles and "NO" otherwise.

Constraints

$1 \le t \le 10^5$
$0 \le a, b \le 10^9$

Example


Input:
3

2 1

2 2

3 3


Output:
YES

NO

YES 
"""

if __name__ == "__main__":
    number_of_test = int(input())

    for _ in range(number_of_test):
        first, second = map(int, input().split())

        # while first > 0 and second > 0:
        #     if first >= second:
        #         first -= 2
        #         second -= 1
        #     else:
        #         first -= 1
        #         second -= 2

        # if first == 0 and second == 0:
        #     print("YES")
        # else:
        #     print("NO")

        # check that the max is less than twice of min
        # if the piles with max number have more than twice the number of coins in the other pile,
        # then even if we remove 2 times the number from the greater pile, the coins in the lesser pile will exhaust
        if max(first, second) > 2 * min(first, second):
            print("NO")
            continue

        # say we remove 2 coins from first and 1 coin from second pile x number of time
        # and we remove 1 coin from first and 2 coins from second pile y number of time
        # for pile to empty, we should have:
        # first - 2x - y = 0
        # second - x - 2y = 0
        # first + second - 2x - y - x - 2y = 0
        # first + second = 3x + 3y i.e 3(x + y)
        # So it should be divisible by 3
        if (first + second) % 3 != 0:
            print("NO")
        else:
            print("YES")
