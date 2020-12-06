class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        Idea:
        inorder traversal will give you sorted list
        left most node will be smallest node
        right most node will be largest node
        smallest's left field should point to largest node
        largest's right field should point to smallest
        other nodes must have two way links
        '''

        if not root:
            return

        def inorder(node):
            nonlocal first_node, last_node
            if not node:
                return

            # left
            inorder(node.left)

            # root
            # in inorder the left most node is visited first. so update first_node
            if not first_node:
                first_node = node
            # first_node remains the left most node

            else:
                # linking smaller val to next larger value
                last_node.right = node
                # last node will be updating in an incrementing value because of inorder traversal.
                # reverse link
                node.left = last_node

            # update the last node as every node is visited
            last_node = node

            # right
            inorder(node.right)

        first_node = None
        last_node = None
        inorder(root)

        # first node should have a reverse link to the last node
        first_node.left = last_node
        # last node should point to first node
        last_node.right = first_node

        return first_node
