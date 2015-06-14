from __future__ import print_function
from __future__ import absolute_import

import sys
import unittest


class TestAssertions(unittest.TestCase):

    def test_equals_ok(self):
        self.assertEquals(0, 0)

    def test_equals_nok_int(self):
        self.assertEquals(1, 2)

    def test_equals_nok_string(self):
        self.assertEquals("Hello world", "Hello World")

    def test_equals_nok_dict(self):
        self.assertEquals(dict(a=1, b=2), dict(a=1, c=3))

    def test_in_nok(self):
        self.assertIn('foo', ('bar', 'baz'))


class TestExceptions(unittest.TestCase):

    def test_divide_zero(self):
        1/0

    def test_long_stack(self):
        def tmp(a):
            return 1/a + tmp(a-1)

        tmp(10)


class TestCapture(unittest.TestCase):

    def test_stdout(self):
        print('a')
        print('b')
        print('c')
        print('d')
        self.assertTrue(False)


class TestAllSucceed(unittest.TestCase):

    def test_ok1(self):
        pass

    def test_ok2(self):
        pass

    def test_ok3(self):
        pass

    def test_ok4(self):
        pass

    def test_ok5(self):
        pass

    def test_ok6(self):
        pass

    def test_ok7(self):
        pass

    def test_ok8(self):
        pass

    def test_ok9(self):
        pass

    def test_ok10(self):
        pass

    def test_ok11(self):
        pass

    def test_ok12(self):
        pass

    def test_ok13(self):
        pass

    def test_ok14(self):
        pass

    def test_ok15(self):
        pass

    def test_ok16(self):
        pass

    def test_ok18(self):
        pass

    def test_ok19(self):
        pass

    def test_ok20(self):
        pass

    def test_ok21(self):
        pass

    def test_ok22(self):
        pass

    def test_ok23(self):
        pass

    def test_ok24(self):
        pass

    def test_ok25(self):
        pass
