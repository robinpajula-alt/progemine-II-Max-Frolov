import unittest

class CombinationLock():
    def __init__(self, combination):
        self.combination = combination
        self.status = "LOCKED"
        self.code = []
        self.code_w = ""

    def enter_digit(self, digit):
        code = self.code
        code.append(digit)
        self.code_w = ""
        for num in code:
            self.code_w += str(num)
        self.check_status()

    def check_status(self):
        if self.code == self.combination:
            self.status = "OPEN"
        elif self.code != self.combination[:len(self.code)]:
            self.status = "ERROR"
        else:
            self.status = self.code_w

class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)