Debugging

When i run this Calendar.py file there one error encounter 
AttributeError: 'NoneType' object has no attribute 'insert'

Then after debugging this file i found 2 issue 

1) When comparison happening  between nodes then node.end >= self.start according to this code existing node should be 
greater than current one but loggicaly it should be node.end <= self.start same for this also node.start <= self.end should be
node.start >= self.end.
2) And elif part we are inserting new node in left subtree, but it should be in right subtree e.g. return self.right_child.insert(node)
3) after elif if no condition match then default false should be return
