# This is an input class.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluateExpressionTree(tree):
    # if the node has no children, just return the value
    if tree.left is None:
        return tree.value

    if tree.value == -1:
        return evaluateExpressionTree(tree.left) + evaluateExpressionTree(tree.right)
    elif tree.value == -2:
        return evaluateExpressionTree(tree.left) - evaluateExpressionTree(tree.right)
    elif tree.value == -3:
        return int(evaluateExpressionTree(tree.left) / evaluateExpressionTree(tree.right))
    else:
        return evaluateExpressionTree(tree.left) * evaluateExpressionTree(tree.right)
