import heapq
import sys

class MedianFinder:
    def __init__(self):  # Don't pass any variables, so self only
        self.left_heap = [] # Each object has attributes which are created by the system not passed from the outside
        self.right_heap = [] # They are always empty lists, so no user input here
        

    def add_num(self, num: int) -> None:
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

        if len(self.left_heap) == 0:
            self.left_heap.append(-num)
            heapq.heapify(self.left_heap)
        elif - num > self.left_heap[0]:
            self.left_heap.append(-num)
        else: 
            self.right_heap.append(num)    
        
        if len(self.left_heap) <3 and len(self.right_heap) == 0:
            pass
        elif len(self.left_heap) > len(self.right_heap) + 1:
            self.right_heap.append(-heapq.heappop(self.left_heap))
        elif len(self.right_heap) > len(self.left_heap):
            self.left_heap.append(heapq.heappop(self.right_heap))    


    def find_median(self) -> float:
        if len(self.right_heap) == len(self.left_heap):
            median = round((float(((-heapq.heappop(self.left_heap)) + heapq.heappop(self.right_heap))/2)),5)
        else:
            median = (-heapq.heappop(self.left_heap))
        return median
    
if __name__ == "__main__":    
    m = MedianFinder()
    m.add_num(2)
    m.add_num(3)
    m.add_num(4)



    print(m.find_median())



# if __name__ == "__main__":
#     n = int(input())
#     mf = MedianFinder()
#     for _ in range(n):
#         line = input().strip().split()
#         if line[0] == "add":
#             mf.add_num(int(line[1]))
#         else:
#             print(f"{mf.find_median():.1f}")