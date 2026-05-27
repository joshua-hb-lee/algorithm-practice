# Binary Search Tree

```
      5
     / \
    3   7
   / \
  2   4
```

## Preorder traversal
```
Root → Left → Right
5 → 3 → 2 → 4 → 7
```

```python
def preorder_iterative(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def preorder(root):
    # use list object, not private primitive variable
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)  # Root
        dfs(node.left)           # Left
        dfs(node.right)          # Right

    dfs(root)
    return result
```

## Inorder traversal
```
Left → Root → Right
2 → 3 → 4 → 5 → 7
```

```python
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    while current or stack:
        # move to left side
        while current:
            stack.append(current)
            current = current.left
        # pop
        current = stack.pop()
        result.append(current.val)
        # move to right
        current = current.right
    return result

def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result
```

# Postorder traversal
```
Left → Right → Root
2 → 4 → 3 → 7 → 5
```

```python
def postorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)           # Left
        dfs(node.right)          # Right
        result.append(node.val)  # Root
    dfs(root)
    return result
```