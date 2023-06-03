Dynamic programming...

decision tree, start from 0, build up to target.
Use recursion.
Avoid duplicates by only using decisions that are equal to or greater than
the previous decision. This makes every solution sorted and unique.
Ex. just added 3? Only add 3 or 4 or 5..... never add 1 or 2 because those will
be handled by their own branch.