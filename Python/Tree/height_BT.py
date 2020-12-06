def height(root):
    if root is None:
        return 0

    left_h = height(root.left)
    right_h = height(root.right)

    return max(left_h, right_h) + 1
