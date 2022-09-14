from unittest import TestCase

import demo.foo as foo


class TestAdd(TestCase):
    """The trivial one that follows unittest framework."""

    def setUp(self):
        self.a = 1

    def test_1(self):
        out = foo.add(self.a, 2)
        self.assertEqual(out, 3)

    def test_2(self):
        out = foo.add(self.a, 5)
        self.assertEqual(out, 6)
