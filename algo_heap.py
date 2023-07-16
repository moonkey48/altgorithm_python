from heapq import heappush, heappop, heapify, nsmallest

# heappush
heap = []
heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 2)
print(heap)
print(heappop(heap))

# heapify
arr = [1,5,32,6,7,3]
heapify(arr)
print(arr)


# maxHeap
nums = [1,4,2,5,6]
max_heap = []

for num in nums:
    heappush(max_heap, (-num, num))
# while heap:
#     print(heappop(max_heap)[1])
    
# n번째 작은 값
print(nsmallest(3,[3,21,6,7,2])[-1])


# heap_sort
def heap_sort(num_arr):
    heapify(num_arr)
    sorted_nums = []
    while heap:
        if len(heap) != 0:
            sorted_nums.append(heappop(num_arr))
    return sorted_nums
    
print(heap_sort([2,5,12,5,9,31,8]))