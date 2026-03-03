# Selection Sort

```java
public class SelectionSort {

	static void selectionSort(int[] data) {

		for (int i = 0; i < data.length - 1; i++) {
			int idxLowest = i;

			for (int j = i + 1; j < data.length; j++) {
				if (data[idxLowest] > data[j])
					idxLowest = j;
			}

			swap(data, idxLowest, i);
		}
	}
	
	static void swap(int[] arr, int a, int b) {
		int tmp = arr[a];
		arr[a] = arr[b];
		arr[b] = tmp;
	}

	public static void main(String[] args) {

		int[] data = { 14, 12, 7, 3, 4, 8, 20, 9, 17 };

		selectionSort(data);

		for (int i = 0; i < data.length; i++)
			System.out.println(data[i]);
	}

}
```

- 반복문이 두 개 $O(n^2)$
    - 실제로 상세하게 계산하면, ${ n * (n - 1)}/{ 2 }$

맨 첫번째부터 기준으로 `idxLowest`로 marking  
오른 방향으로 반복하면서 `idxLowest` 기준값보다 작은 것이 있으면 index 교체 >> 제일 작은 것이 `idxLowest`가 되는 구조.  
그리고 가장 첫번째로 교체

이런 식으로 두번째 자리 이후 반복