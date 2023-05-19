class CodeBuilder:
    def __init__(self, root_name):
    # todo
        self.root_name = root_name
        self.__root_init = None
        self.lines = []
        self.lines.append(f'class {root_name}:')
        i =  ' ' * (4)
        self.lines.append(f'{i}pass')

    def add_field(self, type, name):
    # todo
        if self.__root_init == None:
            self.__root_init = 1
            i =  ' ' * (4)
            ii = i * 2
            self.lines.pop(-1)
            self.lines.append(f'{i}def __init__(self):')
            self.lines.append(f'{ii}self.{type} = {name}')
        else:
            ii =  ' ' * (8)
            self.lines.append(f'{ii}self.{type} = {name}')
        return self

    def __str__(self):
    # todo
        return '\n'.join(self.lines)


cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0').add_field('position','"engenier"')
print(cb)
print('hey')
del cb
#cb = CodeBuilder('Person').add_field('name', '""') \
#    .add_field('age', '0')
#print(cb)


#class Person:
#    def __init__(self):
#        self.name = ""
#        self.age = 0


