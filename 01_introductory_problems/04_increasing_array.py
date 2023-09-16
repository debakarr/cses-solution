"""

CSES - Increasing Array



Time limit: 1.00 s
Memory limit: 512 MB



You are given an array of $n$ integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one. What is the minimum number of moves required?

Input

The first input line contains an integer $n$: the size of the array.

Then, the second line contains $n$ integers $x\_1,x\_2,\ldots,x\_n$: the contents of the array.

Output

Print the minimum number of moves.

Constraints

 $1 \le n \le 2 \cdot 10^5$
 $1 \le x\_i \le 10^9$

Example

Input:
5
3 2 5 1 7

Output:
5 
"""

if __name__ == "__main__":
    number = int(input())
    array = [int(num) for num in input().split()]

    moves = 0
    prev = array[0]
    for num in array[1:]:
        if num < prev:
            moves += prev - num
        else:
            prev = num

    print(moves)

