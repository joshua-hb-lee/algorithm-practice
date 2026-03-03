# Quick Sort

```java
public class QuickSort {
  public static void quickSort(int[] arr) {
      
    sort(arr, 0, arr.length-1);
  }
  
  public static void sort(int[] arr, int start, int end) {
    if(start >= end) return;
    
    int pivotIdx = splitAndSwap(arr, start, end);
    
    sort(arr, start, pivotIdx - 1);
    sort(arr, pivotIdx, end);
  }
  
  public static int splitAndSwap(int[] arr, int start, int end) {
    
    int pivot = arr[(start + end) / 2];
    
    while(start <= end) {
      while(pivot > arr[start]) start++; 
      while(pivot < arr[end]) end--;
      
      if(start <= end) {
        swap(arr, start, end);
        start++;
        end--;
      }
    }
    
    return start;
  }

  //...

}
```
- pivot 기준으로 left, right 배열 객체를 생성해 나눠 저장하는 방식은 성능상 비효율적이다. (재귀호출때마다 배열객체 생성)
- in-place 정렬이 이런면에서 효율적 (해당 배열에 바로 적용)
- [[알고리즘] 퀵 정렬 - Quick Sort (Python, Java)](https://www.daleseo.com/sort-quick/)

```
[6, 5, 1, 4, 7, 2, 3]
[3, 5, 1, 4, 7, 2, 6]
[3, 2, 1, 4, 7, 5, 6]

[3, 2, 1, 4, 7, 5, 6]
[1, 2, 3, 4, 7, 5, 6]

[1, 2, 3, 4, 5, 7, 6]
[1, 2, 3, 4, 5, 6, 7]
```

<br>

# place the pivot on the far right

```java
class QuickSort {
  static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];

    // index of smaller element than pivot value
    int smallPosition = low - 1;

    // traverse array from low to high position
    // move all smaller elements than pivot to the left side of pivot.
    for (int traverse = low; traverse <= high -1; traverse++) {
      if (arr[traverse] < pivot) {
        smallPosition++;
        swap(arr, smallPosition, traverse);
      }
    }

    // move pivot to the next position of last small element.
    // (smallPosition + 1) > next position of last one.
    swap(arr, smallPosition + 1, high);

    return smallPosition + 1;
  }

  static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
      // index of pivot
      int pi = partition(arr, low, high);

      // divide into two part except pivot
      quickSort(arr, low, pi - 1);
      quickSort(arr, pi + 1, high);
    }
  }

  public static void main(String[] args) {
    int[] arr = {6, 5, 1, 4, 7, 2, 3};

    quickSort(arr, 0, arr.length - 1);
  }
}
```