"""

CSES - Palindrome Reorder



Time limit: 1.00 s
Memory limit: 512 MB



Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input


The only input line has a string of length $n$ consisting of characters A-Z.

Output:


Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Constraints

$1 \le n \le 10^6$

Example


Input:
AAAACACBA


Output:
AACABACAA 
"""

from collections import Counter, deque

if __name__ == "__main__":
    string = input()

    counter = Counter(string)

    odd_count = 0
    odd_count_char = None
    for char, count in counter.items():
        if count % 2 != 0:
            odd_count += 1
            odd_count_char = char

    if odd_count > 1:
        print("NO SOLUTION")
    else:
        palindrome = deque()
        if odd_count_char:
            palindrome.append(odd_count_char)
            counter[odd_count_char] -= 1
        for char, count in counter.items():
            for _ in range(1, count + 1, 2):
                palindrome.appendleft(char)
                palindrome.append(char)

        print("".join(palindrome))
