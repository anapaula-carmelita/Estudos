

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        root.level = 0
        return 0
    
    n = height(root.left)
    m = height(root.right)
    if n >= m:
        return n + 1
    else:
        return m + 1
    
