Binary search with some quirks.

- Start off with a normal binary search.
- Significant: either the left or the right can be sorted.
- Have an acceptance condition (mid is answer return mid)
- Have a left is sorted condition and a right is sorted condition
- If left is sorted, you know the bounds of it (between lo and mid), so if our
wannabe number isnt in there, we can safely go right
- If right is sorted, you know the bounds of it (between mid and hi), so if our wannabe number isnt
in there, we can safely go left
- If our number is in either of the sorted portions, we can obviously just look in there
- Boom thats it