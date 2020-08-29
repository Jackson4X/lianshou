# 已知二叉树的前序和中序，求二叉树的后序
# 第一种方法：直接进行后序创建
# 第二种方法：先构建二叉树，在对二叉树进行后序遍历
# 这类题的总结：前序的第一个是根；后序的最后一个是根；中序用来判别左右子树的划分；
#            前序序列中的左子树部分的第一个节点是左子树的根节点；
#            前序序列中的右子树部分的第一个节点是右子树的根节点

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 1:
            print(preorder[0])
            return preorder[0]
        if len(preorder) == 0:
            return

        idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])

        l = self.buildTree(preorder[1: 1+idx], inorder[:idx])
        r = self.buildTree(preorder[1+idx:], inorder[idx+1:])

        root.left = l
        root.right = r
        print(root.val)
        return root


    # 第二种方法，先建立二叉树，再进行后序遍历
    #     if not preorder:
    #         return None
    #     idx = inorder.index(preorder[0])
    #     root = TreeNode(preorder[0])
    #     l = self.buildTree(preorder[1:1+idx], inorder[:idx])
    #     r = self.buildTree(preorder[1+idx:], inorder[1+idx:])
    #
    #     root.left = l
    #     root.right = r
    #
    #     return root
    #
    # def postTraversal(self, root):
    #     if root != None:
    #         self.postTraversal(root.left)
    #         self.postTraversal(root.right)
    #         print(root.val)
preorder=['H', 'G', 'E', 'D', 'B', 'F', 'C', 'A']
inorder=['E', 'G', 'B', 'D', 'H', 'F', 'A', 'C']
S = Solution()
root = S.buildTree(preorder, inorder)
# S.postTraversal(root)