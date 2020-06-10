class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None


class CategoryTree:
	def __init__(self):
		self.root = TreeNode(None)


	def add_category(self, category, parent):
		if not parent:
			self.root = TreeNode(category)
		else:
			self.dfs(self.root, category, parent)

	def dfs(self, root, category, parent):
		if not root:
			return

		if root.val == parent:
			if not root.left:
				root.left = TreeNode(category)
			else:
				root.right = TreeNode(category)
			return

		self.dfs(root.left, category, parent)
		self.dfs(root.right, category, parent)

	def get_children(self, parent):
		
		if not parent:
			return []

		if root.val == parent:
			if root.left and root.right:
				return [root.left.val, root.right.val]
			elif root.left:
				return [root.left.val]
			elif root.right:
				return [root.right.val]

		self.get_children(root.left, parent)
		self.get_children(root.right, parent)

c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(','.join(c.get_children('D')))

