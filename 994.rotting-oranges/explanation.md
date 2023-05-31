Basically, this is one big case of BFS. 

Simple algorithm, sweety:
1. Collect all the twos into a queue (motherFIFO)
2. Increment INT fresh for each 1 you see
3. pop from queue, turning adjacent 1's to 2's (you rotting them mfs), decrement fresh, add new rotting boys queue
4. keep track of the level you on, and change levels accordingly 
(this can be done by keeping a snapshot of the qsize and decrementing this, once it hits zero, get a new snapshot and increment your minutes)
5. when queues empty, return minutes - 1, (off-by-one) if fresh is 0, else -1
6. donezo