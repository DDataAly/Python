import heapq

class MedianFinder:
    def __init__(self):  
        self.left_heap = [] 
        self.right_heap = [] 
        

    def add_num(self, num: int) -> None:
        if len(self.left_heap) == 0 or - num > self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        else: 
            heapq.heappush(self.right_heap, num)  
        
        if len(self.left_heap) > len(self.right_heap) + 1:
            heapq.heappush(self.right_heap, (-heapq.heappop(self.left_heap)))
        elif len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, (-heapq.heappop(self.right_heap)))


    def find_median(self) -> float:
        if len(self.right_heap) == len(self.left_heap):
            median = ((-self.left_heap[0]) + (self.right_heap[0]))/2
        else:
            median = (-self.left_heap[0])
        return median
    

if __name__ == "__main__":    
    m = MedianFinder()
    m.add_num(2)
    m.add_num(3)
    m.add_num(4)
    m.add_num(5)
    print(m.find_median())


# Hackerrank running block
# if __name__ == "__main__":
#     n = int(input())
#     mf = MedianFinder()
#     for _ in range(n):
#         line = input().strip().split()
#         if line[0] == "add":
#             mf.add_num(int(line[1]))
#         else:
#             print(f"{mf.find_median():.1f}")




