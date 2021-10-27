import sys
class ArgumentParser:
    def __init__(self):
        self.argv = sys.argv[1:]
        self.arg_num = 0
        self.args = {}

    def add_argument(self, flag1, flag2 = None, action = None, nargs='-'):
        #globals()[flag1] = None
        self.args[f'arg{self.arg_num}'] = [flag1, flag2, action, nargs]
        self.arg_num += 1

    def parse(self):
        num = 0
        num1 = 0
        args = {}
        while True:
            if not self.args[f'arg{num}'][1] == None:
                if self.args[f'arg{num}'][0] in self.argv or self.args[f'arg{num}'][1] in self.argv:
                    if self.args[f'arg{num}'][2] == 'without_value':
                        args[self.args[f'arg{num}'][1].split('--')[1]] = True
                    else:
                        if self.args[f'arg{num}'][3] == '-':
                            if self.args[f'arg{num}'][0] in self.argv:
                                args[self.args[f'arg{num}'][1].split('--')[1]] = self.argv[self.argv.index(self.args[f'arg{num}'][0]) + 1]
                            elif self.args[f'arg{num}'][1] in self.argv:
                                args[self.args[f'arg{num}'][1].split('--')[1]] = self.argv[self.argv.index(self.args[f'arg{num}'][1]) + 1]
                            else:
                                args[self.args[f'arg{num}'][1].split('--')[1]] = False
                        elif self.args[f'arg{num}'][3] == '+':
                            if self.args[f'arg{num}'][0] in self.argv:
                                num1 = self.argv.index(self.args[f'arg{num}'][0]) + 1
                                _nargs = []
                                while True:
                                    try:
                                        if not self.argv[num1][0] == '-':
                                            _nargs.append(self.argv[num1])
                                        else:
                                            break
                                    except IndexError:
                                        break
                                    num1 += 1
                                args[self.args[f'arg{num}'][1].split('--')[1]] = _nargs
                else:
                    if self.args[f'arg{num}'][2] == 'without_value':
                        args[self.args[f'arg{num}'][1].split('--')[1]] = False
                    else:
                        args[self.args[f'arg{num}'][1].split('--')[1]] = None
                if len(self.args) - 1 == num:
                    break
                num += 1
            else:
                num1 = 0
                #_num = 0
                _nargs = []
                _exceptions = [None, False, True]
                while True:
                    try:
                        if not self.argv[num1][0] == '-':
                            _num = 0
                            _num1 = 0
                            while True:
                                if not self.args[f'arg{_num}'] == self.args[list(self.args)[-1]]:
                                    if not self.args[f'arg{_num}'][1] == None:
                                        if args[self.args[f'arg{_num}'][1].split('--')[1]] in _exceptions:
                                            _num1 += 1
                                            print('if done', _num1)
                                        print('len args', args)
                                        print(self.args)
                                        if _num1 == len(args):
                                            pass
                                            _nargs.append(self.argv[num1])
                                    _num += 1
                            
                                else:
                                    break
                                    
                                
                        else:
                            num1 += 1
                    except IndexError:
                        break
                    num1 += 1
                args[self.args[f'arg{num}'][0]] = _nargs
                break
        return args
