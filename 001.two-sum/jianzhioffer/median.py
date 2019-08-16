
def heapify(parent, heap):
    child = 2* parent + 1
    while (len(heap) > child):
        if child + 1 < len(heap):
            if heap
        

def find(nums):
    heapnum = nums//2
    heap = nums[:heapnum+1]
    for i in range(len(heap)//2 -1, -1, -1):
        heapify(i, heap)
    for j in range(heapnum+1, len(nums)):
        if nums[j] > heap[0]:
            heap[0]