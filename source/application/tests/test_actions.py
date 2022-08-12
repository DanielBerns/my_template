from pathlib import Path
from context import actions

import unittest


class ActionsTestCase(unittest.TestCase):
        
    def test_demo(self):
        print('\n')
        actions.demo.api.simple_demo()


if __name__ == '__main__':
    unittest.main(verbosity=2)
