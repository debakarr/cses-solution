"""

CSES - Repetitions



Time limit: 1.00 s
Memory limit: 512 MB



You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input


The only input line contains a string of $n$ characters.

Output


Print one integer: the length of the longest repetition.

Constraints

$1 \le n \le 10^6$

Example


Input:
ATTCGGGA


Output:
3 
"""

if __name__ == "__main__":
    dna_sequence = input()

    previous_char = dna_sequence[0]
    current_count = 1
    max_char = 1
    for dna_char in dna_sequence[1:]:
        if dna_char == previous_char:
            current_count += 1
        else:
            current_count = 1
        max_char = max(max_char, current_count)
        previous_char = dna_char

    print(max_char)
