"""

CSES - Gray Code



Time limit: 1.00 s
Memory limit: 512 MB



A Gray code is a list of all $2^n$ bit strings of length $n$, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).


Your task is to create a Gray code for a given length $n$.

Input


The only input line has an integer $n$.

Output


Print $2^n$ lines that describe the Gray code. You can print any valid solution.

Constraints

$1 \le n \le 16$

Example


Input:
2


Output:
00

01

11

10 
"""

if __name__ == "__main__":
    number = int(input())

    result = ["0", "1"]

    for _ in range(number - 1):
        first = result[:]
        second = reversed(result)

        result = ["0" + char for char in first] + ["1" + char for char in second]

    for item in result:
        print(item)
