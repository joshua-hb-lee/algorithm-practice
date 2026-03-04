# Stack

```java
public class Stack {
  private int[] elements;
  private int top;

  private static final int INIT_TOP = -1;

  Stack(int limitSize) {
    this.elements = new int[limitSize];
    this.top = INIT_TOP;
  }

  public void push(int element) {
    if (isFull()) {
      throw new IllegalStateException("Stack is full");
    }

    elements[++top] = element;
  }

  public int pop() {
    if (isEmpty()) {
      throw new IllegalStateException("Stack is empty");
    }

    return elements[top--];
  }

  private boolean isFull() {
    return elements.length == top + 1;
  }

  private boolean isEmpty() {
    return top == INIT_TOP;
  }
}
```

<br>

# Queue

Queue is usually implemented with circular method.

```java
public class CircularQueue {
  private int[] elements;
  private int front;
  private int rear;
  private int currentSize;

  private static final int INIT_TOP = -1;

  CircularQueue(int limitSize) {
    this.currentSize = 0;
    this.front = 0;
    this.rear = 0;
    this.elements = new int[limitSize];
  }

  public void enqueue(int element) {
    if (isFull()) {
      throw new IllegalStateException("Queue is full");
    }

    elements[rear] = element;
    rear = (rear + 1) % elements.length;
    currentSize++;
  }

  public int dequeue() {
    if (isEmpty()) {
      throw new IllegalStateException("Queue is empty");
    }

    int target = elements[front];
    front = (front + 1) % elements.length;
    currentSize--;

    return target;
  }

  private boolean isEmpty() {
    return currentSize == 0;
  }

  private boolean isFull() {
    return currentSize == elements.length;
  }

  public static void main(String[] args) {
    CircularQueue queue = new CircularQueue(3);

    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    System.out.println(queue.dequeue());
    System.out.println(queue.dequeue());
    System.out.println(queue.dequeue());
  }
}
```