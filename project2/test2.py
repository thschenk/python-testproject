from __future__ import absolute_import

import sys
import unittest


class Project2Test(unittest.TestCase):

    def test_equals_ok(self):
        self.assertEquals(0, 0)

    def test_equals_nok_int(self):
        self.assertEquals(1, 2)

    def test_in_nok(self):
        self.assertIn('foo', ('bar', 'baz'))

    def test_divide_zero(self):
        1/0
