class Traverse:
    def __init__(self, dot):
        self.i = 0
        self.dot = dot
    # Traverse
    def traverse(self, node):
        # base 1 return
        if node == None:
            return None
        root_key = node.root_key # name of node
        root_value = node.root_value # value of node
        root_shape = node.shape # shape of node
        # base 2
        if root_key in ['id', 'const']:
            # print - draw_node
            var = f"node_{root_key}_{self.i}"
            self.i += 1
            self.dot.node(var, f"{root_key}\n({root_value})", {'color': 'darkseagreen2', 'style': 'filled', 'shape': 'oval'})
            return var

        # determine node by root_key
        if root_key == 'op':
            # print - draw_node
            var = f"node_op_{self.i}"
            self.i += 1
            self.dot.node(var, f"{root_key}\n({root_value})", {'color': 'darkseagreen2', 'style': 'filled', 'shape': 'oval'})

            var_left = self.traverse(node.left)
            if not (var_left == None):
                self.dot.edge(var, var_left)

            var_right = self.traverse(node.right)
            if not(var_right == None):
                self.dot.edge(var, var_right)

            # secret weapon
            with self.dot.subgraph() as s:
                s.attr(rank='same')
                s.node(var_left)
                s.node(var_right)
            self.dot.edge(var_left, var_right, color= 'white')

        elif root_key == 'if':
            # print - draw_node
            var = f"node_if_{self.i}"
            self.i += 1
            self.dot.node(var, f"{root_key}", {'color': 'darkseagreen2', 'style': 'filled', 'shape': 'square'})

            var_test = self.traverse(node.test)
            if not(var_test == None):
                self.dot.edge(var, var_test)
            var_then = self.traverse(node.then)
            if not(var_then == None):
                self.dot.edge(var, var_then)
            var_Else = self.traverse(node.Else)
            if not(var_Else == None):
                self.dot.edge(var, var_Else)

            # secret weapon
            with self.dot.subgraph() as s:
                s.attr(rank='same')
                s.node(var_test)
                s.node(var_then)
                if not (var_Else == None):
                    s.node(var_Else)
            self.dot.edge(var_test, var_then, color='white')
            if not (var_Else == None):
                self.dot.edge(var_then, var_Else, color='white')

            # right_flag = True
            var_next = self.traverse(node.next)
            if not (var_next == None):
                with self.dot.subgraph() as s:
                    s.attr(rank='same')
                    s.node(var)
                    s.node(var_next)
                    s.attr(rank='same')
                self.dot.edge(var, var_next)

              
        elif root_key == 'repeat':
            # print - draw_node
            var = f"node_repeat_{self.i}"
            self.i += 1
            self.dot.node(var, f"{root_key}", {'color': 'darkseagreen2', 'style': 'filled', 'shape': 'square'})

            var_repeat = self.traverse(node.repeat)
            if not(var_repeat == None):
                self.dot.edge(var, var_repeat)
            var_test = self.traverse(node.test)
            if not(var_test == None):
                self.dot.edge(var, var_test)

            # right_flag = True
            var_next = self.traverse(node.next)
            if not(var_next == None):
                with self.dot.subgraph() as s:
                    s.attr(rank='same')
                    s.node(var)
                    s.node(var_next)
                self.dot.edge(var, var_next)


        elif root_key == 'assign':
            # print - draw_node
            var = f"node_assign_{self.i}"
            self.i += 1
            self.dot.node(var, f"{root_key}\n({root_value})", {'color': 'darkseagreen2', 'style': 'filled', 'shape': 'square'})

            var_assign = self.traverse(node.assign)
            if not(var_assign == None):
                self.dot.edge(var, var_assign)

            # right_flag = True
            var_next = self.traverse(node.next)
            if not(var_next == None):
                with self.dot.subgraph() as s:
                    s.attr(rank='same')
                    s.node(var)
                    s.node(var_next)
                self.dot.edge(var, var_next)


        elif root_key == 'read':
            # print - draw_node
            var = f"node_read_{self.i}"
            self.i += 1
            self.dot.node(var, f"{root_key}\n({root_value})", {'color': 'darkseagreen2', 'style': 'filled', 'shape': 'square'})

            # right_flag = True
            var_next = self.traverse(node.next)
            if not(var_next == None):
                with self.dot.subgraph() as s:
                    s.attr(rank='same')
                    s.node(var)
                    s.node(var_next)
                self.dot.edge(var, var_next)


        elif root_key == 'write':
            # print - draw_node
            var = f"node_write_{self.i}"
            self.i += 1
            self.dot.node(var, f"{root_key}", {'color': 'darkseagreen2', 'style': 'filled', 'shape': 'square'})
            var_write = self.traverse(node.write)
            if not(var_write == None):
                self.dot.edge(var, var_write)

            # right_flag = True
            var_next = self.traverse(node.next)
            if not(var_next == None):
                with self.dot.subgraph() as s:
                    s.attr(rank='same')
                    s.node(var)
                    s.node(var_next) # s.attr(rank='same')
                self.dot.edge(var, var_next)

        return var
