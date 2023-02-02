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

        
class make_repeat_Node:  # repeat have 2 childs

    def __init__(self, root_node):
        self.root_key = 'repeat'
        self.root_value = root_node['tokenvalue']
        self.shape = 'square'
        self.next = None

    def test_child(self, node):
        self.test = node

    def repeat_child(self, node):
        self.repeat = node

    def next_child(self, node):
        self.next = node


class make_assign_Node:  # write have 1 childs

    def __init__(self, root_node):
        self.root_key = 'assign'
        self.root_value = root_node['tokenvalue']  # ely 2blo => make_assign_Node([index-1])
        self.shape = 'square'
        self.next = None

    def assign_child(self, node):
        self.assign = node

    def next_child(self, node):
        self.next = node


class make_read_Node:  # read have 0 childs

    def __init__(self, root_node):
        self.root_key = 'read'
        self.root_value = root_node['tokenvalue']  # READ -> (match('READ'), make_read_node())
        self.shape = 'square'
        self.next = None

    def next_child(self, node):
        self.next = node


class make_write_Node:  # write have 3 childs

    def __init__(self, root_node):
        self.root_key = 'write'
        self.root_value = root_node['tokenvalue']  # mosh mohm
        self.shape = 'square'
        self.next = None

    def write_child(self, node):
        self.write = node

    def next_child(self, node):
        self.next = node
