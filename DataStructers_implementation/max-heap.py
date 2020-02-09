class maxHeap:
    def __init__(self):
        self.heap = []

    # O(logn)
    def insert(self,val):
        # add val to the list.
        self.heap.append(val)
        self.__percolateUp(len(heap)-1)

    # O(1)
    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    # O(logN) max num of nodes traversed
    def removeMax(self):
        if len(self.heap)>1:
            max_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max_val
        elif len(self.heap) == 1:
            max_val = self.heap[0]
            del self.heap[0]
            return max_val
        else:
            return None

    # O(logN)
    def __percolateUp(self, index):
        parent_index = (index-1)/2
        if index <=0:
            return
    elif self.heap[parent_index] < self.heap[index]:
        # swap
        temp = self.heap[]
        self.heap[parent_index] = self.heap[index]
        self.heap[index] = temp
        # call it recursively
        self.__percolateUp(self,parent_index)
    # O(logN)
    def __maxHeapify(self,index):
        left = (index *2)+1
        right = (index * 2)+2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap)> right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != right:
            temp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = temp
            self.__maxHeapify(largest)

heap = maxHeap()
