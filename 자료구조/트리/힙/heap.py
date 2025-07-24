class MinHeap:
    @staticmethod
    def heappush(heap, data):
        heap.append(data)
        MinHeap._shift_up(heap, len(heap) - 1)

    @staticmethod
    def heappop(heap):
        if not heap:
            return "Empty Heap!"
        elif len(heap) == 1:
            return heap.pop()
        
        pop_data, heap[0] = heap[0], heap.pop()
        MinHeap._shift_down(heap, 0, len(heap))
        return pop_data

    @staticmethod
    def heapify(arr):
        last = len(arr) // 2
        for current in range(last - 1, -1, -1):
            MinHeap._shift_down(arr, current, len(arr))

    @staticmethod
    def _shift_up(heap, child):
        while child > 0:
            parent = (child - 1) // 2
            if heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
            else:
                break

    @staticmethod
    def _shift_down(heap, parent, last):
        while parent < last:
            child = parent * 2 + 1
            sibling = child + 1
            if sibling < last and heap[child] > heap[sibling]:
                child = sibling
            if child < last and heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                parent = child
            else:
                break


#테스트 코드
import heapq
h1 = [3, 4, 6, 8, 5, 7]
h2 = [3, 4, 6, 8, 5, 7]

print(f"힙 {h1}에 2를 추가한 결과")
MinHeap.heappush(h1, 2)
heapq.heappush(h2, 2)
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)
print()

print(f"힙 {h1}에 3을 추가한 결과")
MinHeap.heappush(h1, 3)
heapq.heappush(h2, 3)
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)

data1 = MinHeap.heappop(h1)
data2 = heapq.heappop(h2)
print("구현한 함수 pop data =", data1)
print("구현한 함수 pop 이후: ", h1)
print()
print("heapq 함수 pop data =", data2)
print("heapq 함수 pop 이후: ", h2)