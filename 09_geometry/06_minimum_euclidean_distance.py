"""

CSES - Minimum Euclidean Distance



Time limit: 1.00 s
Memory limit: 512 MB



Given a set of points in the two-dimensional plane, your task is to find the minimum Euclidean distance between two distinct points.


The Euclidean distance of points $(x\_1,y\_1)$ and $(x\_2,y\_2)$ is $\sqrt{(x\_1-x\_2)^2+(y\_1-y\_2)^2}$.

Input


The first input line has an integer $n$: the number of points.


After this, there are $n$ lines that describe the points. Each line has two integers $x$ and $y$. You may assume that each point is distinct.

Output


Print one integer: $d^2$ where $d$ is the minimum Euclidean distance (this ensures that the result is an integer).

Constraints

$2 \le n \le 2 \cdot 10^5$
$-10^9 \le x,y \le 10^9$

Example


Input:
4

2 1

4 4

1 2

6 3


Output:
2 
"""
