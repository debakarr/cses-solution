"""

CSES - Apples and Bananas



Time limit: 1.00 s
Memory limit: 512 MB



There are apples and bananas and each of them has an integer weight between $1 \ldots k$. Your task is to calculate for each weight $w$ between $2...2k$ the number of ways we can choose an apple and a banana whose combined weight is $w$.

Input

The first input line contains three integers $k$, $n$ and $m$: the number $k$, the number of apples and the number of bananas.

The next line contains $n$ integers $a\_1,a\_2,\ldots,a\_n$: weight of each apple.

The last line contains $m$ integers $b\_1,b\_2,\ldots,b\_m$: weight of each banana.

Output

For each integer $w$ between $2 \ldots 2k$ print the number of ways to choose an apple and a banana whose combined weight is $w$.

Constraints

$1 \le k,n,m \le 2 \cdot 10^5$
$1 \le a\_i \le k$
$1 \le b\_i \le k$

Example

Input:
5 3 4
5 2 5
4 3 2 3

Output:
0 0 1 2 1 2 4 2 0 

Explanation: For example for $w$ = $8$ there are $4$ different ways: we can pick an apple of weight $5$ in two different ways and a banana of weight $3$ in two different ways. 
"""