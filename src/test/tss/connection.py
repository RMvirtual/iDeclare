import unittest
from src.main.tss import connection


class TestTssApiConnection(unittest.TestCase):
    def test_should_connect_to_tss(self):
        print(connection.function_to_run())
        self.fail("DUMMY FAIL FOR TSS CONNECTION")


if __name__ == '__main__':
    unittest.main()
