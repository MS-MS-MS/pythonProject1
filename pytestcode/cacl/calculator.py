class Calculator:

    def add(self, a, b):
        """
        加法计算
        :param a:
        :param d:
        :return: a+b
        """
        result = a + b
        return result

    def sub(self, a, b):
        """
        减法计算
        :return:
        """
        result = a - b
        return result

    def mul(self, a, b):
        """
        乘法计算
        :param a:
        :param b:
        :return: a*b
        """
        result = a * b
        return result

    def div(self, a, b):
        """
        除法计算
        :param a:
        :param b:
        :return: a*b
        """
        if b!=0:
            result = a / b
            return result
        else:
            print("除数不能为零")