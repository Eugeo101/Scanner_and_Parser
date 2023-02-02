class makeOpNode:  # op so have left/right

    def __init__(self, root_node):
        self.root_key = 'op'
        self.root_value = root_node['tokenvalue']
        self.shape = 'oval'

    def left_child(self, node):
        self.left = node

    def right_child(self, node):
        self.right = node


class make_Id_Const_Node:  # id/const so have no childs

    def __init__(self, root_node):
        temp = 'const'
        if root_node['tokentype'] == 'IDENTIFIER':
            temp = 'id'

        self.root_key = temp
        self.root_value = root_node['tokenvalue']
        self.shape = 'oval'


class make_if_Node:  # if have 3 childs

    def __init__(self, root_node):
        self.root_key = 'if'
        self.root_value = root_node['tokenvalue']
        self.shape = 'square'
        self.Else = None
        self.next = None

    def test_child(self, node):
        self.test = node

    def then_child(self, node):
        self.then = node

    def else_child(self, node):
        self.Else = node

    def next_child(self, node):
        self.next = node
