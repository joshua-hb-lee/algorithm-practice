# Heap

메모리에 있는 Heap이 아니다...

- [Complete Binary Tree](https://codingdog.tistory.com/entry/%EC%99%84%EC%A0%84%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC-vs-%ED%8F%AC%ED%99%94%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC-%EC%9D%B4-%EB%91%98%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B4%85%EC%8B%9C%EB%8B%A4) with fast searching the max or min value
- The time complexity of array = $O(n)$
- heap is $O(logn)$, more effiecent than array
- heap is used to implement **PriorityQueue**

## :pushpin: 이진 탐색 트리와 공통점, 차이점

- 공통점
  - 이진 트리에 기반(부모노드에 자식노드가 2개)
- 차이점
  - 힙은 자식노드보다 부모노드가 크기만(혹은 작기만)하면 된다.
  - 이진 탐색 트리는 `왼쪽노드 < 부모노드 < 오른쪽노드` 순으로 크기
  - 힙은 최대값, 최소값 검색 / 이진 탐색 트리는 탐색

## :pushpin: Heap Implementation

```java
public class Heap {
  // array 크기는 제한
  private int[] array;
  // 실제 heap에 있는 데이터 개
  private int size;

  private static final int MAX_SIZE = 10001;

  public Heap() {
    array = new int[MAX_SIZE];
    size = 0;
  }
  /**
  * heap 구조에 insert 기능
  * @param data	insert할 데이터
  */
  public boolean insert(int data) {
    if(isFull())
      return false;
    
    if(size == 0) {
      array[1] = data;
      size = 1;
      return true;
    }
    
    int index = ++size;
    array[index] = data;
    
    while(index > 1) {
      if(array[index/2] >= array[index]) break;
      
      swap(array, index/2, index);
      
      index /= 2;
    }
    
    return true;
  }

  /**
  * heap의 최대값(root node) 추출
  */
  public int popMax() {
    if(isEmpty())
      return -1;
    
    int max = array[1];
    
    if(size == 1) {
      size = 0;
      return max;
    }
    
    // swap root and last node
    swap(array, 1, size);
    array[size] = 0;
    size--;
    
    int index = 1;
    int maxIndex = 0;
    while(size >= index * 2) {
      if(array[index * 2] < array[index * 2 + 1]) 
        maxIndex = index * 2 + 1;
      else 
        maxIndex = index * 2;
      
      if(array[index] < array[maxIndex])
        swap(array, index, maxIndex);
      
      index = maxIndex;
    }
    
    return max;
  }

  private void swap(int[] arr, int x, int y) {
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
  }

  public boolean isFull() {
    if(size >= 10000)
      return true;
    
    return false;
  }

  public boolean isEmpty() {
    if(size == 0) 
      return true;
    
    return false;
  }

  public int[] getArray() {
    return array;
  }

  public int getSize() {
    return size;
  }
}
```

```python
# [[1, 'a'], [2, 'b'], [4, 'c'], [6, 'd'], [7, 'g'], [8, 'f'], [9, 'z']]
class Heap():
    def __init__(self) -> None:
        self.array = []
        self.size = 0
    
    def swapNode(self, x_idx, y_idx):
        tmp = self.array[y_idx]
        self.array[y_idx] = self.array[x_idx]
        self.array[x_idx] = tmp
        
        
    def minHeapifyFromRoot(self):
        if (self.size == 0):
            return
        
        # start from the root
        index = 0
        
        # doing loop until the index's node has any children
        while self.size > index * 2 + 1:
            left = 2 * index + 1
            right = 2 * index + 2
            
            # if right children does not exist, left is used
            if right >= self.size:
                min_idx = left
            else:
                # or compare left with right and decide the smaller one
                min_idx = right if self.array[left][0] > self.array[right][0] else left
            
            # if minheap is valid, just end the process
            if self.array[index][0] > self.array[min_idx][0]:
                return
            
            # swap
            self.swapNode(index, min_idx)
            index = min_idx
    
    def minHeapifyFromTheLast(self):
        if (self.size == 0):
            return
        
        # start from the last one
        index = self.size - 1 # last one
        
        # doing loop until reaching the root
        while index > 0:
            parent_idx = int((index - 1) / 2)
            # if minheap is valid, just end the process
            if self.array[index][0] > self.array[parent_idx][0]:
                return
            
            # swap
            self.swapNode(index, parent_idx)
            index = parent_idx
    
    def append(self, element):
        self.array.append(element)
        self.size += 1
        
        self.minHeapifyFromTheLast()
        print(self.array)
    
    def minpop(self):
        if (self.size == 0):
            return -1
        
        min_value = self.array[0]
        
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        
        self.minHeapifyFromRoot()
        
        return min_value

    def __str__(self):
        return f"{self.array})"
    
if __name__ == "__main__":
    heap = Heap()
    heap.append([5, 'a'])
    heap.append([3, 'c'])
    heap.append([11, 'f'])
    heap.append([21, 'b'])
    heap.append([7, 'v'])
    heap.append([15, 'g'])
    
    print(heap.minpop())
    print(heap.minpop())
    print(heap.minpop())
    print(heap.minpop())
    print(heap.minpop())
    print(heap.minpop())
```

- `insert`
  - 완전 이진 트리 순서대로 맨 마지막 Node에 새로운 데이터 insert
  - 마지막 insert된 노드부터 부모 노드와 비교를 통해 swap
  - 루트 노드까지 진행
  - size가 full인 상황이면 `false` return
- `popMax`
  - Max Heap 기준으로 최대값 추출
  - 루트 노드를 우선 따로 할당해놓는다. (추출)
  - 루트 노드를 시작으로 2개의 자식노드 중에 더 큰 노드와 비교를 통해 swap  
    (왼쪽 자식노드만 있어도 어차피 값이 없는 노드는 0으로 초기화 되기 때문에 그대로 비교 진행하면 됨)
  - 비교하려는 자식노드가 2개 다 없을 때까지 반복 진행  
    (현재 노드에서 2를 곱한 index가 왼쪽 자식노드이기에 size가 index*2보다 작으면 자식노드가 아예 없다는 의미)
  - heap이 비어있으면 `-1` 반환

## 시간 복잡도

- insert, pop: `O(logn)`
- 50%에 대한 비용이 각 단계마다 절감된다는 의미