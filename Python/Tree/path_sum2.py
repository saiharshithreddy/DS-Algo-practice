class Solution:
    def pathSum(self, root, sum):
        def dfs(root, sum, path_nodes, all_paths):
            if not root:
                return
            # add node to path
            path_nodes.append(root.val)

            if root.val == sum and root.left is None and root.right is None:
                all_paths.append(list(path_nodes))
            else:
                dfs(root.left, sum - root.val, path_nodes, all_paths)
                dfs(root.right, sum - root.val, path_nodes, all_paths)
            # pop the node when its subtrees are traversed.
            path_nodes.pop()

        all_paths = []
        dfs(root, sum, [], all_paths)
        return all_paths
