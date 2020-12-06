def size_BT(root):
    # terminating condition

    if root is None:
        return 0

    left_size = size_BT(root.left)
    right_size = size_BT(root.right)

    return left_size + right_size + 1
