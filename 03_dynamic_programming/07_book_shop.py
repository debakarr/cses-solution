"""

CSES - Book Shop



Time limit: 1.00 s
Memory limit: 512 MB



You are in a book shop which sells $n$ different books. You know the price and number of pages of each book.

You have decided that the total price of your purchases will be at most $x$. What is the maximum number of pages you can buy? You can buy each book at most once.

Input

The first input line contains two integers $n$ and $x$: the number of books and the maximum total price.

The next line contains $n$ integers $h\_1,h\_2,\ldots,h\_n$: the price of each book.

The last line contains $n$ integers $s\_1,s\_2,\ldots,s\_n$: the number of pages of each book.

Output

Print one integer: the maximum number of pages.

Constraints

$1 \le n \le 1000$
$1 \le x \le 10^5$
$1 \le h\_i, s\_i \le 1000$

Example

Input:
4 10
4 8 5 3
5 12 8 1

Output:
13

Explanation: You can buy books 1 and 3. Their price is $4+5=9$ and the number of pages is $5+8=13$. 
"""