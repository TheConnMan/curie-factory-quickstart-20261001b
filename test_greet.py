import greet
import unittest


class TestGreet(unittest.TestCase):
    def test_greet_ada(self):
        self.assertEqual(greet.greet("ada"), "hello, ada")


if __name__ == "__main__":
    unittest.main()
