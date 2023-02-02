from utils import *

class Parser:
    def __init__(self, token_list):
        self.token_list = token_list
        self.index = 0
        self.accept = False

    def match(self, expected_token):
        if self.token_list[self.index]['tokentype'] == expected_token:
            self.index += 1
            if (self.index == len(self.token_list)):
                self.accept = True
        else:
            self.error(self.index)
    def program(self):
        return self.stmt_sequence()

    def stmt_sequence(self):  # read -> if correct
        temp_intital = self.statement()  # read
        temp = temp_intital
        while ((self.accept == False) and (self.token_list[self.index]['tokenvalue'] == ';')):
            self.match('SEMICOLON')  # self.token_list[self.index]['tokenvalue']
            new_temp = self.statement()  # assign
            temp.next_child(new_temp)
            temp = new_temp
        return temp_intital

    def statement(self):
        token_type = self.token_list[self.index]['tokentype']
        if token_type == 'IF':
            return self.if_stmt()

        elif token_type == 'REPEAT':
            return self.repeat_stmt()

        elif token_type == 'IDENTIFIER':  # ASSIGN
            return self.assign_stmt()

        elif token_type == 'READ':
            return self.read_stmt()

        elif token_type == 'WRITE':
            return self.write_stmt()

        else:
            self.error(self.index)

    def if_stmt(self):
        temp = make_if_Node(self.token_list[self.index])
        self.match('IF')
        temp.test_child(self.exp())
        self.match('THEN')
        temp.then_child(self.stmt_sequence())
        if (self.token_list[self.index]['tokentype'] == 'ELSE'):
            self.match('ELSE')
            temp.else_child(self.stmt_sequence())
        self.match('END')
        return temp

    def repeat_stmt(self):
        temp = make_repeat_Node(self.token_list[self.index])
        self.match('REPEAT')
        temp.repeat_child(self.stmt_sequence())
        self.match('UNTIL')
        temp.test_child(self.exp())
        return temp

    def assign_stmt(self):
        temp = make_assign_Node(self.token_list[self.index])
        self.match('IDENTIFIER')
        self.match('ASSIGN')
        temp.assign_child(self.exp())
        return temp

    def read_stmt(self):
        self.match('READ')
        temp = make_read_Node(self.token_list[self.index])
        self.match('IDENTIFIER')
        return temp

    def write_stmt(self):
        temp = make_write_Node(self.token_list[self.index])
        self.match('WRITE')
        temp.write_child(self.exp())
        return temp

    def exp(self):
        temp = self.simple_exp()
        if ((self.accept == False) and ((self.token_list[self.index]['tokentype'] == 'LESSTHAN') or (
                self.token_list[self.index]['tokentype'] == 'EQUAL'))):
            new_temp = makeOpNode(self.token_list[self.index])
            self.match(self.token_list[self.index]['tokentype'])
            new_temp.left_child(temp)
            new_temp.right_child(self.simple_exp())
            temp = new_temp
        return temp

    def simple_exp(self):
        temp = self.term()
        while ((self.accept == False) and ((self.token_list[self.index]['tokentype'] == 'PLUS') or (
                self.token_list[self.index]['tokentype'] == 'MINUS'))):
            new_temp = makeOpNode(self.token_list[self.index])
            self.match(self.token_list[self.index]['tokentype'])
            new_temp.left_child(temp)
            new_temp.right_child(self.term())
            temp = new_temp
        return temp

    def term(self):
        temp = self.factor()
        while ((self.accept == False) and ((self.token_list[self.index]['tokentype'] == 'MULT') or (
                self.token_list[self.index]['tokentype'] == 'DIV'))):
            new_temp = makeOpNode(self.token_list[self.index])
            self.match(self.token_list[self.index]['tokentype'])
            new_temp.left_child(temp)
            new_temp.right_child(self.factor())
            temp = new_temp
        return temp

    def factor(self):
        if (self.token_list[self.index]['tokentype'] == 'OPENBRACKET'):
            self.match('OPENBRACKET')
            temp = self.exp()
            self.match('CLOSEDBRACKET')
        elif (self.token_list[self.index]['tokentype'] == 'NUMBER'):
            temp = make_Id_Const_Node(self.token_list[self.index])
            self.match('NUMBER')
        elif (self.token_list[self.index]['tokentype'] == 'IDENTIFIER'):
            temp = make_Id_Const_Node(self.token_list[self.index])
            self.match('IDENTIFIER')
        else:
            self.error(self.index)
        return temp

    def error(self, index):
        raise ValueError('SyntaxError', self.token_list[self.index]['tokentype'])