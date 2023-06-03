Recursion factorial algorithm.

ex: 1, 2, 3

                    []
                [1] [2] [3]
[1, 2] [1, 3]  [2, 3] [2, 1]  [3, 1] [3, 2]
etc...
There is a branch of all perms that start with 1, then 2, then 3. 
So base case: when there is only one remaining number
recursive case: for each number in the remaining numbers, make each one the next number in the permutation building prefix. Update remaining numbers.
ex: prefix = [1, 2] and remaining = [3, 4]
then make two prefixes [1, 2, 3] and [1, 2, 4] and remaining [4] and [3] respectively.
Recurse on these values. Ensure every call has its own copy of the lists.