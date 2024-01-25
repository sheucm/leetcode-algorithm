# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        res = []
        def dfs(v):
            if not v:
                res.append('N')
                return
            res.append(str(v.val))
            dfs(v.left)
            dfs(v.right)
        dfs(root)
        return ",".join(res)


        ### Solution2: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # res = []
        # def bfs(v):
        #     q = [v]
        #     while q:
        #         v = q.pop(0)
        #         if not v:
        #             res.append('N')
        #             continue
        #         res.append(str(v.val))
        #         q.append(v.left)
        #         q.append(v.right)
        # bfs(root)
        # return ",".join(res)
        

    def deserialize(self, data):
        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        vals = data.split(',')
        idx = 0
        def dfs():
            nonlocal idx
            node = None
            val = vals[idx]
            idx += 1
            if val != 'N':
                node = TreeNode()
                node.val = val
                node.left = dfs()
                node.right = dfs()
            return node
        return dfs()


        ### Solution2: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # vals = data.split(',')
        # def bfs():
        #     if vals[0] == 'N': return None
        #     root = TreeNode(); root.val = vals.pop(0)
        #     q = [root]
        #     while q:
        #         v = q.pop(0)
        #         ## Left
        #         val = vals.pop(0)
        #         if val != 'N':
        #             v.left = TreeNode()
        #             v.left.val = val
        #             q.append(v.left)
        #         ## Right
        #         val = vals.pop(0)
        #         if val != 'N':
        #             v.right = TreeNode()
        #             v.right.val = val
        #             q.append(v.right)
        #     return root
        # return bfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))