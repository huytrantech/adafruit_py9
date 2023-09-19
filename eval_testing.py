print('Test Eval')


class EvalEquation(object):
    def __init__(self, equation):
        self.equation = equation

    def set_equation(self, equation):
        self.equation = equation

    def cal_eval(self, x1, x2, x3):
        return modify_value(self.equation, x1, x2, x3)


def modify_value(equation, x1, x2, x3):
    result = eval(equation)
    return result
