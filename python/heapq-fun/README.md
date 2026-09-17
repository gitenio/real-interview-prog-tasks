**Key Operations of a Heap**

Heaps support several essential operations that help manage data efficiently while maintaining heap property.
Operation	Function	Description
Create	heapq.heapify()	- Converts a regular list into a valid min-heap

Push	heapq.heappush() -	Adds a new element to the heap while maintaining the heap property

Pop	heapq.heappop()	- Removes and returns the smallest element from the heap

Peek	heap[0]	- Accesses the smallest element without removing it

Push and Pop	heapq.heappushpop() -	Pushes a new element and removes the smallest element in one step

Replace	heapq.heapreplace()	- Removes the smallest element and inserts a new element in one operation

--------------------------------------------
Difference between heapreplace() and heappushpop()

    heapreplace() always pops smallest element and then pushes a new one whereas, heappushpop() pushes new element first, then pops smallest.
    Use heapreplace() when you want the new element to be in the heap and heappushpop() when new element may or may not stay (depending on comparison).

Advantages vs Disadvantages

Fast for insertion and removal with priority.	

Not suitable for complex data manipulations
Uses less memory than some other data types.	
No direct access to middle items.
Simple to use with the heapq module.	
Can’t fully sort the items automatically.
Works in many cases like heaps and priority queues.
Not safe with multiple threads at the same time.