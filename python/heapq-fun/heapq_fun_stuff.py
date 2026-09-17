import heapq


# ------------------ Initialize an empty list to act as your heap ---------------
grades = []

# Push items onto the heap
heapq.heappush(grades, 85)
heapq.heappush(grades, 92)
heapq.heappush(grades, 74)
heapq.heappush(grades, 89)

# The smallest item is always at index 0 (Peek)
print("Smallest item:", grades[0])  # Output: 74

# Pop items (they come out from smallest to largest)
print(heapq.heappop(grades))  # Output: 74
print(heapq.heappop(grades))  # Output: 85

# ------------------------ converting an existing list ------------------------
numbers = [20, 4, 15, 8, 3]

# Transform the list into a heap in-place
heapq.heapify(numbers)

print("Heapified list:", numbers)
# Output: [3, 4, 15, 8, 20] (Note: The list is a heap tree, not fully sorted!)

# Pop the smallest element
print(heapq.heappop(numbers))  # Output: 3

# ------------------------- Implementing a Priority Queue -------------------

todo_list = []

# Format: (priority_number, task_name)
# Lower priority numbers mean higher urgency (min-heap default)
heapq.heappush(todo_list, (3, "Clean the kitchen"))
heapq.heappush(todo_list, (1, "Fix production bug"))
heapq.heappush(todo_list, (2, "Write documentation"))

# Get the most urgent task
while todo_list:
    priority, task = heapq.heappop(todo_list)
    print(f"Processing task: {task} (Priority: {priority})")

# Output:
# Processing task: Fix production bug (Priority: 1)
# Processing task: Write documentation (Priority: 2)
# Processing task: Clean the kitchen (Priority: 3)

# ------------ finding largest/smallest elems -----------------------------
scores = [50, 99, 82, 34, 76, 91, 22, 64]

# Find the 3 highest scores
top_three = heapq.nlargest(3, scores)
print("Top 3:", top_three)  # Output: [99, 91, 82]

# Find the 2 lowest scores
bottom_two = heapq.nsmallest(2, scores)
print("Bottom 2:", bottom_two)  # Output: [22, 34]

# ------------------------ simulating max heap -------------------------
prices = [100, 500, 250, 900]
max_heap = []

# Invert values on push
for price in prices:
    heapq.heappush(max_heap, -price)

# Invert values back on pop
largest_price = -heapq.heappop(max_heap)
print("Largest price:", largest_price)  # Output: 900

# --------------------- using heap as a max heap ----------------------
nums = [10, 20, 15, 30, 40]

# Convert into a max-heap by inverting values
max_heap = [-n for n in nums]
heapq.heapify(max_heap)

# Access largest element (invert sign again)
print("Largest element:", -max_heap[0])

# ------------------ appending and popping -----------------------------
h = [10, 20, 15, 30, 40]
heapq.heapify(h)
min = heapq.heappushpop(h, 5)
print(min)
print(h)
# Output:
# 5
# [10, 20, 15, 30, 40]

# --------------------- finding largest and smallest -------------------
h = [10, 20, 15, 30, 40]
heapq.heapify(h)

maxi = heapq.nlargest(3, h)
print("3 largest elements:", maxi)

min = heapq.nsmallest(3, h)
print("3 smallest elements:", min)
# Output
#
# 3 largest elements: [40, 30, 20]
# 3 smallest elements: [10, 15, 20]

# ---------------------- Replace and Merge Operations -----------------
h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)

min = heapq.heapreplace(h1, 5)
print(min)
print(h1)

h2 = [2, 4, 6, 8]
h3 = list(heapq.merge(sorted(h1), sorted(h2)))
print("Merged heap:", h3)

# Output:
# 10
# [5, 20, 15, 30, 40]
# Merged heap: [2, 4, 5, 6, 8, 15, 20, 30, 40]
