import sys
class ArgumentParser:
    def __init__(self):
        self.argv = sys.argv[1:]
        self.arg_num = 0
        self.args = {}

    def add_argument(self, flag1, flag2, action = None, nargs='-'):
        self.args[f'arg{self.arg_num}'] = [flag1, flag2, action, nargs]
        self.arg_num += 1

    def parse(self):
        args = {}
        for i in self.argv:
            if '=' in i:
                flag, value = i.split('=')
                for arg in self.args:
                    if flag == self.args[arg][0]:
                        args[self.args[arg][1].split('--')[1]] = value

        for i in range(0, self.arg_num):
            if self.args[f'arg{i}'][0] in self.argv:
                args.update(self.getargs(i))

            elif self.args[f'arg{i}'][1] in self.argv:
                args.update(self.getargs(i))
        
        return args

    def getargs(self, i):
        args = {}
        if self.args[f'arg{i}'][2] == 'without-value':
                args[self.args[f'arg{i}'][1].split('--')[1]] = True
            
        elif self.args[f'arg{i}'][3] == '+':
            num = self.argv.index(self.args[f'arg{i}'][0]) + 1
            _args = []
            while True:
                if self.argv[num][0] != '-':
                    _args.append(self.argv[num])
                else:
                    break
                num += 1
            args[self.args[f'arg{i}'][1].split('--')[1]] = _args
        else:
            args[self.args[f'arg{i}'][1].split('--')[1]] = self.argv[self.argv.index(self.args[f'arg{i}'][0]) + 1]
        return args
