# Binary Search


Binary search is one of the divide and conquer algorithm.

- recursive call method
```java
class BinarySearch {
    public static boolean binarySearch(int[] arr, int target, int left, int right) {
        if (left > right) {
            return false;
        }

        int mid = (left + right) / 2;

        if (arr[mid] == target) {
            return true;
        }

        if (arr[mid] < target) {
            return binarySearch(arr, target, mid + 1, right);
        } else {
            return binarySearch(arr, target, left, mid - 1);
        }
    }

    public static void main(String[] args) {
        int[] arr = {6, 5, 1, 4, 7, 2, 3};
        int target = 7;

        sort(arr);
        binarySearch(arr, target, 0, arr.length - 1);
    }
}
```
$n$ X $1/2$ X $1/2$ X $1/2$ X ... = 1

$n$ = $2^k$

Time Complexity: $O(logn)$

<br>

# example

```
N = 5
NArr = {4, 1, 5, 2, 3}
M = 5
MArr = {1, 3, 7, 9, 5}

result:
1
1
0
0
1
```


```java
class Example {
    static void solve(int n, int[] nArr, int m, int[] mArr) {
        for(int i = 0; i < m; i++) {
            if (BinarySearch.binarySearch(nArr, mArr[i], 0, n - 1)) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }

    public static void main(String[] args) {
        int N = 5;
        int[] NArr = {4, 1, 5, 2, 3};
        int M = 5;
        int[] MArr {1, 3, 7, 9, 5};

        solve(N, NArr, M, MArr);
    }
}
```
Time Complexity: $O(MlogN)$